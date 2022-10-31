import json
import requests
import time
import hmac
import hashlib
import base64
import urllib.parse

class DingAPI:
    def __init__(self, title, web_hook, key):
        self.web_hook = web_hook
        self.headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        self.title = title
        self.key = key

    def get_timestamp(self):
        timestamp = str(round(time.time() * 1000))
        return timestamp

    def get_sign(self, timestamp):
        secret = self.key
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return str(sign)


    def send(self, text):
        time_stamp = self.get_timestamp()
        sign = self.get_sign(time_stamp)

        url = self.web_hook + "&timestamp=" + time_stamp + "&sign=" + sign

        summary = json.dumps({'msgtype': 'markdown',
          'markdown' : { 'title':self.title, 'text' : text}})
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

        print(url)
        print(summary)
        r = requests.post(url, data=summary, headers=headers)
        print(r)

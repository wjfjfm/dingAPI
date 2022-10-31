# Ding Ding Robot API

## Quick Start

get your own access_token and secret key, then:

```python
api = DingAPI(title="Hello World",
              web_hook='https://oapi.dingtalk.com/robot/send?access_token=xxxxxxxx',
              key="xxxxxxxxxx")
api.send("hello, this is a message to send")
```

#!/user/bin/env python
# -*- coding: utf-8 -*-

import requests

url = 'https://open.weixin.qq.com/sdk/report?v=1&o=0&s=2&c=7.0.4&a=wxce3f1a51aa60f801&n=wifi&i=3558&p=833&u=http%3A%2F%2Flujingang.mikecrm.com%2FgGlrgkF'
header = {
    "User-Agent":'Mozilla/5.0 (Linux; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044807 Mobile Safari/537.36 MMWEBID/4351 MicroMessenger/7.0.4.1420(0x2700043A) Process/tools NetType/WIFI Language/zh_CN'
}
req = requests.get(url,headers=header)
print(req)
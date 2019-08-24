import requests
from lxml import etree
import json

city = input()
req = requests.get(' http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
# json字符串
html = req.text
# 转化成 dict 便于处理数据
ds = json.loads(html)['data']


# 天气类的定义
class Weather:
    def __init__(self, data):
        self.city = data['city']
        self.date = data['forecast'][0]['date']
        self.high_tem = data['forecast'][0]['high']
        self.low_tem = data['forecast'][0]['low']
        self.type = data['forecast'][0]['type']

    # 今日天气
    def today(self):
        print(self.city + '\n' + self.date + '\n' + self.high_tem + '\n' + self.low_tem + '\n' + self.type)


if __main__ = ''
weather = Weather(ds)
weather.today()

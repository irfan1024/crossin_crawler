import requests
import json



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

#获取数据函数
def weather_data(city):
    try:
        req = requests.get(' http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
        # json字符串
        html = req.text
        # 转化成 dict 便于处理数据
        #对于这里的数据处理，可以不需要 json 模块，直接对于返回的数据
        #req进行req.json()进行处理就可以得到json转化之后的字典了
        ds = json.loads(html)['data']
        return ds
    except:
        print("查询失败，请重新输入")
        return False


#主程序
if __name__ == '__main__':
    while True:
        city = input('请输入要查询的城市(中文)\n')
        #注意数据正确性的验证！
        if not city:
            break

        ds = weather_data(city)
        if not ds:
            continue
        weather = Weather(ds)
        weather.today()

import requests

url = 'https://weibo.com/a/hot/realtime'
#通过 network 标签的 respond 查找到 user-agent, cookies
cookie = '#######'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
headers = {'User-Agent': user_agent,
           'Cookie': cookie}
#将网页结构转成字符串
req = requests.get(url, headers=headers).text
#写入文件，需要进行解码
with open('sina.html', 'w', encoding='utf-8') as f:
    f.write(req)
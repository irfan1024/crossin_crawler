import requests

url = 'https://weibo.com/a/hot/realtime'
#通过 network 标签的 respond 查找到 user-agent, cookies
cookie = 'Ugrow-G0=1ac418838b431e81ff2d99457147068c; login_sid_t=09f89fd8d0c69c465a3c1b2a6de3ea6a; cross_origin_proto=SSL; YF-V5-G0=a5a6106293f9aeef5e34a2e71f04fae4; _s_tentry=-; Apache=5430104758602.496.1566702234289; SINAGLOBAL=5430104758602.496.1566702234289; ULV=1566702235154:1:1:1:5430104758602.496.1566702234289:; WBStorage=f54cf4e4362237da|undefined; SUB=_2AkMqPgVCf8NxqwJRmP4TzGnjZY9-yQ_EieKcYvSZJRMxHRl-yT83qmUQtRB6Ab4rrYA4wbCLjE5-7G45MTR436Z9XdGi; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9Whv0Qri-foOiP47bDwMqbEv'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
headers = {'User-Agent': user_agent,
           'Cookie': cookie}
#将网页结构转成字符串
req = requests.get(url, headers=headers).text
#写入文件，需要进行解码
with open('sina.html', 'w', encoding='utf-8') as f:
    f.write(req)
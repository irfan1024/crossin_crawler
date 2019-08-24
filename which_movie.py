import requests
import json

url = 'https://api.douban.com/v2/movie/1292052?apikey=0df993c66c0c636e29ecbb5344252a4a'
req = requests.get(url)
html = req.text
ds = req.json()

print(ds)
import requests
import bs4
import csv


#写入函数
def file_w(rows, headers):
    with open('lianjia.csv', 'w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)

#获取数据函数
def catch_data(datas, headers):
    try:
        for data in datas:
            title = data.select('div > p > a')[0].get_text()
            add = ''
            for i in range(1, 4):
                add += data.select('div > p > a')[i].get_text()
                if i != 3:
                    add += "-"
            area =data.select('div > p')[1].get_text().split('\n')[3]
            fangxiang = data.select('div > p')[1].get_text().split('\n')[4]
            huxing = data.select('div > p')[1].get_text().split('\n')[5]
            louceng = data.select('div > p')[1].get_text().split('\n')[7]
            tab_list_is = data.find_all(attrs={"class": "content__list--item--bottom oneline"})[0].find_all('i')
            tab_list = ''
            for tab_list_i in tab_list_is:
                tab_list += tab_list_i.get_text()
                tab_list += '-'
            row = (title, add, area, fangxiang, huxing, louceng, tab_list)
            rows.append(row)
        file_w(rows, headers)
    except:
        print("数据获取错误")

#主函数
if __name__ == '__main__':
    url = 'https://sh.lianjia.com/zufang/'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
    cookie = 'lianjia_uuid=8e493532-6a8b-47d7-94ff-8af97e1594a2; UM_distinctid=16cd279b81019f-0254e61ffab71f-5f4e2917-100200-16cd279b81118d; all-lj=8e5e63e6fe0f3d027511a4242126e9cc; CNZZDATA1256793290=599035166-1566895109-https%253A%252F%252Fcrossincode.com%252F%7C1566900509; lianjia_ssid=f5568dbe-8182-4f8d-8d91-84c106c5bb13; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiOGIyYmJhM2YxZGViOTBkYWE1MzEzMmM1YzcwMjZhYzUwMWJiZGE2NjI0OWMzOGVlZjdmYzQxMjNiODVmNTEzNWM2ZmNiZDFkNTQzZDI0MGM4YTI1MjI4YzkwZWM1MjdkZWJhZmE4ZGY1NmY1YmFhZjg5OGJiMDRlOTRiZjRkMmM0ZDcxZWIwZDcwNGNhNDliOTAwMTc2NmM0MzY3ZDhkY2I4NzYzOWM2Mjc0NDlhYzg5NDM5ZjA4OTE3NTliMjcxYzNhMmVlMjM5MGE0YzEyMDg3MGFhMTQ3ZTRlNDg4OTY1MTAzMWI0NzczMmI0ZTE5MmQ3YmQ2NjZlYTI5ZjdkMTY1NDQzNmNlMWQyMjMwYjY5OWE0NWNiM2EzY2ExMmVjZTcyZWViY2E1ODRmM2RjNTdlZTQwY2RhZDM3MDlhYzYzZTg4NjI1NmZhODIyYzlmMGFmNTIyYjc5MzExMGI1YlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIwODg3MWUyMlwifSIsInIiOiJodHRwczovL3NoLmxpYW5qaWEuY29tL3p1ZmFuZy8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ=='
    header = {
        "User-Agent": user_agent,
        "Cookie": cookie,
    }
    req = requests.get(url, headers=header)
    html = req.text

    # 创建beautifulsoup的对象, 不使用lxml的解析器,虽然可以运行,却会报警告..
    soup = bs4.BeautifulSoup(html, 'lxml')
    datas = soup.find_all('div', class_='content__list--item')
    headers = ['标签', '地址', '面积', '方位', '户型', '楼层', '特征']
    rows = []

    catch_data(datas, headers)
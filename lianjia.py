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
    cookie = '######'
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
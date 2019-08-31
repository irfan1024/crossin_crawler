#!/user/bin/env python
#-*- coding"utf-8 -*-

import requests
import bs4
import csv

#获取详情页信息
def detail(positionURL):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.3',
        "Cookies": '#######'
    }
    try:
        r = requests.get(positionURL, headers=headers)
        text_r = r.text
        soup = bs4.BeautifulSoup(text_r, 'lxml')
        pos_detail = soup.find_all('div', class_='describtion__detail-content')[0].get_text()
        return pos_detail
    except Exception as f:
        print("f", f)
        print("获取详情页失败")
        return ' '
#文件写入
#当时在写入数据的时候出错频繁, 总是报gbk无法解码某个 unicode 码,所以,要在open的参数中加入编码的'utf-8'
def file_w(rows, header):
    try:
        with open('zhaopin.csv', 'w', newline='', encoding='utf-8') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(header)
            f_csv.writerows(rows)
    except Exception as a:
        print('写入数据使错误')

#获取网上数据函数
def datas(html):
    row = ()
    rows = []
    if html['code'] == 200:
        header = ['招聘条数', '职位', '薪水', '学历要求', '工作经验要求', '招聘详细页url', '详情', '是否全职', '公司名', '公司类型', '公司规模']
        data = html['data']
        results = data['results']

        for result in results:
            # 注释
            count = data['count']
            jobname = result['jobName']
            salary = result['salary']
            eduLevel = result['eduLevel']['name']
            workingExp = result['workingExp']['name']
            positionURL = result['positionURL']
            emplType = result['emplType']
            com_name = result['company']['name']
            com_type = result['company']['type']['name']
            com_size = result['company']['size']['name']
            pos_detail = detail(positionURL)
            row = (count, jobname, salary, eduLevel, workingExp, positionURL, pos_detail, emplType, com_name, com_type, com_size)
            rows.append(row)
        file_w(rows, header)
    else:
        print("获取信息错误")

if __name__ == '__main__':
    url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=568&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&_v=0.27141451&x-zp-page-request-id=c13ba3a94c6144b2809453a344c7b68e-1567054908480-225018&x-zp-client-id=c6730fd1-7c40-4d2e-ed7e-a7d0cff48a02'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.3',
        "Cookies": '#########'
    }
    try:
        req = requests.session().get(url, headers=headers)
        html = req.json()
    except:
        print('获取数据错误')
        html = { 'code' : 000}
    datas(html)



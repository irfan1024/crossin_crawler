#!/user/bin/env python
# -*- coding: utf-8 -*-

import requests
import bs4
import pdfkit
import time



#访问函数
def get_data(url):
    header = {
        "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Cookie' : 'pgv_pvi=9950813184; pgv_si=s2315359232; csrftoken=qmEz24wfcFPROFWzFNcfmxhuPuVsvbZeq8e577EY9BL7JYGOYvJbYzp5ZoLXK2Oc; sessionid=7ykqnjqjvenskt7qktetxwiy04t8yfao',
    }
    try:
        req = requests.get(url, headers=header)
        html_json = req.text
        html = bs4.BeautifulSoup(html_json, 'lxml')
    except:
        print('访问函数中获取数据错误')
        html = ''
    return html

#获取首页
def get_first_page():
    url = 'https://python666.cn/cls/lesson/list'
    header = {
        "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            "Cookie" : "pgv_pvi=374220800; pgv_si=s1044332544",
    }
    req = requests.get(url, headers=header)
    html_json = req.text
    html = bs4.BeautifulSoup(html_json, 'lxml')
    filename = html.find_all('a', class_='first-page')[0].get_text()
    html.find('img')['src'] = '../crawle_crossin_class/crossin.jpg'
    content = html.find('div', class_='ppx-main-block').prettify()
    try:
        with open('%s.html' % filename, 'w', encoding='utf-8') as f:
            f.write(content)
    except:
        print('获取首页错误!')
    first_page = filename + '.html'
    return first_page


#获取课程
def get_classes(first_page):
    htmls = []
    shit = 0
    url = 'https://python666.cn/cls/lesson/1'
    while True:
        html = get_data(url)
        next_list = 'https://python666.cn/cls/lesson' + html.find('li', class_='next').select('li > a')[0][
            'href'].strip('..')
        print(next_list)
        content1 = str(shit) + html.find('div', class_='ppx-main-block').prettify()#prettify这个方法是用来优化html页面并可以显示图片!
        title = html.find('a', class_='list-group-item-info').get_text()
        htmls.append(title + '.html')
        try:
            with open('%s.html' % title, 'w', encoding='utf-8') as f:
                        f.write(content1)
        except:
            print(title, '获取课程错误!')
        if next_list == 'https://python666.cn/cls/lesson/list':
            break
        else:
            url = next_list
            shit += 1
    print(htmls)
    htmltopdf(htmls,first_page)

#pdf转化函数
def htmltopdf(htmls, first_page):
    #wkhtmltopdf这里必须要有安装路径,以及出现了中文编码问题,需要在options中进行设置
    path_wk = r"D:\pdfkit\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_wk)
    options = {
        'page-size' : 'A4',
        'encoding' : 'UTF-8',
    }
    cover = first_page
    pdfkit.from_file(htmls, 'python666.pdf', configuration=config, options=options, cover=cover)

#pdf转化函数
def htmltopdf1(htmls):
    #wkhtmltopdf这里必须要有安装路径,以及出现了中文编码问题,需要在options中进行设置
    path_wk = r"D:\pdfkit\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_wk)
    options = {
        'page-size' : 'A4',
        'encoding' : 'UTF-8',
    }
    pdfkit.from_file(htmls, 'crossin_crawler.pdf', configuration=config, options=options)


#主函数
if __name__ == '__main__':
    # htmls = []
    # for i in range(25, 31) :
    #     url = 'https://crossincode.com/vip/homework/%d/' % i
    #     html = get_data(url)
    #     content = html.find('div', class_='panel panel-default').prettify()
    #     title = html.find('div', class_='panel-heading').get_text().strip('\n   ')
    #     htmls.append(title + '.html')
    #     with open('%s.html' % title, 'w', encoding='utf-8') as f:
    #         f.write(content)
    #         time.sleep(10)
    htmls = ['爬虫初体验.html', '你最喜欢哪部电影？.html', '开始进一步的抓取.html', '换个方式刷微博.html', '登录后玩玩知乎.html', '从页面能得到什么.html']
    htmltopdf1(htmls)
    # first_page = get_first_page()
    # get_classes(first_page)





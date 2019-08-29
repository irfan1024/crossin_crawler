#!/user/bin/env python
#-*- coding"utf-8 -*-

import requests
import bs4
import csv

#获取详情页信息
def detail(positionURL):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.3',
        "Cookies": 'x-zp-client-id=c6730fd1-7c40-4d2e-ed7e-a7d0cff48a02; sts_deviceid=16cdb48b16aac-0b8b4b45552f84-5f4e2917-1049088-16cdb48b16b1cc; sts_sg=1; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fcrossincode.com%2Fvip%2Fhomework%2F30%2F; jobRiskWarning=true; sajssdk_2015_cross_new_user=1; dywea=95841923.199334794381206560.1567047070.1567047070.1567047070.1; dywec=95841923; dywez=95841923.1567047070.1.1.dywecsr=crossincode.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/vip/homework/30/; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1567047070; __utma=269921210.791573902.1567047071.1567047071.1567047071.1; __utmc=269921210; __utmz=269921210.1567047071.1.1.utmcsr=crossincode.com|utmccn=(referral)|utmcmd=referral|utmcct=/vip/homework/30/; sou_experiment=unexperiment; LastCity=%E9%82%AF%E9%83%B8; LastCity%5Fid=568; ZP_OLD_FLAG=false; CANCELALL=0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216cdb48b1cd300-069b5ecc49e8a8-5f4e2917-1049088-16cdb48b1ce3e6%22%2C%22%24device_id%22%3A%2216cdb48b1cd300-069b5ecc49e8a8-5f4e2917-1049088-16cdb48b1ce3e6%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; acw_tc=2760822815670558401974820e7148a33af5df678ff295a099741ef44c3a54; sts_sid=16cdd82d0d3b6-0f6596d359d8d5-5f4e2917-1049088-16cdd82d0d4106; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%227663855e-0d8d-4d8d-868a-52ad14d08199-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22jobs%22:{%22funczoneShare%22:%22dtl_best_for_you%22%2C%22recommandActionidShare%22:%2247fd2a3b-01ea-4d67-b873-89a63427f2eb-job%22}%2C%22company%22:{%22actionid%22:%2282b66e76-b71f-4c2b-bc00-50cf2bc63403-company%22%2C%22funczone%22:%22hiring_jd%22}}; sts_evtseq=10; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1567086500'
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
        "Cookies": 'x-zp-client-id=c6730fd1-7c40-4d2e-ed7e-a7d0cff48a02; sts_deviceid=16cdb48b16aac-0b8b4b45552f84-5f4e2917-1049088-16cdb48b16b1cc; sts_sg=1; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fcrossincode.com%2Fvip%2Fhomework%2F30%2F; jobRiskWarning=true; sajssdk_2015_cross_new_user=1; dywea=95841923.199334794381206560.1567047070.1567047070.1567047070.1; dywec=95841923; dywez=95841923.1567047070.1.1.dywecsr=crossincode.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/vip/homework/30/; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1567047070; __utma=269921210.791573902.1567047071.1567047071.1567047071.1; __utmc=269921210; __utmz=269921210.1567047071.1.1.utmcsr=crossincode.com|utmccn=(referral)|utmcmd=referral|utmcct=/vip/homework/30/; acw_tc=276082a815670546718661742e20cc31360aeb74c3f6aa6cc931b8bc347d75; sou_experiment=unexperiment; LastCity=%E9%82%AF%E9%83%B8; LastCity%5Fid=568; ZP_OLD_FLAG=false; CANCELALL=0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216cdb48b1cd300-069b5ecc49e8a8-5f4e2917-1049088-16cdb48b1ce3e6%22%2C%22%24device_id%22%3A%2216cdb48b1cd300-069b5ecc49e8a8-5f4e2917-1049088-16cdb48b1ce3e6%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; sts_sid=16cdd82d0d3b6-0f6596d359d8d5-5f4e2917-1049088-16cdd82d0d4106; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22c0a87e8a-c6e6-4f42-87ce-9e66049c5db1-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22jobs%22:{%22funczoneShare%22:%22dtl_best_for_you%22%2C%22recommandActionidShare%22:%2247fd2a3b-01ea-4d67-b873-89a63427f2eb-job%22}%2C%22company%22:{%22actionid%22:%2282b66e76-b71f-4c2b-bc00-50cf2bc63403-company%22%2C%22funczone%22:%22hiring_jd%22}}; sts_evtseq=8; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1567086434'
    }
    try:
        req = requests.session().get(url, headers=headers)
        html = req.json()
    except:
        print('获取数据错误')
        html = { 'code' : 000}
    datas(html)



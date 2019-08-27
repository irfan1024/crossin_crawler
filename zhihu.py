import requests
import csv

#将数据写入 csv 文件
def file_w(rows):
    with open('zhihu.csv', 'w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(rows)



#获取知乎时间线上的问题的函数
def zhihu(url, headers):
    req = requests.session().get(url, headers=headers)
    dict_json = req.json()
    datas = dict_json['data']
    rows = []

    for data in datas:
        type = data['target']['type']
        if type == 'article':
            header = ['id', '标题', '赞', '作者', '评论数']
            id = data['target']['id']
            title = data['target']['title']
            voteup_count = data['target']['voteup_count']
            author = data['target']['author']['name']
            comment_count = data['target']['comment_count']
            row = (id, title, voteup_count, author, comment_count)

        elif type == 'answer':
            id = data['target']['id']
            action_text = data['action_text']
            voteup_count = data['target']['voteup_count']
            thanks_count =data['target']['thanks_count']
            comment_count = data['target']['comment_count']
            question = data['target']['question']['title']
            author = data['target']['question']['author']['name']
            answer_count = data['target']['question']['answer_count']
            follower_count = data['target']['question']['follower_count']
            row = (id, action_text, voteup_count, thanks_count, comment_count, question, author, answer_count, follower_count)
            header = ['id', '标签', '赞', '感谢', '反对', '问题', '提问者', '回答数', '关注数']
        else:
            continue
        rows.append(header)
        rows.append(row)
    file_w(rows)


if __name__ == '__main__':
    #url, headers
    url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
    cookies = '_zap=9d702648-1c02-4d51-8a5f-ba5be53c05d7; _xsrf=c0347064-31c6-4a06-9175-dc0acc647bb7; d_c0="AABhptIh8Q-PTtc6uV1qBbPWkPhI_E5coZk=|1566660140"; capsion_ticket="2|1:0|10:1566780547|14:capsion_ticket|44:ZWZkMjhmMDA4ZGJjNGE2OGE2ZDVkNWJmNjFhZWRjOTU=|1de7c7f5ce5fba7ad373bba5255017c3df389bbede623a1d8c46f9fbdb0604a3"; z_c0="2|1:0|10:1566780551|4:z_c0|92:Mi4xODVBVEFBQUFBQUFBQUdHbTBpSHhEeVlBQUFCZ0FsVk5obnBRWGdENU5WRW9WQ1pKVTVLOG1nU2YxRk9nX2VhaTZB|6a93da3335d2400f5806be5481658a427adf9f4f7e58c0812807da549dea4990"; q_c1=7cee8b00ac7f440eb8030707e630ea45|1566783010000|1566783010000; tshl=; tst=r; tgw_l7_route=73af20938a97f63d9b695ad561c4c10c'

    headers = {
        "User-Agent": user_agent,
        'Cookie': cookies,
    }
    zhihu(url, headers)

#
#
# import os
# import csv
# import requests
# from http import HTTPStatus
#
# class ZhihuRecommend:
#     URL = "https://www.zhihu.com/api/v3/feed/topstory/recommend"
#
#     def __init__(self, url=URL):
#         self.url = url
#         self.web = requests.session()
#
#     def get_page_data(self):
#         headers = {
#                 'cookie': '_zap=43eaded6-a732-4ee7-85b4-c7ac8c2614c5; d_c0="ABDnkMYHMQ-PTui_mptmfL3t4WcTSx9KIug=|1553768410"; _xsrf=Zgy0cAoMKmR8LXorsOrwWH9688apvRiV; z_c0="2|1:0|10:1554286165|4:z_c0|92:Mi4xOGdxRUFnQUFBQUFBRU9lUXhnY3hEeVlBQUFCZ0FsVk5WZFNSWFFBMTBWX1F5Q1gyUHl5dF9KM0J2Z0Vhc01udzdR|3e8f2f8fa63645be91387e6b259b8dfdc6dd278f9c99a010b500b2c860a1e49b"; q_c1=77ff3c79cc414cd6980fc4df6367c896|1563535619000|1556448479000; tst=r; __utma=51854390.1825543909.1565075465.1565075465.1565075465.1; __utmz=51854390.1565075465.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/napoleon-lee/collections; __utmv=51854390.100-1|2=registration_date=20160124=1^3=entry_date=20160124=1; tgw_l7_route=66cb11',
#                 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
#                 }
#         params = {
#                 'session_token': 'b3b8777f76c7d1d0e2717ddca35d9aae',
#                 'desktop': 'true',
#                 'page_number': 2,
#                 'limit': 6,
#                 'action': 'down',
#                 'after_id': 5
#                 }
#         r = self.web.get("{}".format(self.url), headers=headers, params=params)
#         return r.json()
#
#     def save_csv(self):
#         rows = []
#         headers = ["id","type","offset","verb","created_time","updated_time","target","brief","uninterest_reasons",
#                 "attached_info","actors","show_actor_time","action_text","action_text_tpl","action_card"]
#         data = self.get_page_data()
#         for i in range(len(data['data'])):
#             rows.append(data['data'][i])
#         os.makedirs('./zhihu/', exist_ok=True)
#         with open("./zhihu/zhihu.csv", "w") as f:
#             f_csv = csv.DictWriter(f, headers)
#             f_csv.writeheader()
#             f_csv.writerows(rows)
#
#     def run(self):
#         print ("开始获取知乎时间线内容...")
#         self.save_csv()
#         print ("获取完成。")
#
#
# if __name__ == "__main__":
#     zhihu = ZhihuRecommend()
#     zhihu.run()
import requests
import csv

#将数据写入 csv 文件
def file_w(rows):
    with open('zhihu.csv', 'w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(rows)



#获取知乎时间线上的问题的函数
def zhihu(url, headers):
    try:
        req = requests.session().get(url, headers=headers)
        print('type', type(req))
        dict_json = req.json()
        datas = dict_json['data']
        rows = []
    except:
        print('获取网站数据错误')
        return 0
    for data in datas:
        data_type = data['target']['type']
        if data_type == 'article':
            header = ['id', '标题', '赞', '作者', '评论数']
            id = data['target']['id']
            title = data['target']['title']
            voteup_count = data['target']['voteup_count']
            author = data['target']['author']['name']
            comment_count = data['target']['comment_count']
            row = (id, title, voteup_count, author, comment_count)

        elif data_type == 'answer':
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
            print("未找到数据")
            continue
        rows.append(header)
        rows.append(row)
    try:
        file_w(rows)
    except:
        print("写入文件错误")


#主函数
if __name__ == '__main__':
    #url, headers
    url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
    cookies = '######'
    headers = {
        "User-Agent": user_agent,
        'Cookie': cookies,
    }
    zhihu(url, headers)


import requests
import csv

#批量获取电影海报函数
def image():
    for i in range(0, 40, 20):
        url = ' https://api.douban.com/v2/movie/top250?start=%d&apikey=0df993c66c0c636e29ecbb5344252a4a' % i
        req = requests.get(url)
        json_dict = req.json()
        subjects = json_dict['subjects']
        # 批量获取电影海报
        for subject in subjects:
            image_url = subject['images']['large']
            id = int(subject['id'])
            image = requests.get(image_url)
            with open('./movie_image/%d.jpg' % id, 'wb') as f:
                f.write(image.content)


#批量获取电影数据并保存为 csv 文件函数
def data_csv():
    rows = []
    for i in range(0, 40, 20):
        url = ' https://api.douban.com/v2/movie/top250?start=%d&apikey=0df993c66c0c636e29ecbb5344252a4a' % i
        req = requests.get(url)
        json_dict = req.json()
        subjects = json_dict['subjects']
        # 批量获取电影数据
        for subject in subjects:
            id = subject['id']
            name = subject['title']
            star = subject['rating']['average']
            casts = subject['casts']
            actor = ''
            alt = subject['alt']
            #循环获取演员
            for cast in casts:
                actor += cast['name'] + ', '
            row = (id, name, star, actor, alt)
            rows.append(row)
        #写入 csv 文件
        header = ['id', '电影名称', '评分', '演员', '网址']
        with open('movie.csv', 'w', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(header)
            f_csv.writerows(rows)



#主函数
if __name__ == '__main__':
    data_csv()
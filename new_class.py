#!/user/bin/env python
# -*- coding"utf-8 -*-

import random
import requests

#获取随机数
def get_num():
    url = ' https://python666.cn/cls/number/guess/'
    req = requests.get(url)
    html = req.json()
    return html

#内循环
def inner_loop(game_nums, num0, times):
    game_nums += 1
    while True:
        times += 1
        try:
            print('请输入一个整数')
            num = int(input())
        except:
            print('输入数字错误,请重新输入')
            continue
        if num < num0:
            print('猜小了')
            continue
        elif num > num0:
            print('猜大了')
            continue
        else:
            print('恭喜你,猜对了!')
            print('您一共猜了%d轮' % times)
            return times
#外循环
def external_loop():
    game_data = read_data()
    game_data = handle_data(game_data)
    name = input('请输入用户名..')
    index = output_data(name, game_data)
    print(index,'111111111111')
    if index == 0:
        if game_data[0]:
            data = game_data[index]
            print('!@#')
            game_nums = data['times']
            minitimes = data['mini']
        else:
            print('0000000000000')
            game_nums = 0  # 多少轮
            minitimes = 100  # 最少轮
    elif index == -1:
        index = 0
        game_nums = 0  # 多少轮
        minitimes = 100  # 最少轮
    elif index == -2:
        game_nums = 0#多少轮
        minitimes = 100#最少轮
    else:
        data = game_data[index]
        print('!@#%*&(*&q')
        game_nums = data['times']
        minitimes = data['mini']
    game_begin(index, name,game_nums,minitimes)

#初始化
def game_begin(index, name, game_nums, minitimes):
    index = index
    nums = 0
    totals = []
    while True:
        game_nums += 1
        num0 = get_num()
        times = 0
        times = inner_loop(game_nums, num0, times)
        if times == 0:
            break
        else:
            totals.append(times)
            print('是否继续?y继续,其他任意键结束')
            try:
                a = input()
            except:
                print('请输入正确选项')
                a = input()
            if a == 'y':
                continue
            else:
                break
    for time in totals:
        nums += time
    average =nums / game_nums#平均多少次
    for total in totals:
        if total < minitimes:
            minitimes = total
    print("玩家{},一共玩了了{}次,每次游戏平均{}轮猜中,最快轮数为{}".format(name,game_nums,average,minitimes) )
    print('游戏快乐,欢迎再来!')
    data_show = "玩家{},一共玩了了{}次,每次游戏平均{}轮猜中,最快轮数为{}".format(name,game_nums,average,minitimes) + '\n'
    write_data(index, data_show)

#写入文件函数
def write_data(index, data_show):
    game_data = read_data()
    if index == -2:
        game_data.append(data_show)
        try:
            with open('./game/game.txt', 'a') as f:
                f.writelines(data_show)
        except Exception as i:
            print(i)
            print('写入错误')
    elif index != -2:
        print('data_show', data_show)
        game_data[index] = data_show
        try:
            with open('./game/game.txt', 'w') as f:
                f.writelines(game_data)
        except Exception as i:
            print(i)
            print('写入错误')
    else:
        print("index出错")


#读取文件
def read_data():
    try:
        with open('./game/game.txt', 'r') as f:
            game_data = f.readlines()
    except Exception as e:
        print(e)
        print('读取文件错误')
    return game_data

#游戏数据处理
def handle_data(game_data):
    i = 0
    for data in game_data:
        data = data.split(',')
        dict = {
            'name':data[0][2:],
            'times':int(data[1].split()[0][-2]),
            'average':float(data[2].split()[0][-6:-4]),
            'mini':int(data[3].split()[0][-1]),
        }
        game_data[i] = dict
        i += 1
    return game_data

#用户数据输出
def output_data(name, game_data):
    index = 0
    if game_data == []:
        print('数据库为空')
        index = -1
        return index
    elif game_data != []:
        for data in game_data:
            if name == data['name']:
                print(data)
                game_nums = data['times']
                average = data['average']
                minitimes = data['mini']
                print("玩家{},一共玩了了{}次,每次游戏平均{}轮猜中,最快轮数为{}".format(name, game_nums, average, minitimes))
                return index
            index += 1
        print('没玩过吧?2333')
        #数据库不是空的,但是没有找到
        return -2



if __name__ == '__main__':
    external_loop()

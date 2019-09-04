#!/user/bin/env python
# -*- coding"utf-8 -*-

import random
import pywin32

def inner_loop(num0, times):
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
            break

def external_loop():
    while True:
        num0 = random.randint(1, 10)
        times = 0
        inner_loop(num0, times)
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
    print('游戏快乐,欢迎再来!')
    print(pywin32.GetKeyboardLayoutName())




if __name__ == '__main__':
    external_loop()

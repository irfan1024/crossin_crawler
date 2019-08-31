#!/user/bin/env python
#-*- coding"utf-8 -*-
from pyecharts.charts import Pie
from pyecharts import options as opts
import csv

biaoqian = 0
biaoti = 0

#数据
with open('zhihu.csv') as f:
    reader = csv.reader(f)
    #next()函数用于生成器的 下一步执行!
    reader_now = next(reader)
    #enumerate 用于遍历数据 https://www.runoob.com/python/python-func-enumerate.html
    for index, shuju in enumerate(reader):
        if shuju[1] == '标签':
            biaoqian += 1
        if shuju[1] == "标题":
            biaoti += 1



pie = Pie()
pie.add('知乎首页的专栏和问题量', [('专栏', biaoti), ('问答', biaoqian)])
pie.set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
pie.render()

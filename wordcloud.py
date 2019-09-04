# !/user/bin/env python
# -*- coding"utf-8 -*-
from pyecharts import options as opts
from pyecharts.charts import WordCloud

words = [
    ("小仙女", 10000),
    ("小祖宗", 6181),
    ("莹莹", 4386),
    (" I ", 4055),
    ("LOVE", 2467),
    ("YOU", 2244),
    ("结婚", 1868),
    ("好不好?", 1484),
    ("小宝贝", 1112),
    ("小美女", 865),
    ("女汉子", 847),
    ("女神", 582),
    ("做饭棒棒的", 555),
    ("不生气哈", 550),
    ("还会开车", 462),
    ("咋这么好", 366),
]

wordcloud = WordCloud()
wordcloud.add('词云', words, word_size_range=[20, 100])
wordcloud.set_global_opts(title_opts=opts.TitleOpts(title="wordcloud-基本示例"))
wordcloud.render()







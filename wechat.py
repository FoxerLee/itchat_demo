# -*- coding:utf-8 -*-
import itchat
import re
import jieba

import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

itchat.login()

# 获取好友信息
friends = itchat.get_friends(update=True)[0:]


# part1 计算好友性别比例
male = female = others = 0

for i in friends[1:]:

    sex = i['Sex']

    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        others += 1
# 朋友总数
total = len(friends[1:])

# 好友性别比例
male_ratio = float(male)/total * 100
female_ratio = float(female)/total * 100
others_ratio = float(others)/total * 100

print("男性好友: % 2f%%" % male_ratio + '\n'
      "女性好友: % 2f%%" % female_ratio + '\n'
      "外星生物: % 2f%%" % others_ratio + '\n')


# part2 制作个性签名的自定义词云图
siglist = []
for i in friends:
    # 获取签名，去掉本来是表情，之后变成了emoji, span, class的这些东西
    signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
    # 正则表达式去掉 <>/= 这些符号
    rep = re.compile("if\d+\w*|[<>/=]")
    signature = rep.sub("", signature)
    # 得到的结果存入数组中
    siglist.append(signature)
# 变为字符串
text = "".join(siglist)

# 利用jieba这个库分词
word_list = jieba.cut(text, cut_all=True)
word_space_split = " ".join(word_list)

coloring = np.array(Image.open("/Users/liyuan/Downloads/壁纸/sign.JPG"))
my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=coloring,
                         max_font_size=60, random_state=42, scale=2,
                         font_path="/Library/Fonts/Songti.ttc").generate(word_space_split)

image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

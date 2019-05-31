# _*_coding:utf-8_*_

num_words = []
with open('e:/豆瓣', mode='r', encoding='utf-8') as f:
    for line in f.readlines():
        counter = len(line.split('\t')[2])
        num_words.append(counter)
print("文本统计完成。")

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'
# %matplotlib inline
plt.hist(num_words, 200, facecolor='g')
plt.xlabel('text length')
plt.ylabel('frequent number')
plt.axis([0, 400, 0, 20000])
plt.show()


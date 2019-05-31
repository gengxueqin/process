#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyhanlp import *
import jieba.posseg as pseg

'''
for i in range(0,10):
    text=open('e:/data/yingyan/newtext/%d.txt' % i, 'r', encoding='utf-8').read()
    phrase_list = HanLP.extractPhrase(text, 100)
    print(phrase_list)
    f = open('e:/data/yingyan/new_phrase/res-%d.txt' % i, 'w')
    f.write(str(phrase_list))
    f.write('\r\n')
    f.close()
'''
def handel_data():
    #读取要处理的微博正文提取名词，去除停用词
    fp = open('e:/相似度/title.txt', 'r',encoding='utf8')
    w = []
    s = []
    for line in fp.readlines():    # 按行处理
        line = line.strip()
        seg_lines = pseg.cut(line)  # 分词标注
        for seg_line in seg_lines:   # 判断如果是名词则保留

           #if seg_line.flag == 'v' or seg_line.flag == 'nr' or seg_line.flag == 'ns' or seg_line.flag == 'nt' or seg_line.flag == 'nz':

            w.append(seg_line.word)
    return w

w=handel_data()
print(w)


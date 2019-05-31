#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
根据词性进行相似句子合并
结巴词性表：
n名词
nr人名
ns地名
nt机构团体
nz其他专名
v动词
vd副动词
vn名动词

'''
import os
import jieba
import jieba.posseg as pseg


fw = open('./data10-12_seg','w',encoding='utf8')

fn = open('./data10-12','r',encoding='utf8') # 打开文件
string_data = fn.readlines() # 读出整个文件
stop = [line.strip() for line in open('f:/stopwords/stopwords.txt','r',encoding='utf8',errors='ignore').readlines()]

for l in string_data:
    # 文本分词
    seg_list = jieba.cut(l.split('--')[0]) # 分词
    seg_t=[t for t in seg_list if t not in stop]   # 去停
    fw.write(' '.join(seg_t))
    fw.write('\n')
fw.close()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2.统计含有搜索词的句子的频率，并保存成字典{句子，频率}

import operator

def keyfrq(stop_path,savefrq_path,key_path):

    f = open(stop_path,'r',encoding='gbk')
    fw=open(savefrq_path,'w',encoding='gbk')
    count_dict = {}

    #统计所有句子的频率
    for line in f.readlines():
        line = line.strip()
        count = count_dict.setdefault(line, 0)
        count += 1
        count_dict[line] = count

    # 读取搜索词
    keywords = []
    for line in open(key_path, 'r').readlines():
        keywords.append(line.strip())

    # 统计含关键词的句子频率
    c={}
    for s in keywords:
        for key in count_dict.keys():
            if s in key:
                c.fromkeys(key)
                c[key]=count_dict[key]

    sorted_c = sorted(c.items(), key=operator.itemgetter(1), reverse=True)

    # 保存
    for k,v in sorted_c:
        fw.write('%s'%k+'\n')


#!/usr/bin/env python
# -*- coding: utf-8 -*-

keywords=[]
for line in open('E:/鹰眼/原数据/ynkey.txt', 'r', encoding='gbk').readlines():
    keywords.append(line.strip())

with open('E:/鹰眼/原数据/output_去重.txt', 'r') as f1, open('E:/鹰眼/原数据/output_key.txt', 'w') as f2:
    for line in f1.readlines():
        line = line.strip()
        for k in keywords:
            if k in line:
                f2.write(line + '\n')



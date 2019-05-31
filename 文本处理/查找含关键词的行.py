#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
找出文本中含有关键字的行，并保存。
'''

def findkey(keyfile,infile,outfile):
    keywords=[]
    for line in open(keyfile, 'r', encoding='gbk').readlines():
        keywords.append(line.strip())

    with open(infile, 'r') as f1, open(outfile, 'w') as f2:
        for line in f1.readlines():
            line = line.strip()
            for k in keywords:
                if k in line:
                    f2.write(line + '\n')

import re

list = []
matchPattern = re.compile(r'.+:减肥')
file = open('./test','r')
while 1:
    line = file.readline()
    if not line:
        break
    elif matchPattern.search(line):
        pass
    else:
        list.append(line)
file.close()
file = open('./target', 'w')
for i in list:
    file.write(i)
file.close()

#findkey('E:/鹰眼/ynkey.txt','e:/鹰眼/nn_stop.txt', 'e:/鹰眼/nn_k.txt')
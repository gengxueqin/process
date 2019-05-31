#!/usr/bin/env python
# -*- coding: utf-8 -*-

f=open('e:/台湾选举/11/hyy_ksentence.txt','r',encoding='utf8').readlines()
fw1=open('e:/台湾选举/11/hyy_len1.txt','w',encoding='utf8')
fw2=open('e:/台湾选举/11/hyy_len2.txt','w',encoding='utf8')
for line in f:
    if(len(line.strip())>=6 and len(line.strip())<=10):
        fw1.write(line.strip()+'\n')
    else:
        fw2.write(line.strip()+'\n')

fw1.close()
fw2.close()
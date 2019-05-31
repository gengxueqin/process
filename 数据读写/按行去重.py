#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quchong(infile, outfile):
    infopen = open(infile, 'r',encoding='utf-8')
    outopen = open(outfile, 'w',encoding='utf-8')
    lines = infopen.readlines()
    list_1 = []
    for line in lines:
        if line not in list_1:
            list_1.append(line)
            outopen.write(line)
    infopen.close()
    outopen.close()

quchong("e:/豆瓣", "e:/豆瓣_qc")
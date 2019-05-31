#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd
import os

# 打开文件，读取列数据
name='movie_comment20'
data = xlrd.open_workbook("e:/csv_data/%s.csv"%name)
table = data.sheets()[0] # 表头
nrows = table.nrows  # 行数
ncols = table.ncols  # 列数
colnames = table.col_values(2)[0:] # 列，下标从0开始
fw=open('e:/%s'%name,'a',encoding='utf8')
for l in colnames:
    fw.write(l.strip()+'\n')


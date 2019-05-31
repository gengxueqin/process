#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 读取文件
fn = open('e:/科创/合并','r',encoding='utf8') # 打开文件
string_data = fn.read() # 读出整个文件
fn.close() # 关闭文件
print(string_data)
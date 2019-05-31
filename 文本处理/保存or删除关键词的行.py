#!/usr/bin/env python
# -*- coding: utf-8 -*_

import re
list = []
de = []
matchPattern = re.compile(r'.+:开始|减肥|瘦了|健身|运动|瘦身|瑜伽|瘦腿|瘦腰|跑步|暴瘦|塑形|体重|减脂|健美|呼啦圈|仰卧起坐')
f = open('./data10-12','r',encoding='utf8')
while 1:
    line = f.readline()
    if not line:
        break
    elif matchPattern.search(line):
        de.append(line)
    else:
        list.append(line)
f.close()

file1 = open('./data/去除减肥', 'w',encoding='utf8')
file2 = open('./data/减肥', 'w',encoding='utf8')

for i in list:
    file1.write(i)
file1.close()

for i in de:
    file2.write(i)
file2.close()


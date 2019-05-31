#!/usr/bin/env python
#coding:utf-8

import random
import time

def test(n):
    start = time.clock()

    f = open("1.txt", "r", encoding='utf-8')
    fw = open("train.txt", "w", encoding='utf-8')  # 保存随机抽取的n行文本
    fw2 = open("test.txt", "w", encoding='utf-8')   # 保存剩余的文本
    raw_list = f.readlines()
    random.shuffle(raw_list)

    for i in range(0, n+1):
        fw.writelines(raw_list[i])

    for j in range(n+1, len(raw_list)):
        fw2.writelines(raw_list[j])

    end = time.clock()
    print("cost time is %fs." % (end - start))


def test2():

    f = open("url.txt", "r", encoding='utf-8')
    fw = open("url_random.txt", "w", encoding='utf-8')  # 保存随机抽取的n行文本
    raw_list = f.readlines()
    random.shuffle(raw_list)

    for i in range(len(raw_list)):
        fw.write(raw_list[i])

test2()






















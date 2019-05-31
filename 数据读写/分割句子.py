#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyltp import SentenceSplitter

def sentence_splitter(data_path,sentence_path):
    f=open(data_path,'r').readlines()
    fw=open(sentence_path,'w')
    for sentence in f:
        #sentence = '你好，你觉得这个例子从哪里来的？当然还是直接复制官方文档，然后改了下这里得到的。'
        sents = SentenceSplitter.split(sentence)  # 分句
        #print('\n'.join(sents))
        fw.write('\n'.join(sents))

sentence_splitter('e:/鹰眼/data/keytxt.txt','e:/鹰眼/data/sentence.txt')
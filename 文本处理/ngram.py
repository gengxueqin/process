#分词不去停的语料，分出共现词及共现次数     n-gram

from __future__ import print_function

import logging
import os
import re
from collections import defaultdict
from time import time
from six.moves import range
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.text import TfidfVectorizer

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)




data = []
for i in range(1,501):
    f = open('e:/data/yingyan/ngram/%d.txt' % i, 'w')  #保存提取出来的共现词
    for line in open('e:/data/yingyan/new_txt_seg/%d.txt'%i,'r',encoding='gbk').readlines():
        data.append(line.strip())
        data.append('\n')

    vec =TfidfVectorizer(min_df=1, ngram_range=(4,4))       #提取共现词
    # ngram_range=(1,1) 表示 unigram, ngram_range=(2,2) 表示 bigram, ngram_range=(3,3) 表示 thirgram

    fre = vec.fit_transform(data) # 文本转化成词对应的频数矩阵
    print(fre.shape)       #词频矩阵的大小
    word=vec.get_feature_names() # 得到共现词
    weight=fre.toarray()   #得到词对应的频数
    f.write(str(word))
    f.close()



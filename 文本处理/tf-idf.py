import time
import codecs
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

'''
sklearn里面的TF-IDF主要用到了两个函数：CountVectorizer()和TfidfTransformer()。
    CountVectorizer是通过fit_transform函数将文本中的词语转换为词频矩阵。
    矩阵元素weight[i][j] 表示j词在第i个文本下的词频，即各个词语出现的次数。
    通过get_feature_names()可看到所有文本的关键字，通过toarray()可看到词频矩阵的结果。
    TfidfTransformer也有个fit_transform函数，它的作用是计算tf-idf值。
'''

if __name__ == "__main__":
    corpus = []  # 文档预料 空格连接

    # 读取语料 一行为一个文档
    for line in open('e:/data/yingyan/txt.txt', 'r',encoding='utf-8').readlines():
        #print(line)
        corpus.append(line.strip())
    # print corpus
    #time.sleep(5)

    # 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer = CountVectorizer()

    # 该类会统计每个词语的tf-idf权值
    transformer = TfidfTransformer()

    # 第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))

    # 获取词袋模型中的所有词语
    word = vectorizer.get_feature_names()
    #print(len(word))  #80717
    # 将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
    weight = tfidf.toarray()

#####################以字典格式<key:word,value:tf-idf>保存到文件############################
    c = dict.fromkeys(word)  # <key:word,value:tf-idf>
    f = open('e:/data/cluster_tfidf.txt', 'w')
    #打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    for i in range(len(weight)):
        for j in range(len(word)):
            if weight[i][j] > 0:  # 保存tfidf值大于0的关键词
                # print(word[j],weight[i][j])
                c[word[j]]=weight[i][j]


    #按tf-idf值排序
    c = dict(sorted(c.items(), key=lambda x: x[1], reverse=True))

    # 取出最大的前n个
    cnt = 0
    for key, value in c.items():
        cnt += 1
        if cnt > 1000:
            break
        # print("{}:{}".format(key, value))
        f.write("{}:{}".format(key, value) + ' ')
    f.close()
'''或者直接
c = sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))[:50]   排序并取得前50个值最大的键值对
'''


'''
    # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    for i in range(len(weight)):
        print(u"-------这里输出第", i, u"个文本的词语tf-idf权重------")
        for j in range(len(word)):
            result.write(str(weight[i][j]) + ' ')
        result.write('\r\n\r\n')

    result.close()


  #####################保存tf-idf值大于0的词############################
  # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    result = codecs.open('e:/data/yingyan/keywords.txt', 'w', 'utf-8')
    for i in range(len(weight)):
        for j in range(len(word)):
            if weight[i][j]>0:   #保存tfidf值大于0的关键词
                #print(word[j],weight[i][j])
                result.write(word[j]+' ')
        result.write('\r\n\r\n')
    result.close()
    
    
    #####################以字典格式<key:word,value:tf-idf>保存到文件############################
    c = dict.fromkeys(word)  # <key:word,value:tf-idf>
    f = open('e:/data/yingyan/dict.txt', 'w')

    #打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    for i in range(len(weight)):
        for j in range(len(word)):
            if weight[i][j] > 0:  # 保存tfidf值大于0的关键词
                # print(word[j],weight[i][j])
                c[word[j]]=weight[i][j]

    #按value排序
    c=sorted(c.items(), key=lambda x: x[1], reverse=True)
    s=str(c)
    f.write(s+' ')
    f.close()
'''
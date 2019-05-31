
# 1.删除文本中含有某些字符串的行

def delstop(triple_path,save_path):
    f = open(triple_path, 'r',encoding='gbk')
    fw = open(save_path, 'w',encoding='gbk')
    # 读取停用词
    stopwords = []
    for line in open('e:/鹰眼/data/stopwords.txt', 'r').readlines():
        stopwords.append(line.strip())

    for value in f.readlines():
        flag = True
        for i in stopwords:
            if i in value:
                flag = False
                break
        if flag is True:
            fw.write('%s' % value)
    fw.close()
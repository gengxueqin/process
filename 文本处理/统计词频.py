
# python 3.4.3
# 功能：统计文本中的词频。
# 缺陷：标点符号的频数也会计算在内。

with open('E:/分词/已分词/txt1_seg/2.txt', 'r', encoding='utf-8') as inFile:
    dict = {}      # 创建一个空字典
    word = ''      # 空字符串以便于连接字符
    for char in inFile.read():
        if char != ' ':
                word += char   # 连接字符
        else:
            if word in dict:
                dict[word]+=1
                word=''        # 将word置为空，否则，word值无限增大
            else:
                dict.setdefault(word, 1)
                word=''
    #with open('e:/data/自动推送/count/%d.txt'%i, mode='w', encoding='utf-8') as outFile:
count=0
for word, freq in dict.items():
    if freq > 0:
        count += 1
print(count)
            #s = '{0}:{1}\t'.format(word, freq)
            #outFile.write(s)
    #outFile.close()


    # 然后合并即可
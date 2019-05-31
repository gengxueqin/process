#-*-coding:utf-8-*-

#计算分词后的文本的不同词的个数
contents = open("E:/分词/已分词/txt1_seg/2.txt","r",encoding='utf8').read()
#mylen = len(contents)
#line_num = contents.count("\n")
words_num = len(set(contents.split()))
#print("字符数：%s,\n行数:%s,\n单词数量%s"%(mylen,line_num,words_num))
print(words_num)
#!/usr/bin/env python
# _*_ coding:utf-8 _*_



#将xml文件转换成中文txt  这里选用sogou数据
import codecs
f = codecs.open('e:/data/sogou/news_xml.dat', 'rb', 'mbcs')
text = f.read().encode('utf-8')
f.close()
f = open('e:/data/sogou/news_utf8.txt','wb')
f.write(text)
f.close()     #转换成utf-8编码
# text.decode('utf-8').encode('gbk',errors='ignore')  #转换成gbk编码


#中文显示文本前几行
import codecs
f = codecs.open('e:/data/sogou/news_utf8.txt',encoding='gbk',errors='ignore')
for i in range(7):
    print(f.readline().strip())

#查看文本后几行
with open("e:/data/sogou/news_utf8.txt",encoding='utf-8') as f:
    txt=f.readlines()
keys=[k for k in range(0,len(txt))]
result={k:v for k,v in zip(keys,txt[::-1])}
for i in range(10):
    print (result[i])

#在文本行首添加<root>, 并保存到文件11中
fp=open("e:/data/12/080806.txt",encoding='utf-8')
str=fp.read()
str="<root>\n"+str
fp.close()
fp=open("e:/ndata/SogouCS/080806.txt","w",encoding="utf-8")  #保存更改后的文本到新的文件
fp.write(str)
fp.close()
#行尾加</root>
f = open('e:/ndata/SogouCS/080806.txt','a')
f.write('</root>')
f.close()

#查看文件编码
import chardet
path='userdict.txt'
f=open(path,'rb')
data=f.read()
print(chardet.detect(data))


#查看jieba分词结果
import jieba
data1=jieba.cut('最近新出的iPhone照像功能美美哒')
print (data1)
print (','.join(data1))

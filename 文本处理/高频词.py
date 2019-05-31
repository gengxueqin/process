#高频词
import jieba.analyse
f=open('E:/科创_seg/合并','r',encoding='utf8').read()
result=jieba.analyse.extract_tags(f,50)
print(result)




import jieba
import re

def read_data(path):
    f = open(path, 'r', encoding='utf8')
    data = []
    for line in f.readlines():
        line = re.sub('[a-zA-Z]+','',line)
        text = line.strip().split('\t')
        if len(text) == 3 and text[1] == '好评':
            data.append('好评'+'\t'+text[2])
        if len(text) == 3 and text[1] == '差评':
            data.append('差评'+'\t'+text[2])
    return data

def cut_data(data):
    stopwords = [line.strip() for line in open('f:/stopwords/3.txt', 'r').readlines()]
    for s in data:
        seg = jieba.cut(s.split('\t')[1])
        seg_t=[t for t in seg if t not in stopwords]   # 去停
        l = " ".join(seg_t)
        f.write(s.split('\t')[0]+'\t'+l+'\n')


#f1=open('e:/train.txt','w',encoding='utf8')
f=open('e:/影评数据/hb-val.txt','w',encoding='utf8')
p = read_data('e:/影评数据/hb-val')
cut_data(p)



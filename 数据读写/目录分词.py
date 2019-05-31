
#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import jieba
import os

#读取原始语料库
def savefile(savepath,content):
    with open(savepath,"w",encoding='utf8') as fp:
        fp.write(content)

def readfile(path):
    with open(path,"r",encoding='utf8') as fp:
        content=fp.read()
    return content


#给语料库一份一份地分词、去停止词
def corpus_seg(corpus_path,seg_path):
    catelist=os.listdir(corpus_path)
    for mydir in catelist:
        class_path=corpus_path+mydir+"/"
        seg_dir=seg_path+mydir+"/"

        if not os.path.exists(seg_dir):
            os.makedirs(seg_dir)
        #stop = [line.strip() for line in open('e:/data/stopwords/stopwords.txt').readlines()]
        file_list = os.listdir(class_path)
        for file_path in file_list:
            fullname = class_path+file_path
            content = readfile(fullname)

            content=content.replace("\r\n", "")
            content=content.replace(" ", "")
            content_seg=jieba.cut(content)
            content = filter(str.isalnum, content_seg)  # 过滤掉标点符号
            data = " ".join(content)
            savefile(seg_dir+file_path,data)
    print("中文语料库分词结束！！！")


if __name__ == "__main__":
    corpus_path = "E:/ee/分词/"    # 将文本放入文件夹1
    seg_path = "E:/ee/seg/"
    corpus_seg(corpus_path, seg_path)


#coding=utf-8
'''''
Created on 2015年8月15日
统计一篇文章各个单词出现的词频，并按单次的词频从大到小输出
@author: minmin
'''
import re
import collections

''''' 
从文件中读取内容，统计词频 
'''
def count_word(path):
    result = {}
    with open(path,'r',encoding='utf8') as file_obj:
        all_the_text = file_obj.read()

        for word in all_the_text.split():
            if word not in result:
                result[word] = 0
            result[word] += 1

        return result


''''' 
以词频倒序 
'''
def sort_by_count(d):
    #字典排序
    d = collections.OrderedDict(sorted(d.items(), key = lambda t: -t[1]))
    return d

if __name__ == '__main__':
    file_name = "e:/科创_seg/科创"
    fw=open("e:/科创_seg/keywords",'w',encoding='utf8')

    dword = count_word(file_name)
    dword = sort_by_count(dword)

    for key,value in dword.items():
        #print (key + ":%d" % value)
        fw.write('%s: %d'%(key,value)+'\n')

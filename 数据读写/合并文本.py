#合并多个文本到一个文本
import os
def merge_txt():
    filelist=os.listdir('E:/科创/1/')
    newfile=open('E:/科创/合并','w',encoding='utf8')
    for filename in filelist:
        filepath='E:/科创/1/'+'\\'+filename
        for txt in open(filepath,'r',encoding='utf8'):
            newfile.write(txt.strip())
        newfile.write('\n')
    newfile.close()

merge_txt()
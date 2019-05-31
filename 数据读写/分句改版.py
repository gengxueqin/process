#title、content分句处理
#按行读取txt文件
import re

def sentence_splitter(infile,outfile):
    s = []
    f  = open(infile,'r',encoding='gbk')
    for lines in f:
        str1=str(lines)
        ls1=re.sub(r'\ | |；|_|:|！|？|：|——|--|\丨|，|；| ','。',str1)
        ls =ls1.strip('\n').split('。')
        for i in ls:
            s.append(i)
    f.close()
    #print(s)
#逐行写入txt
    f1 = open(outfile,'w',encoding='utf-8')
    for j in s:
        f1.write(j+'\n')
    f1.close()

def delblankline(in_file, out_file):
    infp = open(in_file, "r",encoding='gbk')
    outfp = open(out_file, "w",encoding='gbk')
    lines = infp.readlines()
    for li in lines:
        if li.split():
            outfp.writelines(li)
    infp.close()
    outfp.close()

def clearBlankLine(f1,f2):
    file1 = open(f1, 'r', encoding='utf-8') # 要去掉空行的文件
    file2 = open(f2, 'w', encoding='utf-8') # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()


if __name__ == '__main__':
    infile="e:/舆情/yq3.txt"
    #in_file="G:/data/yuqin201809/sheet2/content/content11.txt"
    #f1=''

    outfile='e:/舆情/data/sentence_gy.txt'
    #out_file="G:/data/yuqin201809/sheet2/content/content12.txt"
    #f2=''
    sentence_splitter(infile,outfile)
    #delblankline(in_file, out_file)
    #clearBlankLine(f1,f2)


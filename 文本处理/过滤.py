import jieba.posseg as pseg
import re
fp = open("E:/data/鹰眼/500-1000_seg.txt", 'r', encoding='utf-8')
f=open('e:/data/过滤实体词.txt', 'w', encoding='utf-8')
for line in fp.readlines():  # 按行处理
    contents = []
    line = line.strip()

    #line=re.sub('(http[s]?://]|www.)([a-z]|[A-Z]|[0-9]|[/.]|[~])*', '', line.replace('\n', ''))  # 过滤网址
    line=re.sub('[^\w\u4e00-\u9fff]+', '',line.replace('\n',''))    #过滤非中英文字符
    line = re.sub('[A-Za-z]+', '', line.replace('/n', '')) #过滤字母
    line = re.sub('[0-9]*[0-9]+', '', line.replace('\n', ''))  # 过滤数字

    seg_lines = pseg.cut(line)  # 分词标注
    for seg_line in seg_lines:  # 判断如果是名词则保留
       if not (seg_line.flag == 'nr' or seg_line.flag == 'ns' or seg_line.flag == 'nz'):
            contents.append(seg_line.word)  # 保留名词

    for w in contents:

        f.write(w+' ')

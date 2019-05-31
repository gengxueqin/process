#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2.统计含有搜索词的句子的频率，并保存成字典{句子，频率}
import operator

def frq():
    f = open("e:/鹰眼/output_去停.txt",'r')
    fw=open("e:/鹰眼/output_frq.txt",'w')
    count_dict = {}

#统计所有句子的频率
    for line in f.readlines():
        line = line.strip()
        count = count_dict.setdefault(line, -1)
        count += 1
        count_dict[line] = count

    sorted_c = sorted(count_dict.items(), key=operator.itemgetter(1), reverse=True)

    # 保存
    for k,v in sorted_c:
        if v>=6:
            fw.write('%s %d'%(k,v)+'\n')
    f.close()
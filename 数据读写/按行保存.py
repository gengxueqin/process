
# 1.将txt文件的每一行作为一个文本保存
import time
start = time.clock()

file = open("e:/舆情/4.txt", "r", encoding='utf-8')

for num, value in enumerate(file, 1):
    # print("第%s行的内容是：%s" %(num,value))
    f = open("e:/舆情/4/%s.txt" % num, "w", encoding='utf-8')
    f.write('%s' % value.strip())
    f.close()

end = time.clock()

print("cost time is %fs" % (end - start))
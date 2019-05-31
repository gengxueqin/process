
import glob
import time

csvx_list = glob.glob('e:/data/*.csv')
print('总共发现%s个CSV文件' % len(csvx_list))
time.sleep(2)
print('正在处理............')
for i in csvx_list:
    fr = open(i, 'r',encoding='utf-8').read()
    with open('e:/combine1.csv', 'a', encoding='utf-8') as f:
        f.write(fr)
    print('写入成功！')
print('写入完毕！')
print('5秒钟自动关闭程序！')
time.sleep(5)

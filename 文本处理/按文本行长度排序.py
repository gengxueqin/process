myList = []
fw=open('e:/舆情/fp_sort.txt','w')

for line in open('e:/舆情/fp_frq.txt','r'):
    myList.append(line.strip())

myList.sort(key = lambda i:len(i),reverse=True)
print(myList)
for line in myList:
    print(line)
    fw.write(line+'\n')
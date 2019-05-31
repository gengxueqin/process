

a = {'季青林':2,'冯思越':"很帅","汪磊":"chun","完善":520,"大量":"你是三八"}


f=open('e:/data/key0.txt','w')

for k in a.keys():
    print(k)
    f.write(k)
    f.write('\n')
f.close()





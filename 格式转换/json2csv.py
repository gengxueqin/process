import os
import csv
import json

def trans(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        #print(child[13:-5])
        jsonData = open(child[0:-5]+'.json', 'r',encoding='utf8')
        csvfile = open('e:/csv_data/'+child[13:-5]+'.csv', 'w', newline='',encoding='utf8') # python3下
        data = {}
        keys_write = True
        writer = csv.writer(csvfile)

        for line in jsonData:#获取属性列表
            dic=json.loads(line[0:-1])
            keys=dic.keys()
            #print(dic)
            for key in keys:
                if key in dic.keys():
                    data[key] = dic[key]
                else:
                    data[key] = ""
            #print(data)

            if keys_write == True:
                writer.writerow(data.keys())
            writer.writerow(data.values())
            keys_write = False

        jsonData.close()
        csvfile.close()

trans("e:/case_data/")

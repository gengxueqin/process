import pandas as pd
import os
def csv_to_xlsx_pd():
    filelist=os.listdir('E:/csv_data/')
    for filename in filelist:
        filepath='E:/csv_data/'+'\\'+filename
        csv = pd.read_csv(filepath, encoding='utf-8')
        csv.to_excel('e:/xls_data/'+filename.split('.')[0]+'.xls', sheet_name='data',startcol=0)

if __name__ == '__main__':
    csv_to_xlsx_pd()

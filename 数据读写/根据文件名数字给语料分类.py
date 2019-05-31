#1.按评分将语料库分成5类

import os, shutil, collections

counter_dict = collections.defaultdict(int)

#创建字典 存放语料库
src_dir = {'train': './train', 'test': './test'}

try:
  for i in range(1, 6):
      os.mkdir(f'./{i}_train')
      os.mkdir(f'./{i}_test')

except OSError:
        pass

for tag, folder in src_dir.items():
    for file in os.listdir(folder):
        score = round(float(file.split('.txt')[0].split('_')[-1]))   # 提出文本的情感分数，round取整
        counter_dict[f'{score}_{tag}'] += 1
        shutil.copy2(f'{folder}/{file}', f'./{score}_{tag}/{file}')  # 将文件1按照分值1-5复制到文件2

# defaultdict(<class 'int'>,
# {'2_train': 3019, '1_train': 2981, '5_train': 6000, '4_test': 1500, '2_test': 2000, '5_test': 500})
print(counter_dict)

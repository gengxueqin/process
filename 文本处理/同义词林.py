def get_sym(w, word_set):
    # w:  input word
    # word_set: 同义词词集或相关词词集
    results = []
    if(len(w)==1):
        for each in word_set:
            for word in each:
                if w == word:
                    results.append(each)
                    break
    else:
        for each in word_set:
            for word in each:
                if w in word:
                    results.append(each)
                    break
    return results

f = open('F:\哈工大同义词词林扩展版\哈工大同义词词林\同义词词林.txt','r')
lines = f.readlines()
sym_words = []
sym_class_words = []
# 从txt中获取词条，构建同义词词集sym_words和相关词词集sym_class_words
for line in lines:
    line = line.replace('\n', '')
    items = line.split(' ')
    index = items[0]
    if (index[-1]=='='):
        sym_words.append(items[1:])
    if (index[-1] == '#'):
        sym_class_words.append(items[1:])
print(sym_words)
print(64*'*')
print(sym_class_words)
while True:
    w = input()
    print('同义词', 66*'*')
    print(get_sym(w, sym_words))
    print('同类词', 66 * '*')
    print(get_sym(w, sym_class_words))



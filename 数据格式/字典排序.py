def count_words(path, n):
    dic = {}
    # 读取预料 一行预料为一个文档
    line=open(path, 'r', encoding='utf-8').read()
    # print(line)
    words=line.split()

    for word in words:
        dic[word] = words.count(word)
    wordslist = sorted(dic.items(), key=lambda kv: (-kv[1], kv[0]))[:n]
    return wordslist


def test_run():
    path='e:/data/yingyan/cluster/res-00000'
    print(count_words(path, 5))


if __name__ == '__main__':
    test_run()
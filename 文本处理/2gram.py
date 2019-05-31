
class NGram(object):

    def __init__(self, n):
        # n is the order of n-gram language model
        self.n = n
        self.unigram = {}
        self.bigram = {}

    # scan a sentence, extract the ngram and update their
    # frequence.
    #
    # @param    sentence    list{str}
    # @return   none
    def scan(self, sentence):
        # file your code here
        for line in sentence:
            self.ngram(line.split())
        # unigram

        if self.n == 2:
            fip = open("e:/data/鹰眼/500-1000_phrase.txt", "w",encoding='utf-8')
            print(sys.stderr, "failed to open data.bi")
            c = sorted(self.bigram.items(), key=lambda kv: (-kv[1], kv[0]))[:100]   #bi-gram的个数

            fip.write(str(c))


    # caluclate the ngram of the words
    # @param    words       list{str}
    # @return   none
    def ngram(self, words):
        # bigram
        if self.n == 2:
            num = 0
            stri = ''
            for i in words:
                num = num + 1
                if num == 1:
                    stri = stri
                stri = stri + i
                if num == 2:
                    if stri not in self.bigram:
                        self.bigram[stri] = 1
                    else:
                        self.bigram[stri] = self.bigram[stri] + 1
                    stri=''
                    num = 0


if __name__ == "__main__":
    import sys

    fip = open("e:/data/鹰眼/500-1000_seg.txt", "r", encoding='utf-8')
    print(sys.stderr, "failed to open input file")
    sentence = []
    for line in fip:
        if len(line.strip()) != 0:
            sentence.append(line.strip())

    bi = NGram(2)

    bi.scan(sentence)


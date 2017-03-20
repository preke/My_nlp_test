# coding= utf-8

import jieba
from jieba import posseg
from jieba import analyse


class separateWords(object):
    def __init__(self):
        self.stopkey = [line.strip().decode('utf-8') for line in open('stopwords.txt').readlines()]
    
    def split_word(self):
        f = open('desc.txt', 'r')
        g = open('splited_v2.txt', 'wb')
        line = f.readline()
        cnt = 0
        while line:
            line_words = posseg.cut(line)
            wordSet = set(self.stopkey)
            _str = ""
            for word, v in line_words:
                if word in wordSet:
                    pass
                else:
                    _str = _str + word.encode('utf-8') + ' '
            
            g.write(_str)
            g.write('\n')
            print cnt
            cnt = cnt + 1
            line = f.readline()

        g.close()
        f.close()


    
    # Got all the words in the corpus
    # vectorizer = CountVectorizer()
    # transformer = TfidfTransformer()

    # tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    # word=vectorizer.get_feature_names()
    # weight=tfidf.toarray()


    # print len(words)
    # for word in words:
    #     g.write(word.encode('utf-8'))
    #     g.write('\n')

    # f.close()
    # g.close()







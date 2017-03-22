#coding=utf-8
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# read data

f = open('splited_v2.txt', 'r')
sentences = []
line = f.readline()
while line:
    if len(line) > 2:
        sen = []
        for word in line.split():
            sen.append(word)
        sentences.append(sen)
    else:
        pass
    line = f.readline()
f.close()
# finish reading data

# train the model
model = gensim.models.Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)
model.save('mymodel_command')
# finish training model
print 'finished'

# ----------------------------------------------------------------------

#coding=utf-8
import numpy as np
import gensim
from gensim import corpora, models, similarities

model = gensim.models.Word2Vec.load('mymodel_command')

class MyCorpus(object):
    def __iter__(self):
        for line in open('splited_v2.txt'): # this is job desc
            if len(line) > 2:
                yield line.split()

def get_tfidf():
    Corp = MyCorpus()
    dictionary = corpora.Dictionary(Corp)
    corpus = [dictionary.doc2bow(text) for text in Corp]  #把所有评论转化为词包（bag of words）
    tfidf = models.TfidfModel(corpus)                     #使用tf-idf 模型得出该评论集的tf-idf 模型
    corpus_tfidf = tfidf[corpus]                          #此处已经计算得出所有评论的tf-idf 值
    return dictionary, corpus_tfidf



dictionary, corpus_tfidf = get_tfidf()
doc = []
cnt = 0
g = open('splited_v2.txt', 'r')
for item in corpus_tfidf:
    a = np.zeros(100)
    for element in item:
        try:
            a = a + model[dictionary[element[0]].encode('utf-8')] * element[1]
        except:
            print dictionary[element[0]].encode('utf-8')
            cnt = cnt + 1
    doc.append(a)
print len(doc)
print str(cnt) + 'bad datas'
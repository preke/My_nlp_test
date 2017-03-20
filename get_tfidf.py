#coding=utf-8
from gensim import corpora, models, similarities

class MyCorpus(object):

    def __iter__(self):
        for line in open('splited_v2.txt'):
            if len(line) > 2:
                yield line.split()


def get_tfidf():
    Corp = MyCorpus()
    dictionary = corpora.Dictionary(Corp)
    corpus = [dictionary.doc2bow(text) for text in Corp] #把所有评论转化为词包（bag of words）
    tfidf = models.TfidfModel(corpus) #使用tf-idf 模型得出该评论集的tf-idf 模型
    corpus_tfidf = tfidf[corpus]  #此处已经计算得出所有评论的tf-idf 值
    g = open('job_description.txt', 'wb')
    for item in corpus_tfidf:
        item.sort(key = lambda x:x[1], cmp=lambda x,y: cmp(float(x), float(y)), reverse = True)
        for element in item[:10]:
            g.write(dictionary[element[0]].encode('utf-8'))
            g.write(' ')
        g.write('\n')
    g.close()
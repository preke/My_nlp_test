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

# declare data
import numpy as np
doc = []
g = open('splited_v2.txt', 'r')
line = g.readline()
while line:
    if len(line) > 2:
        a = np.zeros(100)
        #a.dtype = ('float32')
        for word in line.split():
            try:
                a = a + model[word]
            except:
				#print word
        
        doc.append(a)
    else:
        pass
    line = g.readline()

print len(doc)

# till now we trans all the sentences to 100-d vectors

import os.path
if not os.path.isfile('text8'):
    os.system('wget -c http://mattmahoney.net/dc/text8.zip')
    os.system('unzip text8.zip')

from gensim.models import Word2Vec, KeyedVectors
from gensim.models.word2vec import Text8Corpus

params = {
    'alpha': 0.05,
    'size': 100,
    'window': 5,
    'iter': 5,
    'min_count': 5,
    'sample': 1e-4,
    'sg': 1,
    'hs': 0,
    'negative': 5
}

model = Word2Vec(Text8Corpus('text8'), **params)
print(model)

from gensim.similarities.index import AnnoyIndexer

model.init_sims()
annoy_index = AnnoyIndexer(model, 100)

def GetWords(vector):
	return model.most_similar([vector], topn=5, indexer=annoy_index)


vector = model.wv.syn0norm[0]
GetWords(vector)

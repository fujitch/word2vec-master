# -*- coding: utf-8 -*-

from gensim.models import word2vec
import pickle

sentences = word2vec.Text8Corpus('text/data_neologd.txt')

model = word2vec.Word2Vec(sentences, size=200, min_count=20, window=15, iter=100)

pickle.dump(model, open('word2vec_neologd_iter100.pickle', 'wb'))
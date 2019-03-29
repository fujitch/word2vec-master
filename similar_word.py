# -*- coding: utf-8 -*-

from gensim.models import word2vec
import pickle

try:
    model
except NameError:
    model = pickle.load(open('word2vec_neologd.pickle', 'rb'))

vector = model.wv['10.1%']
out = model.most_similar([ vector ], [], 20)
for a in out:
    print(a)
    
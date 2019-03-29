# -*- coding: utf-8 -*-

from gensim.models import word2vec
import pickle

try:
    model
except NameError:
    model = pickle.load(open('word2vec.pickle', 'rb'))
    
vector1 = model.wv['東京']
vector2 = model.wv['日本']
vector3 = model.wv['イギリス']

vector = vector1 - vector2 + vector3

word = model.most_similar([vector], [], 5)

for a in word:
    print(a)
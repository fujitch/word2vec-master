# -*- coding: utf-8 -*-

import glob
import MeCab

m = MeCab.Tagger(r'-Owakati -d C:\Users\hori\workspace\encoder-decoder-sentence-chainer-master\mecab-ipadic-neologd')
wikis = glob.glob('text/*/*')
for wiki in wikis:
    if wiki.find(".txt") != -1:
        continue
    file = open(wiki, 'rb')
    sentence = file.read().decode('utf-8')
    sentence = m.parse(sentence)
    sentence = sentence.replace('</ doc >', '</ doc > \n')
    sentence = sentence.encode('utf-8')
    fout = open(wiki + '_indention.txt', 'wb')
    fout.write(sentence)
    file.close()
    fout.close()
    print(wiki)

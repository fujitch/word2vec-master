# -*- coding: utf-8 -*-

import glob

all_strings = ""
texts = glob.glob('text/*/*indention.txt')
texts = texts[:520]
for text in texts:
    file = open(text, 'rb')
    sentence = file.read().decode('utf-8')
    all_strings = all_strings + sentence
    file.close()
    print(text)
# all_strings = all_strings.encode('utf-8')
# fout = open('text/data_neologd_indention.txt', 'wb')
fout = open('text/data_neologd_indention_notbyte_2_10.txt', 'w', encoding='utf-8')
fout.write(all_strings)
fout.close()
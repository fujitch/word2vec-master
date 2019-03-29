# -*- coding: utf-8 -*-

import random
import MeCab
from Parser import Parser

class Maker():
    def __init__(self):
        self.year_master = []
        for i in range(1950, 2050):
            self.year_master.append(str(i))
        self.number_master_smaller = []
        for i in range(10):
            self.number_master_smaller.append(str(i))
        self.number_master = []
        for i in range(100):
            self.number_master.append(str(i))
        self.number_master_larger = []
        for i in range(1000):
            self.number_master_larger.append(str(i))
        
    def generate_word_sentence(self, code):
        if code == 1:
            phraseList = []
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['実質', '相対', '実効']))
            wList.append(random.choice(['GDP', '国内総生産']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master_larger))
            wList.append(random.choice(['兆', '億', '万']))
            wList.append(random.choice(['円', 'ドル', 'ユーロ']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "の" + phraseList[1][0] + phraseList[1][1] + "は" + phraseList[2][0] + phraseList[2][1] + phraseList[2][2] + "です。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 2:
            phraseList = []
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['エネルギー', '化石燃料', 'エネルギー資源', '石油', '食料', '石炭', '省エネ', '省エネルギー']))
            wList.append(random.choice(['効率', '生産性']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['PJ']))
            wList.append(random.choice(['/']))
            wList.append(random.choice(['兆', '億', '万']))
            wList.append(random.choice(['円', 'ドル', 'ユーロ']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "の" + phraseList[1][0] + phraseList[1][1] + "は" + phraseList[2][0] + phraseList[2][1] + phraseList[2][2] + phraseList[2][3] + phraseList[2][4] + "です。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 3:
            phraseList = []
            wList = []
            wList.append(random.choice(['実質', '相対', '実効']))
            wList.append(random.choice(['GDP', '国内総生産']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            wList.append(random.choice(['間']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master_larger))
            wList.append(random.choice(['兆', '億', '万']))
            wList.append(random.choice(['円', 'ドル', 'ユーロ']))
            wList.append(random.choice(['増加', '減少', '増大', '急増', '低下', '上昇', '拡大', '下落']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "は" + phraseList[1][0] + phraseList[1][1] + "から" + phraseList[1][2] + phraseList[1][3] + "の" + phraseList[1][4] + "に" + phraseList[2][0] + phraseList[2][1] + phraseList[2][2] + phraseList[2][3] + "しました。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 4:
            phraseList = []
            wList = []
            wList.append(random.choice(['エネルギー', '化石燃料', 'エネルギー資源', '石油', '食料', '石炭', '省エネ', '省エネルギー']))
            wList.append(random.choice(['効率', '生産性']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            wList.append(random.choice(['間']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['PJ', 'km']))
            wList.append(random.choice(['/']))
            wList.append(random.choice(['兆', '億', '万']))
            wList.append(random.choice(['円', 'ドル', 'ユーロ']))
            wList.append(random.choice(['増加', '減少', '増大', '急増', '低下', '上昇', '拡大', '下落']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "は" + phraseList[1][0] + phraseList[1][1] + "から" + phraseList[1][2] + phraseList[1][3] + "の" + phraseList[1][4] + "に" + phraseList[2][0] + phraseList[2][1] + phraseList[2][2] + phraseList[2][3] + phraseList[2][4] + phraseList[2][5] + "しました。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 5:
            phraseList = []
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            wList.append(random.choice(['実質', '相対', '実効']))
            wList.append(random.choice(['GDP', '国内総生産']))
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['%']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "の" + phraseList[0][2] + phraseList[0][3] + "は" + phraseList[0][4] + phraseList[0][5] + "の" + phraseList[0][6] + phraseList[0][7] + "です。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 6:
            phraseList = []
            wList = []
            wList.append(random.choice(['英国', 'イギリス', 'アメリカ', 'ドイツ', '米国', '中国', 'インド', '欧州', 'スペイン', '韓国', '日本']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['.']))
            wList.append(random.choice(self.number_master_smaller))
            phraseList.append(wList)
            sentence = phraseList[0][0] + "は" + phraseList[1][0] + phraseList[1][1] + phraseList[1][2] + "です。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 7:
            phraseList = []
            wList = []
            wList.append(random.choice(['英国', 'イギリス', 'アメリカ', 'ドイツ', '米国', '中国', 'インド', '欧州', 'スペイン', '韓国', '日本']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['英国', 'イギリス', 'アメリカ', 'ドイツ', '米国', '中国', 'インド', '欧州', 'スペイン', '韓国', '日本']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master_larger))
            wList.append(random.choice(['%']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + "は" + phraseList[1][0] + "の" + phraseList[2][0] + phraseList[2][1] + "です。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 8:
            phraseList = []
            wList = []
            wList.append(random.choice(['英国', 'イギリス', 'アメリカ', 'ドイツ', '米国', '中国', 'インド', '欧州', 'スペイン', '韓国', '日本']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['石油', '原油', '石炭', '天然ガス']))
            wList.append(random.choice(['依存', '寡占']))
            wList.append(random.choice(['度']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['.']))
            wList.append(random.choice(self.number_master_smaller))
            wList.append(random.choice(['%']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + "における" + phraseList[1][0] + "の" + phraseList[1][1] + phraseList[1][2] + "は" + phraseList[2][0] + phraseList[2][1] + phraseList[2][2] + phraseList[2][3] + "です。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 9:
            phraseList = []
            wList = []
            wList.append(random.choice(['英国', 'イギリス', 'アメリカ', 'ドイツ', '米国', '中国', 'インド', '欧州', 'スペイン', '韓国', '日本']))
            phraseList.append(wList)
            wList = []
            choiceList = random.sample(['石油', '原油', '石炭', '天然ガス'], 3)
            wList.append(choiceList[0])
            wList.append(choiceList[1])
            wList.append(choiceList[2])
            wList.append(random.choice(['依存', '寡占']))
            wList.append(random.choice(['度']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['.']))
            wList.append(random.choice(self.number_master_smaller))
            wList.append(random.choice(['%']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + "における" + phraseList[1][0] + "と" + phraseList[1][1] + "と" + phraseList[1][2] + "の" + phraseList[1][3] + phraseList[1][4] + "は" + phraseList[2][0] + phraseList[2][1] + phraseList[2][2] + phraseList[2][3] + "です。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 10:
            phraseList = []
            wList = []
            wList.append(random.choice(['石油', '原油', '石炭', '天然ガス']))
            wList.append(random.choice(['依存', '寡占']))
            wList.append(random.choice(['度']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['最も', '特に', '比較的', '次に']))
            wList.append(random.choice(['高い', '低い', '大きい', '小さい']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['英国', 'イギリス', 'アメリカ', 'ドイツ', '米国', '中国', 'インド', '欧州', 'スペイン', '韓国', '日本']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + "の" + phraseList[0][1] + phraseList[0][2] + "が" + phraseList[1][0] + phraseList[1][1] + "のは" + phraseList[2][0] + "です。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 11:
            phraseList = []
            wList = []
            choiceList = random.sample(['石油', '原油', '石炭', '天然ガス'], 3)
            wList.append(choiceList[0])
            wList.append(choiceList[1])
            wList.append(choiceList[2])
            wList.append(random.choice(['依存', '寡占']))
            wList.append(random.choice(['度']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['最も', '特に', '比較的', '次に']))
            wList.append(random.choice(['高い', '低い', '大きい', '小さい']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['英国', 'イギリス', 'アメリカ', 'ドイツ', '米国', '中国', 'インド', '欧州', 'スペイン', '韓国', '日本']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + "と" + phraseList[0][1] + "と" + phraseList[0][2] + "の" + phraseList[0][3] + phraseList[0][4] + "が" + phraseList[1][0] + phraseList[1][1] + "のは" + phraseList[2][0] + "です。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 12:
            phraseList = []
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['電力', '電気']))
            wList.append(random.choice(['化', '普及', '導入']))
            wList.append(random.choice(['率', '効率']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['.']))
            wList.append(random.choice(self.number_master_smaller))
            wList.append(random.choice(['%']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "の" + phraseList[1][0] + phraseList[1][1] + phraseList[1][2] + "は" + phraseList[2][0] + phraseList[2][1] + phraseList[2][2] + phraseList[2][3] + "です。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 13:
            phraseList = []
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['電力', '電気']))
            wList.append(random.choice(['化', '普及', '導入']))
            wList.append(random.choice(['率', '効率']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['.']))
            wList.append(random.choice(self.number_master_smaller))
            wList.append(random.choice(['%']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "の" + phraseList[1][0] + phraseList[1][1] + phraseList[1][2] + "は" + phraseList[2][0] + phraseList[2][1] + phraseList[2][2] + phraseList[2][3] + "です。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 14:
            phraseList = []
            wList = []
            wList.append(random.choice(['電力', '電気']))
            wList.append(random.choice(['化', '普及', '導入']))
            wList.append(random.choice(['率', '効率']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            wList.append(random.choice(['間']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['.']))
            wList.append(random.choice(self.number_master_smaller))
            wList.append(random.choice(['%']))
            wList.append(random.choice(['増加', '減少', '増大', '急増', '低下', '上昇', '拡大', '下落']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + phraseList[0][2] + "は" + phraseList[1][0] + phraseList[1][1] + "から" + phraseList[1][2] + phraseList[1][3] + "の" + phraseList[1][4] + "に" + phraseList[2][0] + phraseList[2][1] + phraseList[2][2] + phraseList[2][3] + phraseList[2][4] + "しました。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 15:
            phraseList = []
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['電力', '電気']))
            wList.append(random.choice(['化', '普及', '導入']))
            wList.append(random.choice(['率', '効率']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['%']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "の" + phraseList[1][0] + phraseList[1][1] + phraseList[1][2] + "は" + phraseList[2][0] + phraseList[2][1] + "の" + phraseList[3][0] + phraseList[3][1] + "です。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 16:
            phraseList = []
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['製造業', '建設業', '窯業', '製紙業']))
            wList.append(random.choice(['エネルギー源']))
            wList.append(random.choice(['占める']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['石油', '原油', '石炭', '天然ガス']))
            wList.append(random.choice(['比率', '割合', 'シェア']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['.']))
            wList.append(random.choice(self.number_master_smaller))
            wList.append(random.choice(['%']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "の" + phraseList[1][0] + phraseList[1][1] + "に" + phraseList[1][2] + phraseList[2][0] + "の" + phraseList[2][1] + "は" + phraseList[3][0] + phraseList[3][1] + phraseList[3][2] + phraseList[3][3] + "です。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 17:
            phraseList = []
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['最終']))
            wList.append(random.choice(['エネルギー']))
            wList.append(random.choice(['消費', '消費量', '需要', '使用', '生産量', '利用']))
            wList.append(random.choice(['占める']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['家庭', '工業', '産業', '一般家庭', '自動車', '運輸', '貨物']))
            wList.append(random.choice(['部門', '分野']))
            wList.append(random.choice(['比率', '割合', 'シェア']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['.']))
            wList.append(random.choice(self.number_master_smaller))
            wList.append(random.choice(['%']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "の" + phraseList[1][0] + phraseList[1][1] + phraseList[1][2] + "に" + phraseList[1][3] + phraseList[2][0] + phraseList[2][1] + "の" + phraseList[2][2] + "は" + phraseList[3][0] + phraseList[3][1] + phraseList[3][2] + phraseList[3][3] + "です。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 18:
            phraseList = []
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['最終']))
            wList.append(random.choice(['エネルギー']))
            wList.append(random.choice(['消費', '消費量', '需要', '使用', '生産量', '利用']))
            wList.append(random.choice(['占める']))
            phraseList.append(wList)
            wList = []
            choiceList = random.sample(['企業', '会社', '事業所', '世帯'], 2)
            wList.append(choiceList[0])
            wList.append(random.choice(['・']))
            wList.append(choiceList[1])
            wList.append(random.choice(['等']))
            wList.append(random.choice(['比率', '割合', 'シェア']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['.']))
            wList.append(random.choice(self.number_master_smaller))
            wList.append(random.choice(['%']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "の" + phraseList[1][0] + phraseList[1][1] + phraseList[1][2] + "に" + phraseList[1][3] + phraseList[2][0] + phraseList[2][1] + phraseList[2][2] + phraseList[2][3] + "の" + phraseList[2][4] + "は" + phraseList[3][0] + phraseList[3][1] + phraseList[3][2] + phraseList[3][3] + "です。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        
    def sort_random_list(self, phraseList):
        words = ""
        # random.shuffle(phraseList)
        for phrase in phraseList:
            for word in phrase:
                words = words + word
        return words
            
# test
if __name__ == '__main__':
    
    maker = Maker()
    m = MeCab.Tagger(r'-Owakati -d C:\Users\hori\workspace\encoder-decoder-sentence-chainer-master\mecab-ipadic-neologd')
    """
    parser = Parser()
    
    wordsList = []
    sentenceList = []
    for i in range(20000):
        index = random.randint(1, 18)
        words, sentence = maker.generate_word_sentence(index)
        words = m.parse(words)[:-2].split(' ')
        sentence = m.parse(sentence)[:-2].split(' ')
        for i in range(len(words)):
            w = words[i]
            words[i] = parser.parse(w)
        for i in range(len(sentence)):
            w = sentence[i]
            sentence[i] = parser.parse(w)
        words = " ".join(words)
        sentence = " ".join(sentence)
        words = parser.parse_num_fix(words)
        sentence = parser.parse_num_fix(sentence)
        wordsList.append(words)
        sentenceList.append(sentence)
    fw = open('words_20181118_parse.txt', 'wb')
    fs = open('sentence_20181118_parse.txt', 'wb')
    fw.write("\n".join(wordsList).encode('utf-8'))
    fs.write("\n".join(sentenceList).encode('utf-8'))
    """
    words, sentence = maker.generate_word_sentence(1)
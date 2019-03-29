# -*- coding: utf-8 -*-

import random
import MeCab

class Maker():
    def __init__(self):
        self.year_master = ['2013', '2014', '2015', '2012', '2016', '2009', '2006', '2017', '2011', '2007', '2008', '2005', '2018', '2010', '2002', '2003', '2004', '2019', '2001', '1997', '1972', '1998', '1992', '1985', '1986', '1993', '1982', '1983', '2022', '1989']
        self.number_master = []
        for i in range(100):
            self.number_master.append(str(i))
        
    def generate_word_sentence(self, code):
        if code == 1:
            phraseList = []
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['実質', '一時']))
            wList.append('GDP')
            wList.append(random.choice(['成長', '発展']))
            wList.append(random.choice(['率', '比率', '割合']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append('.')
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['%', '％']))
            wList.append(random.choice(['増', '減少', '増大', '増大', '増加', '減退', '低下', '減']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "の" + phraseList[1][0] + phraseList[1][1] + phraseList[1][2] + phraseList[1][3] + "は" + phraseList[2][0] + phraseList[2][1] + phraseList[2][2] + phraseList[2][3] + phraseList[2][4] + "でした。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 2:
            phraseList = []
            wList = []
            wList.append(random.choice(['原油', '石油', 'シェールガス', 'オイル', 'LNG', 'シェールオイル', 'ガソリン']))
            wList.append(random.choice(['価格', '市況', '相場', '物価']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['高騰', '上昇', '下落', '急落', '急騰', '乱高下', '低迷', '変動', '下降', '回復']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "は" + phraseList[1][0] + "しています。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 3:
            phraseList = []
            wList = []
            wList.append(random.choice(['エネルギー', '石炭']))
            wList.append(random.choice(['消費', '需要', '使用', '排出', '輸入', '輸出']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            wList.append(random.choice(['以降', '以後', '以来', 'から']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['減少', '増加', '低下', '上昇', '増大', '下落', '減退', '悪化', '低迷']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "は" + phraseList[1][0] + phraseList[1][1] + phraseList[1][2] + phraseList[2][0] + "しています。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 4:
            phraseList = []
            wList = []
            wList.append(random.choice(['製造', 'サービス', '鉄鋼', '畜産']))
            wList.append(random.choice(['業', '業種', '産業', '部門']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['省エネルギー', '省エネ']))
            wList.append(random.choice(['化']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['進ん', '取り組ん', '高まっ']))
            phraseList.append(wList)
            if phraseList[2][0] == '進ん':
                sentence = phraseList[0][0] + phraseList[0][1] + "では" + phraseList[1][0] + phraseList[1][1] + "が" + phraseList[2][0] + "でいます。"
            elif phraseList[2][0] == '取り組ん':
                sentence = phraseList[0][0] + phraseList[0][1] + "では" + phraseList[1][0] + phraseList[1][1] + "に" + phraseList[2][0] + "でいます。"
            elif phraseList[2][0] == '高まっ':
                sentence = phraseList[0][0] + phraseList[0][1] + "では" + phraseList[1][0] + phraseList[1][1] + "が" + phraseList[2][0] + "ています。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 5:
            phraseList = []
            wList = []
            wList.append(random.choice(['産業', '工業']))
            wList.append(random.choice(['部門']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append('.')
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['倍', '割', '%', '％']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "では" + phraseList[1][0] + phraseList[1][1] + phraseList[1][2] + phraseList[1][3] + "となりました。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 6:
            phraseList = []
            wList = []
            wList.append(random.choice(['産業', '工業', '家庭']))
            wList.append(random.choice(['部門']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['エネルギー', '石炭']))
            wList.append(random.choice(['消費', '需要', '使用', '輸入', '輸出', '生産']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['同', '同じ']))
            wList.append(random.choice(['程度']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['推移', '減少', '増加', '上昇', '低迷']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "では" + phraseList[1][0] + phraseList[1][1] + "は" + phraseList[2][0] + phraseList[2][1] + "で" + phraseList[3][0] + "しています。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code ==7:
            phraseList = []
            wList = []
            wList.append(random.choice(['国内', '海外', '国外', '自国', 'わが国']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['再生', '持続']))
            wList.append(random.choice(['可能']))
            wList.append(random.choice(['エネルギー']))
            wList.append(random.choice(['導入', '普及', '利用', '創出']))
            wList.append(random.choice(['量', '指数', '割合']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['倍', '割', '%', '％']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['減少', '増加', '低下', '上昇', '増大', '下落', '減退', '悪化', '低迷']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + "での" + phraseList[1][0] + phraseList[1][1] + phraseList[1][2] + phraseList[1][3] + phraseList[1][4] + "は" + phraseList[2][0] + phraseList[2][1] + "から" + phraseList[2][2] + phraseList[2][3] + "までに" + phraseList[3][0] + phraseList[3][1] + "に" + phraseList[4][0] + "しています。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 8:
            phraseList = []
            wList = []
            wList.append(random.choice(['風力', '太陽光', '地熱', '水力', '火力', '原子力']))
            wList.append(random.choice(['発電']))
            wList.append(random.choice(['利益', '収益', '利潤', '収支']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['倍', '割', '%', '％']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['減少', '増加', '低下', '上昇', '増大', '下落', '減退', '悪化', '低迷']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "の" + phraseList[0][2] + "は" + phraseList[1][0] + phraseList[1][1] + "から" + phraseList[1][2] + phraseList[1][3] + "までに" + phraseList[2][0] + phraseList[2][1] + phraseList[3][0] + "しています。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 9:
            phraseList = []
            wList = []
            wList.append(random.choice(['現在']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['保有', '所有']))
            wList.append(random.choice(['資産', '株式', '資本']))
            wList.append(random.choice(['割合', '比率', 'シェア']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['%', '％']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['アメリカ', '米国', '英国', 'イタリア', 'ドイツ', 'イギリス', '欧州']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['国外', '海外']))
            wList.append(random.choice(['比率', '割合', 'シェア']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['高い', '低い', '大きい']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['企業']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + "では、" + phraseList[1][0] + phraseList[1][1] + "の" + phraseList[1][2] + "の" + phraseList[2][0] + phraseList[2][1] + "が" + phraseList[3][0] + "と、" + phraseList[4][0] + phraseList[4][1] + "が" + phraseList[5][0] + phraseList[6][0] + "となっています。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 10:
            phraseList = []
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['アメリカ', '米国', '英国', 'イタリア', 'ドイツ', 'イギリス', '欧州']))
            wList.append(random.choice(['電気']))
            wList.append(random.choice(['送電', '配電', '接続']))
            wList.append(random.choice(['網', 'ネットワーク', 'パイプライン', '線']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['億', '兆', '万', '千']))
            wList.append(random.choice(['ポンド', 'ユーロ', 'ドル', '円']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['投資', '融資', '出資']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "に" + phraseList[1][0] + "の" + phraseList[1][1] + phraseList[1][2] + phraseList[1][3] + "に" + phraseList[2][0] + phraseList[2][1] + phraseList[2][2] + phraseList[3][0] + "しています。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 11:
            phraseList = []
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            wList.append(random.choice(['現在']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['か国', 'カ国', 'ヵ国', 'ヶ国']))
            wList.append(random.choice(['以上', '程度', '近く']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['進出', '参画', '参入', '展開']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + phraseList[0][2] + "、" + phraseList[1][0] + phraseList[1][1] + phraseList[1][2] + phraseList[2][0] + "しています。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 12:
            phraseList = []
            wList = []
            wList.append(random.choice(['電気', '電力', 'ガス']))
            wList.append(random.choice(['消費', '需要', '使用']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['石油', 'オイル']))
            wList.append(random.choice(['ショック']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            wList.append(random.choice(['以降', '以後', '以来']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['着実', '確実', '急速']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['減少', '増加', '低下', '上昇', '増大', '下落', '減退']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "は、" + phraseList[1][0] + phraseList[1][1] + "の" + phraseList[2][0] + phraseList[2][1] + phraseList[2][2] + "も" + phraseList[3][0] + "に" + phraseList[4][0] + "しています。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 13:
            phraseList = []
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['.']))
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['倍', '割', '%', '％']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['拡大', '増大', '低下', '増加', '増大']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "から" + phraseList[0][2] + phraseList[0][3] + "の間に" + phraseList[1][0] + phraseList[1][1] + phraseList[1][2] + phraseList[1][3] + "に" + phraseList[2][0] + "しました。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 14:
            phraseList = []
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['世界', '国際']))
            wList.append(random.choice(['的']))
            wList.append(random.choice(['金融', '通貨']))
            wList.append(random.choice(['危機']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['影響', '悪影響', 'インパクト']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['生産', '出荷']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['減少', '増加', '低下', '上昇', '増大', '下落', '減退']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "から、" + phraseList[1][0] + phraseList[1][1] + phraseList[1][2] + phraseList[1][3] + "の" + phraseList[2][0] + "で" + phraseList[3][0] + "が" + phraseList[4][0] + "しました。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 15:
            phraseList = []
            wList = []
            wList.append(random.choice(['企業', '会社', '銀行', '組織']))
            wList.append(random.choice(['向け']))
            wList.append(random.choice(['中心', '主力', '始め']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['電気', '電力', 'ガス']))
            wList.append(random.choice(['消費', '需要', '使用', '生産']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['減少', '上昇', '増大', '下落']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['転じ', '向かい']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "を" + phraseList[0][2] + "に" + phraseList[1][0] + phraseList[1][1] + "が" + phraseList[2][0] + "に" + phraseList[3][0] + "ました。"
            words = self.sort_random_list(phraseList)
            return words, sentence
        if code == 16:
            phraseList = []
            wList = []
            wList.append(random.choice(['入札', '改定', '募集', '投票', '落札', '評価', '算定']))
            wList.append(random.choice(['量', '指数', '割合']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['第', '']))
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['回', '章', '節', '条', '部', '号']))
            wList.append(random.choice(['～', 'から', '〜', '~']))
            wList.append(random.choice(['第', '']))
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['回', '章', '節', '条', '部', '号']))
            phraseList.append(wList)
            wList = []
            wList.append(random.choice(['合計', '最大', '約', '推計', 'およそ', '推定']))
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['～', 'から', '〜', '~']))
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['GW', '%', '％', 'リットル', 'ユーロ', 'MW']))
            wList.append(random.choice(['募集', '聴取', '公募']))
            phraseList.append(wList)
            sentence = phraseList[0][0] + phraseList[0][1] + "につきましては、" + phraseList[1][0] + phraseList[1][1] + phraseList[1][2] + phraseList[1][3] + phraseList[1][4] + phraseList[1][5] + phraseList[1][6] + "で" + phraseList[2][0] + phraseList[2][1] + phraseList[2][2] + phraseList[2][3] + phraseList[2][4] + "を" + phraseList[2][5] + "することとしました。"
            words = self.sort_random_list(phraseList)
            return words, sentence
            
    def sort_random_list(self, phraseList):
        words = ""
        random.shuffle(phraseList)
        for phrase in phraseList:
            for word in phrase:
                words = words + word
        return words
            
# test
if __name__ == '__main__':
    maker = Maker()
    m = MeCab.Tagger('-Owakati')
    
    wordsList = []
    sentenceList = []
    for i in range(10000):
        index = random.randint(1, 16)
        words, sentence = maker.generate_word_sentence(index)
        words = m.parse(words)[:-2]
        sentence = m.parse(sentence)[:-2]
        wordsList.append(words)
        sentenceList.append(sentence)
    fw = open('words_random_order20181105_2.txt', 'wb')
    fs = open('sentence_random_order20181105_2.txt', 'wb')
    fw.write("\n".join(wordsList).encode('utf-8'))
    fs.write("\n".join(sentenceList).encode('utf-8'))
    
    # words, sentence = maker.generate_word_sentence(1)
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
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年', '年版']))
            wList.append(random.choice(['実質', '一時']))
            wList.append('GDP')
            wList.append(random.choice(['成長', '発展']))
            wList.append(random.choice(['率', '比率', '割合']))
            wList.append(random.choice(self.number_master))
            wList.append('.')
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['%', '％']))
            wList.append(random.choice(['増', '減少', '増大', '増大', '増加', '減退', '低下', '減']))
            words = ""
            for w in wList:
                words = words + w
            sentence = wList[0] + wList[1] + "の" + wList[2] + wList[3] + wList[4] + wList[5] + "は" + wList[6] + wList[7] + wList[8] + wList[9] + wList[10] + "でした。"
            return words, sentence
        if code == 2:
            wList = []
            wList.append(random.choice(['原油', '石油', 'シェールガス', 'オイル', 'LNG', 'シェールオイル', 'ガソリン']))
            wList.append(random.choice(['価格', '市況', '相場', '物価']))
            wList.append(random.choice(['高騰', '上昇', '下落', '急落', '急騰', '乱高下', '低迷', '変動', '下降', '回復']))
            words = ""
            for w in wList:
                words = words + w
            sentence = wList[0] + wList[1] + "は" + wList[2] + "しています。"
            return words, sentence
        if code == 3:
            wList = []
            wList.append(random.choice(['エネルギー', '石炭']))
            wList.append(random.choice(['消費', '需要', '使用', '排出', '輸入', '輸出']))
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            wList.append(random.choice(['以降', '以後', '以来', 'から']))
            wList.append(random.choice(['減少', '増加', '低下', '上昇', '増大', '下落', '減退', '悪化', '低迷']))
            words = ""
            for w in wList:
                words = words + w
            sentence = wList[0] + wList[1] + "は" + wList[2] + wList[3] + wList[4] + wList[5] + "しています。"
            return words, sentence
        if code == 4:
            wList = []
            wList.append(random.choice(['製造', 'サービス', '鉄鋼', '畜産']))
            wList.append(random.choice(['業', '業種', '産業', '部門']))
            wList.append(random.choice(['省エネルギー', '省エネ']))
            wList.append(random.choice(['化']))
            wList.append(random.choice(['進ん', '取り組ん', '高まっ']))
            words = ""
            for w in wList:
                words = words + w
            if wList[4] == '進ん':
                sentence = wList[0] + wList[1] + "では" + wList[2] + wList[3] + "が" + wList[4] + "でいます。"
            elif wList[4] == '取り組ん':
                sentence = wList[0] + wList[1] + "では" + wList[2] + wList[3] + "に" + wList[4] + "でいます。"
            elif wList[4] == '高まっ':
                sentence = wList[0] + wList[1] + "では" + wList[2] + wList[3] + "が" + wList[4] + "ています。"
            return words, sentence
        if code == 5:
            wList = []
            wList.append(random.choice(['産業', '工業']))
            wList.append(random.choice(['部門']))
            wList.append(random.choice(self.number_master))
            wList.append('.')
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['倍', '割', '%', '％']))
            words = ""
            for w in wList:
                words = words + w
            sentence = wList[0] + wList[1] + "では" + wList[2] + wList[3] + wList[4] + wList[5] + "となりました。"
            return words, sentence
        if code == 6:
            wList = []
            wList.append(random.choice(['産業', '工業', '家庭']))
            wList.append(random.choice(['部門']))
            wList.append(random.choice(['エネルギー', '石炭']))
            wList.append(random.choice(['消費', '需要', '使用', '輸入', '輸出', '生産']))
            wList.append(random.choice(['同', '同じ']))
            wList.append(random.choice(['程度']))
            wList.append(random.choice(['推移', '減少', '増加', '上昇', '低迷']))
            words = ""
            for w in wList:
                words = words + w
            sentence = wList[0] + wList[1] + "では" + wList[2] + wList[3] + "は" + wList[4] + wList[5] + "で" + wList[6] + "しています。"
            return words, sentence
        if code ==7:
            wList = []
            wList.append(random.choice(['国内', '海外', '国外', '自国', 'わが国']))
            wList.append(random.choice(['再生', '持続']))
            wList.append(random.choice(['可能']))
            wList.append(random.choice(['エネルギー']))
            wList.append(random.choice(['導入', '普及', '利用', '創出']))
            wList.append(random.choice(['量', '指数', '割合']))
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['倍', '割', '%', '％']))
            wList.append(random.choice(['減少', '増加', '低下', '上昇', '増大', '下落', '減退', '悪化', '低迷']))
            words = ""
            for w in wList:
                words = words + w
            sentence = wList[0] + "での" + wList[1] + wList[2] + wList[3] + wList[4] + wList[5] + "は" + wList[6] + wList[7] + "から" + wList[8] + wList[9] + "までに" + wList[10] + wList[11] + "に" + wList[12] + "しています。"
            return words, sentence
        if code == 8:
            wList = []
            wList.append(random.choice(['風力', '太陽光', '地熱', '水力', '火力', '原子力']))
            wList.append(random.choice(['発電']))
            wList.append(random.choice(['利益', '収益', '利潤', '収支']))
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['倍', '割', '%', '％']))
            wList.append(random.choice(['減少', '増加', '低下', '上昇', '増大', '下落', '減退', '悪化', '低迷']))
            words = ""
            for w in wList:
                words = words + w
            sentence = wList[0] + wList[1] + "の" + wList[2] + "は" + wList[3] + wList[4] + "から" + wList[5] + wList[6] + "までに" + wList[7] + wList[8] + wList[9] + "しています。"
            return words, sentence
        if code == 9:
            wList = []
            wList.append(random.choice(['現在']))
            wList.append(random.choice(['保有', '所有']))
            wList.append(random.choice(['資産', '株式', '資本']))
            wList.append(random.choice(['割合', '比率', 'シェア']))
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['%', '％']))
            wList.append(random.choice(['アメリカ', '米国', '英国', 'イタリア', 'ドイツ', 'イギリス', '欧州']))
            wList.append(random.choice(['国外', '海外']))
            wList.append(random.choice(['比率', '割合', 'シェア']))
            wList.append(random.choice(['高い', '低い', '大きい']))
            wList.append(random.choice(['企業']))
            words = ""
            for w in wList:
                words = words + w
            sentence = wList[0] + "では、" + wList[1] + wList[2] + "の" + wList[3] + "の" + wList[4] + wList[5] + "が" + wList[6] + "と、" + wList[7] + wList[8] + "が" + wList[9] + wList[10] + "となっています。"
            return words, sentence
        if code == 10:
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            wList.append(random.choice(['アメリカ', '米国', '英国', 'イタリア', 'ドイツ', 'イギリス', '欧州']))
            wList.append(random.choice(['電気']))
            wList.append(random.choice(['送電', '配電', '接続']))
            wList.append(random.choice(['網', 'ネットワーク', 'パイプライン', '線']))
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['億', '兆', '万', '千']))
            wList.append(random.choice(['ポンド', 'ユーロ', 'ドル', '円']))
            wList.append(random.choice(['投資', '融資', '出資']))
            words = ""
            for w in wList:
                words = words + w
            sentence = wList[0] + wList[1] + "に" + wList[2] + "の" + wList[3] + wList[4] + wList[5] + "に" + wList[6] + wList[7] + wList[8] + wList[9] + "しています。"
            return words, sentence
        if code == 11:
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            wList.append(random.choice(['現在']))
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['か国', 'カ国', 'ヵ国', 'ヶ国']))
            wList.append(random.choice(['以上', '程度', '近く']))
            wList.append(random.choice(['進出', '参画', '参入', '展開']))
            words = ""
            for w in wList:
                words = words + w
            sentence = wList[0] + wList[1] + wList[2] + "、" + wList[3] + wList[4] + wList[5] + wList[6] + "しています。"
            return words, sentence
        if code == 12:
            wList = []
            wList.append(random.choice(['電気', '電力', 'ガス']))
            wList.append(random.choice(['消費', '需要', '使用']))
            wList.append(random.choice(['石油', 'オイル']))
            wList.append(random.choice(['ショック']))
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            wList.append(random.choice(['以降', '以後', '以来']))
            wList.append(random.choice(['着実', '確実', '急速']))
            wList.append(random.choice(['減少', '増加', '低下', '上昇', '増大', '下落', '減退']))
            words = ""
            for w in wList:
                words = words + w
            sentence = wList[0] + wList[1] + "は、" + wList[2] + wList[3] + "の" + wList[4] + wList[5] + wList[6] + "も" + wList[7] + "に" + wList[8] + "しています。"
            return words, sentence
        if code == 13:
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['.']))
            wList.append(random.choice(self.number_master))
            wList.append(random.choice(['倍', '割', '%', '％']))
            wList.append(random.choice(['拡大', '増大', '低下', '増加', '増大']))
            words = ""
            for w in wList:
                words = words + w
            sentence = wList[0] + wList[1] + "から" + wList[2] + wList[3] + "の間に" + wList[4] + wList[5] +wList[6] + wList[7] + "に" + wList[8] + "しました。"
            return words, sentence
        if code == 14:
            wList = []
            wList.append(random.choice(self.year_master))
            wList.append(random.choice(['年度', '年']))
            wList.append(random.choice(['世界', '国際']))
            wList.append(random.choice(['的']))
            wList.append(random.choice(['金融', '通貨']))
            wList.append(random.choice(['危機']))
            wList.append(random.choice(['影響', '悪影響', 'インパクト']))
            wList.append(random.choice(['生産', '出荷']))
            wList.append(random.choice(['減少', '増加', '低下', '上昇', '増大', '下落', '減退']))
            words = ""
            for w in wList:
                words = words + w
            sentence = wList[0] + wList[1] + "から、" + wList[2] + wList[3] + wList[4] + wList[5] + "の" + wList[6] + "で" + wList[7] + "が" + wList[8] + "しました。"
            return words, sentence
        if code == 15:
            wList = []
            wList.append(random.choice(['企業', '会社', '銀行', '組織']))
            wList.append(random.choice(['向け']))
            wList.append(random.choice(['中心', '主力', '始め']))
            wList.append(random.choice(['電気', '電力', 'ガス']))
            wList.append(random.choice(['消費', '需要', '使用', '生産']))
            wList.append(random.choice(['減少', '上昇', '増大', '下落']))
            wList.append(random.choice(['転じ', '向かい']))
            words = ""
            for w in wList:
                words = words + w
            sentence = wList[0] + wList[1] + "を" + wList[2] + "に" + wList[3] + wList[4] + "が" + wList[5] + "に" + wList[6] + "ました。"
            return words, sentence
            
# test
if __name__ == '__main__':
    maker = Maker()
    m = MeCab.Tagger('-Owakati')
    wordsList = []
    sentenceList = []
    for i in range(10000):
        index = random.randint(1, 15)
        words, sentence = maker.generate_word_sentence(index)
        words = m.parse(words)[:-2]
        sentence = m.parse(sentence)[:-2]
        wordsList.append(words)
        sentenceList.append(sentence)
    fw = open('words20181017.txt', 'wb')
    fs = open('sentence20181017.txt', 'wb')
    fw.write("\n".join(wordsList).encode('utf-8'))
    fs.write("\n".join(sentenceList).encode('utf-8'))
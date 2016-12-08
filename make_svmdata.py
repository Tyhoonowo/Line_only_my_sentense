# -*- coding:utf-8 -*-
'''
持ってきたuser.txtを
1．分かち書き

2．tfidfを求める


'''
import os
import re
import MeCab
import math

def calc_tf(sentence):
	m = MeCab.Tagger ("--node-format=%m\s%f[0]\\n --eos-format='' ")#メカブを使う
	# f = open(file_pass, 'r')#00000370.txtフィアルを開く
	# doc=f.read()#ファイルの内容をdocにいれる
	nobe = 0
	hinshinobe = 0
	# doc.decode("utf-8")
	# print doc
	# print m.parse(doc)
	cd = m.parse(sentence)#メカブを使用したものをcdに入れる
	list1 = []#名詞のみを入れるリスト
	cp2 = cd.split()#真ん中の空白をなくす
	del cp2[-1]


#---------------------------------------------------------------前回参照
	# # for i in range(len(cp2)):#
	# # 	j = i%2
	# # 	if j == 0:
	# # 		print cp2[i], cp2[i+1]
	# print "異なり語数"
	# word = cp2[0::2] #偶数だけとるプログラム
	# hinshi = cp2[1::2] #奇数だけ取るプログラム
	# # for i in range(len(word)):#メカブの情報を取り出すがエラーをはく
	# print word[i],hinshi[i]

	# for i in range(len(hinshi)):#1から品詞の数分繰り返す
	# 	spell = re.search("名詞",hinshi[i])#名詞と書いているものを取り出す
	# 	if spell:#一致した時
	# 		list1.append(word[i])#wordの配列に入れる
#-----------------------------------------------------------

	list1 = cp2[0::2]

	tf = {}#リストをつくる
	for tfword in list1:#名詞のリストからすべてを取り出す
		if tfword not in tf:#リストの中に今までのものが入ってないときに
			tf[tfword] = 0#ｔｆに0を入れる
		tf[tfword] += 1#数をふやす

	# for z in list1:#正規化をする
	# 	print z,tf[z]#単語と頻度の表示
		# tf[z] = 1.0*tf[z]/len(list1)#正規化シたものの表示
	nomalize_tf = {}
		#### 単語をキーとして正規化した値を保存 ####
	for k, l in tf.items():
		nomalize_tf[k] = 1.0 * l / len(list1)

	return nomalize_tf

def calc_df(tf):
	df = {}#dfのディクショナリを宣言
	for dfword in tf:	#tfの配列を渡してもらう
		for df2word in dfword.keys():	#tfで取り出した文字列を繰り返す
			if df2word not in df:	#ユニークをする
				df[df2word] = 0	#単語を新しく入れる
			df[df2word] += 1 #dfの値を入れる
	return df

def calc_idf(df,sentencenum):
	idf={}#idfのディクショナリを宣言
	for idfword in df.keys():#dfの単語を繰り返す
		idf[idfword] = math.log(1.0*sentencenum/df[idfword])+1#idfを求める
	return idf

def calc_tfidf(tf,idf):
	tfidfdic = {}#ディクショナリ
	tfidf = []#リスト（結果）をいれる
	for tfdoc in tf:#一つの文章をとりだす
		for tfword in tfdoc.keys():# 文字に入れる。
			tfidfdic[tfword] = tfdoc[tfword] * idf[tfword]#tfidfに値をいれる
		tfidf.append(tfidfdic)#一致した時にtfidfにいれる
		tfidfdic = {}#再初期化
	# print tf[0]["KDDI"]
	# print idf["KDDI"]
	return tfidf

def tfidf_process(body_file):
	tf5 = []
	df5 = []
	idf5 = []
	tfidf5 = []
	for sentence in body_file:#星5のtfを求める
		tf5.append(calc_tf(sentence))
	df5 = calc_df(tf5)
	idf5 = calc_idf(df5,len(body_file))
	tfidf5 = calc_tfidf(tf5,idf5)
	return tfidf5

def make_svm_word_array(word,tfidf):
	num = len(word)
	print num
	for title in tfidf:
		for title_word in title.keys():
			if title_word not in word:
				word[title_word] = num
				num = num + 1
	return word


if __name__=="__main__":

	user = []
	tfidf_user = []
	tf = []
	word = {}

	input_file = open('user.txt')
	line = input_file.readline()

	while line:
		# print line
		user.append(line)
		line = input_file.readline()

	tfidf_user = tfidf_process(user)

	# # 以下確認プログラム
	# for i in tfidf_user:
	# 	for k,l in i.items():
	# 		print k,l
	word = make_svm_word_array(word, tfidf_user)
	word = make_svm_word_array(word, tfidf_user)
	

'''
以下確認等
	# for sentence in user:
	# 	tf.append(calc_tf(sentence))

	# for i in tf:
	# 	for k,l in i.items():
	# 		print k,l

	# for sentence in user:
	# 	m = MeCab.Tagger ("--node-format=%m\s%f[0]\\n --eos-format='' ")#メカブを使う
	# 	cd = m.parse(sentence)#メカブを使用したものをcdに入れる
	# 	cp2 = cd.split()#真ん中の空白をなくす
	# 	del cp2[-1]
	# 	word = cp2[0::2] #偶数だけとるプログラム
	# 	hinshi = cp2[1::2] #奇数だけ取るプログラム
	# 	for i in word:
	# 		print i
'''

	

	# 	#ここから下svr_lightに渡す学習データを作る！！！
	# #言葉をタグづけする
	# for title1 in tfidf1:	#tfidf1の配列を渡してもらう
	# 	for title1_word in title1.keys():	#tfidfで取り出した文字列を繰り返す
	# 		# print title1_word, title1[title1_word]#tfidfの単語と状態表示
	# 		if title1_word not in words:#言葉にタグをつけるプログラム
	# 			words[title1_word] = num
	# 			num = num + 1
	# #タグづけされたでーたを元にして書き込む
	# for title1 in tfidf1:
	# 	fp.write('1 ')
	# 	for title1_word in title1.keys():
	# 		if title1_word not in words.keys():#もし、単語が入ってないとき
	# 			break
	# 		tag = words[title1_word]#タグを取り出す
	# 		attrs[tag] = title1[title1_word]
	# 		# if tag in attrs:#
	# 		# 	attrs[tag] = attrs[tag] + 1
	# 		# else:
	# 		# 	attrs[tag] = 1
	# 		# print title1_word,tag#出ているものの表示
	# 	for ak in sorted(attrs.keys()):
	# 		if attrs[ak] != 0:
	# 			# print str(ak) + ":" + str(attrs[ak])
	# 			fp.write(str(ak))
	# 			fp.write(':')
	# 			fp.write(str(attrs[ak]))
	# 			fp.write(' ')
	# 	for i in range(len(attrs)):#初期化
	# 		attrs[i] = 0
	# 	fp.write('\n')
	# 		# if title1_word not in str1:	#ユニークをする
	# 		# 	df[df2word] = 0	#単語を新しく入れる
	# 		# df[df2word] += 1 #dfの値を入れる



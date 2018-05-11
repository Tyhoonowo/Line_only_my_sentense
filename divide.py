# -*- coding:utf-8 -*-
'''
Lineの文章を分割するプログラム
人のLineの文章を取ってくる

前回との違い
うまくいかなかった段落のバグを直しました

githubの確認
'''

import MeCab
import re
import sys

#名前の入力（抽出させる）
USER_NAME = "名前入力"
# USER_NAME = "りんな"

#入力ファイル，出力ファイルをきめる
input_file = open('input_data.txt')
output_file = open('user.txt','w+')

#ファイルの読み込み
line_data = input_file.read()
line_data.decode("utf-8")


#時刻によって分ける
line_split_data = re.split(r'\n\d+:\d+ ',line_data)

#時刻で分類したものを取り出し，それが「りんな」でなく，「自分の名前」が含まれていた時を抽出
#その名前の部分（最初）を削除(ファイルによって変更)
for i in line_split_data:
	for j in re.findall(USER_NAME,i):
		sentence = i.lstrip(USER_NAME)
		next = sentence.lstrip()
		output_file.write(str(next))
		output_file.write("\n")

input_file.close
output_file.close


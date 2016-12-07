# -*- coding:utf-8 -*-
'''
Lineの文章を分割するプログラム
人のLineの文章を取ってくる

前回との違い
うまくいかなかった段落のバグを直しました

'''

import MeCab
import re
import sys

USER_NAME = "名前入力"
# USER_NAME = "りんな"


input_file = open('input_data.txt')
#input_file = open('easy_test.txt','r')
output_file = open('user.txt','w+')
# pre_file = open('pre.txt','w+')

line_data = input_file.read()
line_data.decode("utf-8")
print "データの読み取りとデコード"

#line_split_data = line_data.split("i")
#line_split_data = line_data.split(r'\d+')
line_split_data = re.split(r'\n\d+:\d+ ',line_data)

#以下繰り返しの見直し
# for i in range(len(line_split_data)):
# 	print line_split_data[i]

# for k in line_split_data:
# 	print k

#以下書き込みの見直し
# for i in line_split_data:
# 	output_file.write( str (i) )
# 	output_file.write("\n")

# output_file.write( str(line_split_data) )

for i in line_split_data:
	for j in re.findall(USER_NAME,i):
	# for j in re.findall("村橋達明",i):
		# pre_file.write( str (i) )
		# pre_file.write("\n")
		# output_file.write( str (i.lstrip(USER_NAME+" ")) )
		sentence = i.lstrip(USER_NAME)
		print sentence ,"処理前"
		next = sentence.lstrip()
		print next ,"空白処理後"
		output_file.write(str(next))
		output_file.write("\n")
		# pre_file.write(str(sentence))
		# pre_file.write("\n")
		# output_file.write( str ( sentence.lstrip() ) )
		# output_file.write( str (i.lstrip()) )
		# output_file.write("\n")
		


input_file.close
output_file.close
# pre_file.close

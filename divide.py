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

input_file = open('input_data.txt')
#input_file = open('easy_test.txt','r')
output_file = open('user.txt','w+')

line_data = input_file.read()
line_data.decode("utf-8")
print "データの読み取りとデコード"

#line_split_data = line_data.split("i")
#line_split_data = line_data.split(r'\d+')
line_split_data = re.split(r'\n\d+:\d+ ',line_data)

for i in range(len(line_split_data)):
	print line_split_data[i]

for k in line_split_data:
	print k

output_file.write( str(line_data) )

input_file.close
output_file.close


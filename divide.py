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

output_file.write( str(line_data) )

input_file.close
output_file.close


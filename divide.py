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

line_data = input_file.read()
input_file.close()

print "デバッグ用"

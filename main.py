# coding=gbk

f = open("title.txt" , mode= "r")

a = f.readlines()

print(a)

b = '国内新闻：北京疾控：接种新冠疫苗后不得带离按压棉签'
c = '国内新闻：北京市属公园11日至17日免费开放，8日开始预约'

import difflib

def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

# for i in a:
#     print(i)
# print(ord(a)-ord(b))
# print(ord(a)-ord(c))
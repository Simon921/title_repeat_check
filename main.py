# coding=gbk
import difflib

f = open("title.txt", mode="r")
a = f.readlines()

b = '国内新闻：北京疾控：接种新冠疫苗后不得带离按压棉签'
c = '国内新闻：北京市属公园11日至17日免费开放，8日开始预约'


def string_similar(s1, s2):
    return difflib.SequenceMatcher(lambda x: x == "\n", s1, s2).quick_ratio()


m = 1

for i in a:
    print(m - 1)
    print(a[m - 1], a[m], string_similar(a[m - 1], a[m]))
    m += 1
    print(m)

# coding=gbk
import difflib

f = open("title.txt", mode="r", encoding='gbk')
a = f.readlines()
f.close()
q = open("title.txt", mode="r", encoding='gbk')
b = q.readlines()
q.close()


def string_similar(s1, s2):
    return difflib.SequenceMatcher(lambda x: x == "\n", s1, s2).quick_ratio()


for i in a:
    for k in b:
        print(i, k, string_similar(i, k))



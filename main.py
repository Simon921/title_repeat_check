# coding=gbk
import difflib

f = open("title.txt", mode="r", encoding='gbk')
a = f.readlines()
f.close()
q = open("title.txt", mode="r", encoding='gbk')
b = q.readlines()
q.close()


def string_similar(s1, s2):
    return difflib.SequenceMatcher(lambda x: x == '\n国内新闻国际新闻', s1, s2).quick_ratio()


with open('test.txt', "w") as f:
    f.write('')

r = []

for i in a:
    for k in b:
        samerate = i + k + str(string_similar(i, k)) + "\n\n"
        if 1 > string_similar(i, k) > 0.55:
            r.append(samerate)
            print(i, k)


with open('test.txt', 'a') as f:
    for i in r:
        f.write(i)

# coding=gbk
import difflib

f = open("title.txt", mode="r")
a = f.readlines()

b = '�������ţ��������أ������¹�����󲻵ô��밴ѹ��ǩ'
c = '�������ţ�����������԰11����17����ѿ��ţ�8�տ�ʼԤԼ'


def string_similar(s1, s2):
    return difflib.SequenceMatcher(lambda x: x == "\n", s1, s2).quick_ratio()


m = 1

for i in a:
    print(m - 1)
    print(a[m - 1], a[m], string_similar(a[m - 1], a[m]))
    m += 1
    print(m)

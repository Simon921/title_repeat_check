# coding=gbk

f = open("title.txt" , mode= "r")

a = f.readlines()

print(a)

b = '�������ţ��������أ������¹�����󲻵ô��밴ѹ��ǩ'
c = '�������ţ�����������԰11����17����ѿ��ţ�8�տ�ʼԤԼ'

import difflib

def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

# for i in a:
#     print(i)
# print(ord(a)-ord(b))
# print(ord(a)-ord(c))
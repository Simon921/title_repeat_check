# coding=gbk
import difflib

f = open("����.txt", mode="r", encoding='gbk')
a = f.readlines()
f.close()

q = open("����.txt", mode="r", encoding='gbk')
b = q.readlines()
q.close()


def string_similar(s1, s2):
    return difflib.SequenceMatcher(lambda x: x == '\n', s1, s2).quick_ratio()


with open('���.txt', "w") as f:
    f.write('')

r = []

for i in a:
    for k in b:
        samerate_str = "��� " + str(a.index(i)) + " " + i + "��� " + str(b.index(k)) + " " + k
        samerate_val = "���ƶȣ� " + str(string_similar(i, k))[0:4] + "\n\n"
        samerate = (samerate_str, samerate_val)
        if 1 > string_similar(i, k) > 0.55:
            r.append(samerate)
            print(samerate)


with open('���.txt', 'a') as f:
    # ��ȡ�б�ĵڶ���Ԫ��
    def takeSecond(elem):
        return elem[1]

    # ָ���ڶ���Ԫ������ ����
    r.sort(key=takeSecond, reverse=True)

    for i in r:
        if (r.index(i) % 2) == 0:
            f.write(i[0])
            f.write(i[1])

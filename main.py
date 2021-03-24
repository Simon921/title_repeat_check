# coding=gbk
import difflib

f = open("标题.txt", mode="r", encoding='gbk')
a = f.readlines()
f.close()

q = open("标题.txt", mode="r", encoding='gbk')
b = q.readlines()
q.close()


def string_similar(s1, s2):
    return difflib.SequenceMatcher(lambda x: x == '\n', s1, s2).quick_ratio()


with open('结果.txt', "w") as f:
    f.write('')

r = []

for i in a:
    for k in b:
        samerate_str = "序号 " + str(a.index(i)) + " " + i + "序号 " + str(b.index(k)) + " " + k
        samerate_val = "相似度： " + str(string_similar(i, k))[0:4] + "\n\n"
        samerate = (samerate_str, samerate_val)
        if 1 > string_similar(i, k) > 0.55:
            r.append(samerate)
            print(samerate)


with open('结果.txt', 'a') as f:
    # 获取列表的第二个元素
    def takeSecond(elem):
        return elem[1]

    # 指定第二个元素排序 降序
    r.sort(key=takeSecond, reverse=True)

    for i in r:
        if (r.index(i) % 2) == 0:
            f.write(i[0])
            f.write(i[1])

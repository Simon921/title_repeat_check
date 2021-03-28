# coding=gbk
import difflib

# f = open("����.txt", mode="r", encoding='gbk')
# a = f.readlines()
# f.close()
#
# q = open("����.txt", mode="r", encoding='gbk')
# b = q.readlines()
# q.close()


def string_similar(s1, s2):
    return difflib.SequenceMatcher(lambda x: x == '\n', s1, s2).quick_ratio()


# with open('���.txt', "w") as f:
#     f.write('')
#
# r = []
#
# for i in a:
#     for k in b:
#         samerate_str = "��� " + str(a.index(i)) + " " + i + "��� " + str(b.index(k)) + " " + k
#         samerate_val = "���ƶȣ� " + str(string_similar(i, k))[0:4] + "\n\n"
#         samerate = (samerate_str, samerate_val)
#         if 1 > string_similar(i, k) > 0.55:
#             r.append(samerate)
#             print(samerate)
#
# with open('���.txt', 'a') as f:
#     # ��ȡ�б�ĵڶ���Ԫ��
#     def takesecond(elem):
#         return elem[1]
#
#
#     # ָ���ڶ���Ԫ������ ����
#     r.sort(key=takesecond, reverse=True)
#
#     for i in r:
#         if (r.index(i) % 2) == 0:
#             f.write(i[0])
#             f.write(i[1])
#
# with open('���.txt', 'r') as l:
#     qq = l.read()

from PyQt6.QtWidgets import QApplication,QWidget,QTextEdit,QVBoxLayout,QPushButton
import sys

class TextEditDemo(QWidget):
    def __init__(self,parent=None):
        super(TextEditDemo, self).__init__(parent)
        self.setWindowTitle('��������ظ��� v1.1')

        #���崰�ڵĳ�ʼ��С
        self.resize(600,400)
        #���������ı���
        self.textEdit=QTextEdit()
        #����������ť
        self.btnPress1=QPushButton('����')

        #ʵ������ֱ����
        layout=QVBoxLayout()
        #��ؿؼ���ӵ���ֱ������
        layout.addWidget(self.textEdit)
        self.textEdit.setPlaceholderText('������ճ���ڴ˴���ÿ��һ��')

        layout.addWidget(self.btnPress1)

        #���ò���
        self.setLayout(layout)

        #����ť�ĵ���ź�����صĲۺ������а󶨣����������
        self.btnPress1.clicked.connect(self.btnPress1_clicked)


    def btnPress1_clicked(self):
        #��ȡ�����ı���������
        hh = self.textEdit.toPlainText()

        a = []
        for c in hh.split('\n'):
            a.append(c)
        b = a[:]

        r = []

        for i in a:
            for k in b:
                samerate_str = "��� " + str(a.index(i)) + " " + i + "\n" + "��� " + str(b.index(k)) + " " + k + "\n"
                samerate_val = "���ƶȣ� " + str(string_similar(i, k))[0:4] + "\n\n"
                samerate = (samerate_str, samerate_val)
                if 1 > string_similar(i, k) > 0.55:
                    r.append(samerate)

        self.textEdit.clear()

        def takesecond(elem):
            return elem[1]

        # ָ���ڶ���Ԫ������ ����
        r.sort(key=takesecond, reverse=True)

        for j in r:
            if (r.index(j) % 2) == 0:
                self.textEdit.insertPlainText(j[0])
                self.textEdit.insertPlainText(j[1])


if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=TextEditDemo()
    win.show()
    sys.exit(app.exec())
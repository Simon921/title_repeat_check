# coding=gbk
import difflib

# f = open("标题.txt", mode="r", encoding='gbk')
# a = f.readlines()
# f.close()
#
# q = open("标题.txt", mode="r", encoding='gbk')
# b = q.readlines()
# q.close()


def string_similar(s1, s2):
    return difflib.SequenceMatcher(lambda x: x == '\n', s1, s2).quick_ratio()


# with open('结果.txt', "w") as f:
#     f.write('')
#
# r = []
#
# for i in a:
#     for k in b:
#         samerate_str = "序号 " + str(a.index(i)) + " " + i + "序号 " + str(b.index(k)) + " " + k
#         samerate_val = "相似度： " + str(string_similar(i, k))[0:4] + "\n\n"
#         samerate = (samerate_str, samerate_val)
#         if 1 > string_similar(i, k) > 0.55:
#             r.append(samerate)
#             print(samerate)
#
# with open('结果.txt', 'a') as f:
#     # 获取列表的第二个元素
#     def takesecond(elem):
#         return elem[1]
#
#
#     # 指定第二个元素排序 降序
#     r.sort(key=takesecond, reverse=True)
#
#     for i in r:
#         if (r.index(i) % 2) == 0:
#             f.write(i[0])
#             f.write(i[1])
#
# with open('结果.txt', 'r') as l:
#     qq = l.read()

from PyQt6.QtWidgets import QApplication,QWidget,QTextEdit,QVBoxLayout,QPushButton
import sys

class TextEditDemo(QWidget):
    def __init__(self,parent=None):
        super(TextEditDemo, self).__init__(parent)
        self.setWindowTitle('计算标题重复度 v1.1')

        #定义窗口的初始大小
        self.resize(600,400)
        #创建多行文本框
        self.textEdit=QTextEdit()
        #创建两个按钮
        self.btnPress1=QPushButton('计算')

        #实例化垂直布局
        layout=QVBoxLayout()
        #相关控件添加到垂直布局中
        layout.addWidget(self.textEdit)
        self.textEdit.setPlaceholderText('将标题粘贴在此处，每行一个')

        layout.addWidget(self.btnPress1)

        #设置布局
        self.setLayout(layout)

        #将按钮的点击信号与相关的槽函数进行绑定，点击即触发
        self.btnPress1.clicked.connect(self.btnPress1_clicked)


    def btnPress1_clicked(self):
        #获取多行文本框中内容
        hh = self.textEdit.toPlainText()

        a = []
        for c in hh.split('\n'):
            a.append(c)
        b = a[:]

        r = []

        for i in a:
            for k in b:
                samerate_str = "序号 " + str(a.index(i)) + " " + i + "\n" + "序号 " + str(b.index(k)) + " " + k + "\n"
                samerate_val = "相似度： " + str(string_similar(i, k))[0:4] + "\n\n"
                samerate = (samerate_str, samerate_val)
                if 1 > string_similar(i, k) > 0.55:
                    r.append(samerate)

        self.textEdit.clear()

        def takesecond(elem):
            return elem[1]

        # 指定第二个元素排序 降序
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
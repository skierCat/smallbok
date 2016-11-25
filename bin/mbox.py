# -*- coding: utf-8 -*-
# -*-地址处理 -*-
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
cwd=os.path.dirname(os.path.abspath("__File__"))
if cwd.find("bin")>=0:
    sys.path.append(cwd)
elif cwd.find("bin")<0:
    cwd=cwd+r"\bin"
    sys.path.append(cwd)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
import time
from bin.form01 import Ui_form01
from bin.form02 import Ui_form02
from bin.form03 import Ui_form03
from bin.form04 import Ui_form04
from bin.form05 import Ui_form05
class Ui_BoxWindow(object):
    def __init__(self):
        #全局控制变量
        self.formNum=0 #窗口加载与否变量
        self.dir=cwd  #程序主目录
    def setupUi(self, BoxWindow):
        BoxWindow.setObjectName("BoxWindow")
        BoxWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(BoxWindow)
        self.centralwidget.setObjectName("centralwidget")
        BoxWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BoxWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar") #菜单设置
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")
        self.account = QtWidgets.QMenu(self.menubar)
        self.account.setObjectName("account")
        self.engineering = QtWidgets.QMenu(self.menubar)
        self.engineering.setObjectName("engineering")
        self.help = QtWidgets.QMenu(self.menubar)
        self.help.setObjectName("help")
        BoxWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BoxWindow)
        self.statusbar.setObjectName("statusbar")
        BoxWindow.setStatusBar(self.statusbar)
        self.exit = QtWidgets.QAction(BoxWindow)
        self.exit.setObjectName("exit")
        self.accountForm = QtWidgets.QAction(BoxWindow)
        self.accountForm.setObjectName("accountForm")
        self.accountForm_2 = QtWidgets.QAction(BoxWindow)
        self.accountForm_2.setObjectName("accountForm_2")
        self.accountForm_3 = QtWidgets.QAction(BoxWindow)
        self.accountForm_3.setObjectName("accountForm_3")
        self.engineering_1 = QtWidgets.QAction(BoxWindow)
        self.engineering_1.setObjectName("engineering_1")
        self.engineering_2 = QtWidgets.QAction(BoxWindow)
        self.engineering_2.setObjectName("engineering_2")
        self.verticalLayoutPlay = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayoutPlay.setObjectName("verticalLayoutPlay")
        self.verticalLayoutPlay.setGeometry(QtCore.QRect(0, 0, 400, 80))
        
        self.file.addAction(self.exit)
        self.account.addAction(self.accountForm)
        self.account.addAction(self.accountForm_2)
        self.account.addAction(self.accountForm_3)
        self.engineering.addAction(self.engineering_1)
        self.engineering.addAction(self.engineering_2)
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.account.menuAction())
        self.menubar.addAction(self.engineering.menuAction())
        self.menubar.addAction(self.help.menuAction())
        

        self.retranslateUi(BoxWindow)
        QtCore.QMetaObject.connectSlotsByName(BoxWindow)
        
        #槽的设置
        self.exit.triggered.connect(self.Exit)      #点击退出菜单转入Exit函数
        self.accountForm.triggered.connect(self.Account)
        self.accountForm_2.triggered.connect(self.Account_two)
        self.accountForm_3.triggered.connect(self.Account_three)
        self.engineering_1.triggered.connect(self.engineering_one)
        self.engineering_2.triggered.connect(self.engineering_two)


    #汉化定义
    def retranslateUi(self, BoxWindow):
        _translate = QtCore.QCoreApplication.translate
        icon = QtGui.QIcon('myico.ico')
        BoxWindow.setWindowIcon(icon)
        BoxWindow.setWindowTitle(_translate("BoxWindow", "小魔方-作者：文强"))
        self.file.setTitle(_translate("BoxWindow", "文件"))
        self.account.setTitle(_translate("BoxWindow", "财务管理"))
        self.engineering.setTitle(_translate("BoxWindow", "工程管理"))
        self.help.setTitle(_translate("BoxWindow", "帮助"))
        self.exit.setText(_translate("BoxWindow", "退出"))
        self.accountForm.setText(_translate("BoxWindow", "银行账户管理"))
        self.accountForm_2.setText(_translate("BoxWindow", "原始凭证扫描仪"))
        self.accountForm_3.setText(_translate("BoxWindow", "工资单QQ推送器"))
        self.engineering_1.setText(_translate("BoxWindow", "放样坐标计算器"))
        self.engineering_2.setText(_translate("BoxWindow", "文档填写工具"))

        #槽链接的函数开始
    def Exit(self):#点击退出
        self.close()
    def Account(self):#加载分析窗口
        if self.formNum==0:#没有其他窗口就直接加载
            self.child=Ui_form01()
            self.verticalLayoutPlay.addWidget(self.child)
            self.child.show()
            self.formNum=1#设置有窗口变量
        else:#有窗口的话就先撤销窗口然后加载
            self.child.close()
            self.formNum=0
            self.child=Ui_form01()
            self.verticalLayoutPlay.addWidget(self.child)
            self.child.show()
            self.formNum=1
    def Account_two(self):#加载分析窗口
        if self.formNum==0:#没有其他窗口就直接加载
            self.child=Ui_form04()
            self.verticalLayoutPlay.addWidget(self.child)
            self.child.show()
            self.formNum=1#设置有窗口变量
        else:#有窗口的话就先撤销窗口然后加载
            self.child.close()
            self.formNum=0
            self.child=Ui_form04()
            self.verticalLayoutPlay.addWidget(self.child)
            self.child.show()
            self.formNum=1
    def Account_three(self):#加载分析窗口
        if self.formNum==0:#没有其他窗口就直接加载
            self.child=Ui_form05()
            self.verticalLayoutPlay.addWidget(self.child)
            self.child.show()
            self.formNum=1#设置有窗口变量
        else:#有窗口的话就先撤销窗口然后加载
            self.child.close()
            self.formNum=0
            self.child=Ui_form05()
            self.verticalLayoutPlay.addWidget(self.child)
            self.child.show()
            self.formNum=1
    def engineering_one(self):
        if self.formNum==0:#没有其他窗口就直接加载
            self.child=Ui_form02()
            self.verticalLayoutPlay.addWidget(self.child)
            self.child.show()
            self.formNum=1#设置有窗口变量
        else:#有窗口的话就先撤销窗口然后加载
            self.child.close()
            self.formNum=0
            self.child=Ui_form02()
            self.verticalLayoutPlay.addWidget(self.child)
            self.child.show()
            self.formNum=1
    def engineering_two(self):
        if self.formNum==0:#没有其他窗口就直接加载
            self.child=Ui_form03()
            self.verticalLayoutPlay.addWidget(self.child)
            self.child.show()
            self.formNum=1#设置有窗口变量
        else:#有窗口的话就先撤销窗口然后加载
            self.child.close()
            self.formNum=0
            self.child=Ui_form03()
            self.verticalLayoutPlay.addWidget(self.child)
            self.child.show()
            self.formNum=1
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BoxWindow = QtWidgets.QMainWindow()
    ui = Ui_BoxWindow()
    ui.setupUi(BoxWindow)
    BoxWindow.show()
    sys.exit(app.exec_())


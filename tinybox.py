# -*- coding: utf-8 -*-
# 启动程序
# 作者：冯文强
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QWidget
from bin.mbox import Ui_BoxWindow
from bin.sbox import Ui_Form
import time
import sys

class my_Box(QMainWindow,Ui_BoxWindow):             #继承了boxwindow的类
    def __init__(self):
        super(my_Box,self).__init__()
        self.setupUi(self)                          #加载主界面项目
        
#加载主界面项目

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    box=my_Box()
    box.show()
    sys.exit(app.exec_())


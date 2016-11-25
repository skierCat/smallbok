# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\程序设计\小魔方\界面设计\form01\form01.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
import pymysql
import time
class Ui_form01(QtWidgets.QTabWidget):#重载一个QTabWidget
    def __init__(self,master=None):
        QtWidgets.QWidget.__init__(self, master)
        self.createUI()
        #局部变量
        self.stopCameraID=0#摄像头打开关键字
        self.image=0#摄像头记录的图像
        self.items=[]#分类全局变量
        self.camera=0#摄像头选择
        self.dataconfig={}#数据库信息字典
        self.id=0#总序号，唯一关键编号
        self.tmpurl=''#系统缓存文件夹
        self.dataurl=''#系统数据文件夹
        self.configurl=''#系统配置文件夹
        self.getSetting()#初始化程序
        self.comboboxNum=0 #查看的combobox中有多少数据
        self.itemNum=0 #表格数据清除辅助变量
        self.config = self.dataconfig
    def createUI(self):
        self.setObjectName("myTab")
        
        self.cpwTab = QtWidgets.QWidget()
        self.cpwTab.setObjectName("cpwTab")
        self.hBox1_1=QtWidgets.QHBoxLayout()
        self.cpwEdit=QtWidgets.QLineEdit()
        self.cpwButton=QtWidgets.QPushButton("搜  索")
        self.hBox1_1.addWidget(self.cpwEdit)
        self.hBox1_1.addWidget(self.cpwButton)
        self.hBox1_2=QtWidgets.QHBoxLayout()
        self.cpwCombobox=QtWidgets.QComboBox()
        self.hBox1_2.addWidget(self.cpwCombobox)
        self.hBox1_3=QtWidgets.QHBoxLayout()
        self.model=QStandardItemModel(1,6)
        self.model.setHorizontalHeaderLabels(['编号','公司','账号','开户行','说明','分类'])
        self.cpwTable=QtWidgets.QTableView()
        self.cpwTable.setModel(self.model)
        self.cpwTable.horizontalHeader().setStretchLastSection(True)
        self.cpwTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.hBox1_3.addWidget(self.cpwTable)
        self.vBox1=QtWidgets.QVBoxLayout(self.cpwTab)
        self.vBox1.addLayout(self.hBox1_1)
        self.vBox1.addLayout(self.hBox1_2)
        self.vBox1.addLayout(self.hBox1_3)
        

        self.delTab = QtWidgets.QWidget()
        self.delTab.setObjectName("delTab")
        self.hBox2_1=QtWidgets.QHBoxLayout()
        self.delEdit=QtWidgets.QLineEdit()
        self.delButton=QtWidgets.QPushButton("删  除")
        self.delLabel=QtWidgets.QLabel()
        self.delLabel.setText("输入第几条数据的编号确定删除！")
        self.hBox2_1.addWidget(self.delEdit)
        self.hBox2_1.addWidget(self.delButton)
        self.hBox2_2=QtWidgets.QHBoxLayout()
        self.delLabel=QtWidgets.QLabel()
        self.delLabel.setText("先查询好账户编号，然后输入第几条数据的编号确定删除！")
        self.hBox2_2.addWidget(self.delLabel)
        self.vBox2=QtWidgets.QVBoxLayout(self.delTab)
        self.vBox2.addLayout(self.hBox2_1)
        self.vBox2.addLayout(self.hBox2_2)
        

        self.addaccountTab = QtWidgets.QWidget()
        self.addaccountTab.setObjectName("addaccountTab")
        self.hBox3_1=QtWidgets.QHBoxLayout()
        self.addcompanyLabel=QtWidgets.QLabel()
        self.addcompanyLabel.setText("公司开户名称")
        self.addcompanyEdit=QtWidgets.QLineEdit()
        self.hBox3_1.addWidget(self.addcompanyLabel)
        self.hBox3_1.addWidget(self.addcompanyEdit)
        self.hBox3_2=QtWidgets.QHBoxLayout()
        self.addaccountLabel=QtWidgets.QLabel()
        self.addaccountLabel.setText("银行账户号码")
        self.addaccountEdit=QtWidgets.QLineEdit()
        self.hBox3_2.addWidget(self.addaccountLabel)
        self.hBox3_2.addWidget(self.addaccountEdit)
        self.hBox3_3=QtWidgets.QHBoxLayout()
        self.addbankLabel=QtWidgets.QLabel()
        self.addbankLabel.setText("开户银行名称")
        self.addbankEdit=QtWidgets.QLineEdit()
        self.hBox3_3.addWidget(self.addbankLabel)
        self.hBox3_3.addWidget(self.addbankEdit)
        self.hBox3_4=QtWidgets.QHBoxLayout()
        self.addotherLabel=QtWidgets.QLabel()
        self.addotherLabel.setText("备注及说明等")
        self.addotherEdit=QtWidgets.QLineEdit()
        self.hBox3_4.addWidget(self.addotherLabel)
        self.hBox3_4.addWidget(self.addotherEdit)
        self.hBox3_5=QtWidgets.QHBoxLayout()
        self.addsaveButton=QtWidgets.QPushButton("保  存")
        self.hBox3_5.addWidget(self.addsaveButton)
        self.vBox3=QtWidgets.QVBoxLayout(self.addaccountTab)
        self.vBox3.addLayout(self.hBox3_1)
        self.vBox3.addLayout(self.hBox3_2)
        self.vBox3.addLayout(self.hBox3_3)
        self.vBox3.addLayout(self.hBox3_4)
        self.vBox3.addLayout(self.hBox3_5)

        self.addTab(self.cpwTab,"查找账户")
        self.addTab(self.delTab,"删除账户")
        self.addTab(self.addaccountTab,"添加账户")
        self.setCurrentIndex(0)
        #设置槽
        self.addsaveButton.clicked.connect(self.addAccountIn)
        self.delButton.clicked.connect(self.delAccountIn)
        self.cpwButton.clicked.connect(self.searchCompany)

    #搜索信息
    def searchCompany(self):
        if(self.itemNum!=0):
            for row in range(self.itemNum):
                for column in range(6):
                    item=QStandardItem('')
                    self.model.setItem(row,column,item)
        self.itemNum=0
        if(self.comboboxNum!=0):
            for i in range(self.comboboxNum):
                self.cpwCombobox.removeItem(i)
        keyword=self.cpwEdit.text().strip()
        conn = pymysql.connect(**self.config)
        if (keyword!=''):
            try:
                    with conn.cursor() as cur:
                        word="select * from bankinfor where company like '%"+ keyword +"%' or otherinfor like '%"+ keyword +"%'"
                        cur.execute(word)
                        table=cur.fetchall()
                        for i in range(len(table)):
                            self.itemNum=self.itemNum+1
                            self.cpwCombobox.addItem("第"+str(table[i][0])+"数据")
                            self.comboboxNum=self.comboboxNum+1
                            for row in range(len(table)):
                                for column in range(6):
                                    item=QStandardItem(str(table[row][column]))
                                    self.model.setItem(row,column,item)
                        conn.commit()
                        
            finally:
                    self.cpwEdit.setText('')
                    cur.close()
                    conn.close()
        else:
            self.cpwEdit.setText('')
            conn.close()
            
    #添加账户信息
    def addAccountIn(self):
        company=self.addcompanyEdit.text().strip()
        banknum=self.addaccountEdit.text().strip()
        bank=self.addbankEdit.text().strip()
        otherinfor=self.addotherEdit.text().strip()
        typenum=1
        conn = pymysql.connect(**self.config)
        if(company !='' and banknum!='' and bank!=''):
            try:
                with conn.cursor() as cur:
                    word="INSERT INTO bankinfor (id, company, account, bank, otherinfor, type) VALUES ('', '%s', '%s', '%s', '%s', '%s')" % (company,banknum,bank,otherinfor,typenum)
                    cur.execute(word)
                    conn.commit()
                    
            finally:
                self.addcompanyEdit.setText('')
                self.addaccountEdit.setText('')
                self.addbankEdit.setText('')
                self.addotherEdit.setText('')
                cur.close()
                conn.close()
        else:
            self.addcompanyEdit.setText('')
            self.addaccountEdit.setText('')
            self.addbankEdit.setText('')
            self.addotherEdit.setText('')
            cur.close()
            conn.close()

    #删除账户信息
    def delAccountIn(self):
        numid=self.delEdit.text().strip()
        conn = pymysql.connect(**self.config)
        word="select id from bankinfor where id=%s" % (str(numid))
        try:
            with conn.cursor() as cur:
                    check=cur.execute(word)
                    if(check==1):
                        word="DELETE FROM bankinfor where id=%d" % (int(numid))
                        cur.execute(word)
                        self.delLabel.setText("删除成功！")
                    else:self.delLabel.setText("删除失败！")
                    conn.commit();
        finally:
            self.delEdit.setText('')
            cur.close()
            conn.close()
        
    def getSetting(self):
        #初始化路径
        fp=open('lib/config.wenq')
        text=fp.readlines()
        self.tmpurl=text[1].strip('\n')
        self.dataurl=text[2].strip('\n')
        self.configurl=text[0].strip('\n')
        fp.close()
        #初始化数据库
        fp=open(self.configurl+'database.wenq')
        text=fp.readlines()
        self.dataconfig={
          'host':text[0].strip('\n'),
          'port':int(text[1].strip('\n')),
          'user':text[2].strip('\n'),
          'password':text[3].strip('\n'),
          'db':text[4].strip('\n'),
          'charset':text[5].strip('\n'),
          }
        fp.close()
    
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    player = Ui_form01()
    player.show()
    player.resize(720,450)
    if sys.argv[1:]:
        player.OpenFile(sys.argv[1])
    sys.exit(app.exec_())

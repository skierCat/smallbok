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
import xlrd
import win32com
from win32com.client import Dispatch
import time
import threading
import multiprocessing

class Ui_form03(QtWidgets.QTabWidget):#重载一个QTabWidget
    def __init__(self,master=None):
        QtWidgets.QWidget.__init__(self, master)
        self.createUI()
        #局部变量
        self.sheet=0 #工作表
        self.keyNum=0 #替换的个数
        self.row=[] #列
        self.replaceWord=[]
        self.mFilename='' #全局变量word文件名
        self.saveAs_head=1
        self.saveAs_point=1
        self.progressPercent=0 #进度条百分百
    def createUI(self):
        self.setObjectName("myTab")
        self.cpwTab = QtWidgets.QWidget()
        self.cpwTab.setObjectName("cpwTab")
        self.hBox1_1=QtWidgets.QHBoxLayout()
        self.excelButton=QtWidgets.QPushButton("读入表格")
        self.wordButton=QtWidgets.QPushButton("读入模板")
        self.startButton=QtWidgets.QPushButton("开始生成")
        self.hBox1_1.addWidget(self.excelButton)
        self.hBox1_1.addWidget(self.wordButton)
        self.hBox1_1.addWidget(self.startButton)
        self.hBox1_2=QtWidgets.QHBoxLayout()
        self.progressBar=QtWidgets.QProgressBar()
        self.progressBar.setStyleSheet("margin-top:10px;height:5px;")
        self.progressBar.setTextVisible(False)
        self.progressBar.setValue(0)
        self.hBox1_2.addWidget(self.progressBar)
        self.hBox1_3=QtWidgets.QHBoxLayout()
        
        self.cpwTable=QtWidgets.QTableView()
        
        self.cpwTable.horizontalHeader().setStretchLastSection(True)
        self.cpwTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.hBox1_3.addWidget(self.cpwTable)
        self.hBox1_4=QtWidgets.QHBoxLayout()
        self.statusLabel=QtWidgets.QLabel()
        self.statusLabel.setStyleSheet("background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);font-size:10px;padding-left:15px;padding-top:15px;padding-bottom:15px;")
        self.statusLabel.setText("即将显示生成情况。。。。。。")
        self.hBox1_4.addWidget(self.statusLabel)
        self.vBox1=QtWidgets.QVBoxLayout(self.cpwTab)
        self.vBox1.addLayout(self.hBox1_1)
        self.vBox1.addLayout(self.hBox1_2)
        self.vBox1.addLayout(self.hBox1_3)
        self.vBox1.addLayout(self.hBox1_4)
        

        self.delTab = QtWidgets.QWidget()
        self.delTab.setObjectName("delTab")
        self.hBox1=QtWidgets.QHBoxLayout()
        self.label_1=QtWidgets.QLabel()
        self.label_1.setText("一级文件名起始数值：")
        self.line_1=QtWidgets.QLineEdit()
        self.label_2=QtWidgets.QLabel()
        self.label_2.setText("二级文件名变化系数：")
        self.line_2=QtWidgets.QLineEdit()
        self.hBox1.addWidget(self.label_1)
        self.hBox1.addWidget(self.line_1)
        self.hBox1.addWidget(self.label_2)
        self.hBox1.addWidget(self.line_2)

        self.hBox3=QtWidgets.QHBoxLayout()
        self.label_3=QtWidgets.QLabel()
        self.label_3.setText("替换第几个工作表：")
        self.line_3=QtWidgets.QLineEdit()
        self.hBox3.addWidget(self.label_3)
        self.hBox3.addWidget(self.line_3)
        
        
        self.hBox2=QtWidgets.QHBoxLayout()
        self.addButton=QtWidgets.QPushButton("添  加")
        self.sendButton=QtWidgets.QPushButton("设  置")
        self.hBox2.addWidget(self.addButton)
        self.hBox2.addWidget(self.sendButton)
        self.vBox2=QtWidgets.QVBoxLayout(self.delTab)
        self.vBox2.addLayout(self.hBox2)
        self.vBox2.addLayout(self.hBox1)
        self.vBox2.addLayout(self.hBox3)
        
        

        self.addTab(self.cpwTab,"文件生成")
        self.addTab(self.delTab,"设置")
        self.setCurrentIndex(1)
        #设置槽
        self.excelButton.clicked.connect(self.readExcel)
        self.wordButton.clicked.connect(self.readWord)
        self.startButton.clicked.connect(self.start)
        self.addButton.clicked.connect(self.addnew)
        self.sendButton.clicked.connect(self.setting)

    #保存设置
    def setting(self):
        self.saveAs_head=int(self.line_1.text())
        self.saveAs_point=int(self.line_2.text())
        self.sheet=int(self.line_3.text())-1
        for i in range(self.keyNum):
            self.row.append(str(globals()['self.line_'+str(i+1)+'_2'].text()))
            self.replaceWord.append(str(globals()['self.line_'+str(i+1)+'_1'].text()))

    #读入excel表格
    def readExcel(self):
        self.statusLabel.setText("正在读取Excel文件。。。。。。")
        getfile = QFileDialog.getOpenFileName(self,"选取数据文件","")
        if(getfile[0]!=''):
            self.excelData=xlrd.open_workbook(getfile[0])  #全局变量excel数据
            table=self.excelData.sheets()[self.sheet]
            rows=table.nrows
            cols=table.ncols
            self.model=QStandardItemModel(rows,cols)
            self.cpwTable.setModel(self.model)
            for i in range(rows):
                for j in range(cols):
                    item=QStandardItem(str(table.cell(i,j).value))
                    self.model.setItem(i,j,item)
    
    def readWord(self):
        self.statusLabel.setText("正在读取Word模板文件。。。。。。")
        getfile = QFileDialog.getOpenFileName(self,"选取模板文件","")
        if(getfile[0]!=''):
            self.mFilename=getfile[0] #全局变量word文件名

    def start(self):
        start = threading.Thread(target = self.process_start)
        progress =threading.Thread(target = self.process_change)
        start.start()
        progress.start()
        
    def process_change(self):
        count=0
        while count < 99:
            if(count>99):count=99
            self.progressBar.setValue(count)
            count=self.progressPercent
            time.sleep(1)
        self.progressBar.setValue(99)
        

    def process_start(self):
        myData=[]
        name=1
        if(self.sheet!='' and len(self.row)!=0 and len(self.replaceWord)!=0 and len(self.excelData.sheets())!=0 and self.mFilename!=''):
            table=self.excelData.sheets()[self.sheet]
            for i in range(len(self.row)):
                myData.append(table.col_values(i))
            app=Dispatch('Word.Application')
            app.Visible=False
            app.ScreenUpdating=False
            for tmp in range(len(myData[0])):
                lenth=len(myData[0])
                doc=app.Documents.Open(self.mFilename)
                if(name==self.saveAs_point):
                    name=1
                    self.saveAs_head=self.saveAs_head+1
                myfilename=str(os.getcwd())+'/tmp/'+str(self.saveAs_head)+'_'+str(name)+'.doc'
                for i in range(len(self.replaceWord)):
                    for j in range(len(self.row)):
                        if (i==j):
                            app.Selection.Find.Execute(str(self.replaceWord[i]),False,False,False,False,False,True,1,True,str(myData[j][tmp]),2)
                            self.statusLabel.setText("正在将"+str(self.replaceWord[i]+'替换为'+str(myData[j][tmp])))
                doc.SaveAs(myfilename)
                doc.Close()
                name=name+1
                self.progressPercent=int((tmp+1)/lenth*100)
                time.sleep(1)
                self.statusLabel.setText("正在保存文件:"+str(myfilename))
            self.statusLabel.setText("完成！！！！！！！")
            app.Quit()
            
    #添加新的设置
    def addnew(self):
        self.keyNum=self.keyNum+1
        globals()['self.hBox2_'+str(self.keyNum)]=QtWidgets.QHBoxLayout()
        globals()['self.label_'+str(self.keyNum)+'_1']=QtWidgets.QLabel()
        globals()['self.label_'+str(self.keyNum)+'_1'].setText("关键字"+str(self.keyNum)+"：")
        globals()['self.line_'+str(self.keyNum)+'_1']=QtWidgets.QLineEdit()
        globals()['self.label_'+str(self.keyNum)+'_2']=QtWidgets.QLabel()
        globals()['self.label_'+str(self.keyNum)+'_2'].setText("替换数据列数：")
        globals()['self.line_'+str(self.keyNum)+'_2']=QtWidgets.QLineEdit()
        globals()['self.hBox2_'+str(self.keyNum)].addWidget(globals()['self.label_'+str(self.keyNum)+'_1'])
        globals()['self.hBox2_'+str(self.keyNum)].addWidget(globals()['self.line_'+str(self.keyNum)+'_1'])
        globals()['self.hBox2_'+str(self.keyNum)].addWidget(globals()['self.label_'+str(self.keyNum)+'_2'])
        globals()['self.hBox2_'+str(self.keyNum)].addWidget(globals()['self.line_'+str(self.keyNum)+'_2'])
        self.vBox2.addLayout(globals()['self.hBox2_'+str(self.keyNum)])
        
                
                
                
            
            
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    player = Ui_form03()
    player.show()
    player.resize(720,450)
    if sys.argv[1:]:
        player.OpenFile(sys.argv[1])
    sys.exit(app.exec_())

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
import cmath
import random
import math
class Ui_form02(QtWidgets.QTabWidget):#重载一个QTabWidget
    def __init__(self,master=None):
        QtWidgets.QWidget.__init__(self, master)
        self.createUI()
        #局部变量
        self.itemNum=0 #表格数据清除辅助变量
        self.myData=[]
    def createUI(self):
        self.setObjectName("myTab")
        
        self.cpwTab = QtWidgets.QWidget()
        self.cpwTab.setObjectName("cpwTab")
        self.hBox1_1=QtWidgets.QHBoxLayout()
        self.cpwButton_js=QtWidgets.QPushButton("计   算")
        self.cpwButton_hy=QtWidgets.QPushButton("核   验")
        self.hBox1_1.addWidget(self.cpwButton_js)
        self.hBox1_1.addWidget(self.cpwButton_hy)
        self.hBox1_3=QtWidgets.QHBoxLayout()
        self.model=QStandardItemModel(9,9)
        self.model.setHorizontalHeaderLabels(['X坐标（设计）','Y坐标（设计）','X生成','Y生成','距离','角度','△X','△Y','偏移'])
        self.model.setVerticalHeaderLabels(['测站点','后视点','检查点','放样点1','放样点2','放样点3','放样点4','放样点5','放样点6'])
        self.cpwTable=QtWidgets.QTableView()
        self.cpwTable.setModel(self.model)
        self.cpwTable.horizontalHeader().setStretchLastSection(True)
        self.cpwTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.hBox1_3.addWidget(self.cpwTable)
        self.vBox1=QtWidgets.QVBoxLayout(self.cpwTab)
        self.vBox1.addLayout(self.hBox1_1)
        self.vBox1.addLayout(self.hBox1_3)
        
        self.addTab(self.cpwTab,"放样信息计算表")
        self.setCurrentIndex(0)
        #设置槽
        self.cpwButton_js.clicked.connect(self.jisuan)
        self.cpwButton_hy.clicked.connect(self.jisuan)

    #信息
    def jisuan(self):
        #初始数据
        base_x=0
        base_y=0
        #首先循环获得所有数据
        for i in range(9):
            for j in range(9):
                index=self.model.index(i,j)
                self.myData.append(self.model.data(index))
        #基准坐标
        if (self.myData[0]!=None and self.myData[1]!=None):
            base_x=float(self.myData[0])
            base_y=float(self.myData[1])
        if(base_x!=0 and base_y!=0):
            #然后把数据进行加工
            for i in range(9):
                if ((i==1 or i==2) and self.myData[i*9]!=None and self.myData[i*9+1]!=None and self.myData[i*9]!='' and self.myData[i*9+1]!=''):#第二行和第三行处理
                    rel_x=float(self.myData[i*9])
                    rel_y=float(self.myData[i*9+1])
                    c_x=rel_x-base_x
                    c_y=rel_y-base_y
                    distance=cmath.polar(complex(c_x,c_y))
                    self.myData[i*9+4]=distance[0]
                    if(distance[1]>=0):
                        temp=distance[1]*180/math.pi
                        d=int(temp)
                        f=int((temp-d)*60)
                        m=round(float(((temp-d)*60-f)*60),2)
                        print('测试')
                        self.myData[i*9+5]=str(d)+'°'+str(f)+'′'+str(m)+'″'
                    elif(distance[1]<0):
                        temp=360+distance[1]*180/math.pi
                        d=int(temp)
                        f=int((temp-d)*60)
                        m=round(float(((temp-d)*60-f)*60),2)
                        self.myData[i*9+5]=str(d)+'°'+str(f)+'′'+str(m)+'″'
                if ((i>2) and self.myData[i*9]!=None and self.myData[i*9+1]!=None and self.myData[i*9]!='' and self.myData[i*9+1]!=''):#三行后处理且每行前两个不为空
                    d_x=random.randint(-2, 2)
                    d_y=random.randint(-2, 2)
                    rel_x=round(float(self.myData[i*9])+d_x/1000,3)
                    rel_y=round(float(self.myData[i*9+1])+d_y/1000,3)
                    c_x=rel_x-base_x
                    c_y=rel_y-base_y
                    distance=cmath.polar(complex(c_x,c_y))
                    self.myData[i*9+2]=rel_x
                    self.myData[i*9+3]=rel_y
                    self.myData[i*9+4]=distance[0]
                    self.myData[i*9+6]=math.fabs(d_x)
                    self.myData[i*9+7]=math.fabs(d_y)
                    self.myData[i*9+8]=round(math.sqrt(float(d_x*d_x+d_y*d_y)),1)
                    if(distance[1]>=0):
                        temp=distance[1]*180/math.pi
                        d=int(temp)
                        f=int((temp-d)*60)
                        m=round(((temp-d)*60-f)*60,2)
                        self.myData[i*9+5]=str(d)+'°'+str(f)+'′'+str(m)+'″'
                    elif(distance[1]<0):
                        temp=360+distance[1]*180/math.pi
                        d=int(temp)
                        f=int((temp-d)*60)
                        m=round(((temp-d)*60-f)*60,2)
                        self.myData[i*9+5]=str(d)+'°'+str(f)+'′'+str(m)+'″'
            #将数据写入表格中
            for i in range(9):
                for j in range(9):
                    if(self.myData[i*9+j]==None):
                        self.myData[i*9+j]=''
                    item=QStandardItem(str(self.myData[i*9+j]))
                    self.model.setItem(i,j,item)
            #释放数据
            self.myData=[]
        else:
            for i in range(9):
                for j in range(9):
                    item=QStandardItem('基准出错')
                    self.model.setItem(i,j,item)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    player = Ui_form02()
    player.show()
    player.resize(720,450)
    if sys.argv[1:]:
        player.OpenFile(sys.argv[1])
    sys.exit(app.exec_())

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
from bin.qqbot import QQBot
import xlrd
import threading

class MyQQBot(QQBot):
    def __init__(self,sendgzdpass):
        self.sendpass=sendgzdpass
    def onPollComplete(self, msgType, from_uin, buddy_uin, message):
        if message == '-hello':
            self.send(msgType, from_uin, '你好，我是QQ机器人')
        elif message == '-stop':
            self.stopped = True
            self.send(msgType, from_uin, 'QQ机器人已关闭')
        if message == self.sendpass:
            self.send(msgType, from_uin, '你好，QQ机器人即将为您推送Excel工资单！')
            excelfile=''
            if (os.path.isfile('tmp/'+self.sendpass[1:]+'.xls')):
                excelfile='tmp/'+self.sendpass[1:]+'.xls'
            elif (os.path.isfile('tmp/'+self.sendpass[1:]+'.xlsx')):
                excelfile='tmp/'+self.sendpass[1:]+'.xlsx'
            if(excelfile!=''):
                qqRowid=0
                qqColid=0
                data = xlrd.open_workbook(excelfile)
                table = data.sheets()[0]
                title=table.row_values(0)
                for i in range(len(title)):
                    if(isinstance(title[i],float)==True):
                       title[i]=''.join(str(title[i]).split())
                    else:
                        title[i]=''.join(title[i].split())
                    if (title[i]=='QQ' or title[i]=='qq'):
                        qqRowid=i
                        print('qq所在列：'+str(qqRowid))
                from_qq=self.buddiesDictU[from_uin]['qq']
                print('当前的qq号：')
                qq_list=table.col_values(qqRowid)
                for i in range(len(qq_list)):
                    if(isinstance(qq_list[i],float)==True):
                       qq_list[i]=''.join(str(qq_list[i]).split())
                    else:
                        qq_list[i]=''.join(qq_list[i].split())
                    if (qq_list[i]!='' and len(qq_list[i])>=5):
                        qqColid=i
                        qqnum=int(qq_list[i])
                        qquin=self.buddiesDictQ[qqnum]['uin']
                        print(str(qqnum)+'所在行：'+str(qqColid))
                        gzd_data=table.row_values(qqColid)
                        mymsg=''
                        for i in range(len(gzd_data)):
                            if(isinstance(gzd_data[i],float)==True):
                               gzd_data[i]=''.join(str(gzd_data[i]).split())
                            else:
                                gzd_data[i]=''.join(gzd_data[i].split())
                            if (gzd_data[i]!='' and i!=qqRowid):
                                mymsg=mymsg+title[i]+'：'+gzd_data[i]+'\n'
                        self.send(msgType, qquin, mymsg)
                        gzd_data=[]
                qq_list=[]
                title=[]

class Ui_form05(QtWidgets.QTabWidget):#重载一个QTabWidget
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
        self.cpwButton=QtWidgets.QPushButton("设置口令并开启服务器")
        self.hBox1_1.addWidget(self.cpwEdit)
        self.hBox1_1.addWidget(self.cpwButton)

        self.hBox1_2=QtWidgets.QHBoxLayout()
        self.myLabel=QtWidgets.QLabel()
        self.myLabel.setText("请将需要推送的Excel文件请放程序所在目录下的tmp目录中，然后输入-加文件名作为口令！！")
        self.hBox1_2.addWidget(self.myLabel)
        
        self.vBox1=QtWidgets.QVBoxLayout(self.cpwTab)
        self.vBox1.addLayout(self.hBox1_1)
        self.vBox1.addLayout(self.hBox1_2)
        self.addTab(self.cpwTab,"工资发送服务器")
        self.setCurrentIndex(0)
        #设置槽
        self.cpwButton.clicked.connect(self.start)

    def start(self):
        s = threading.Thread(target = self.startServer)
        p = threading.Thread(target = self.updateUi)
        status = threading.Thread(target = self.scanStatus)
        s.start()
        p.start()
        status.start()

    #QQ机器人服务
    def startServer(self):
        password=self.cpwEdit.text().strip()
        myqqbot = MyQQBot(password)
        myqqbot.Login()
        myqqbot.Run()
    #状态检测线程
    def scanStatus(self):
        TmpDir = os.path.join(os.path.expanduser('~'), '.qqbot-tmp')
        while True:
            if os.path.exists(TmpDir):
                tmpFile=open(TmpDir+'/loginstatas.wenq','r')
                texto=tmpFile.read()
                tmpFile.close()
                time.sleep(25)
                tmpFile=open(TmpDir+'/loginstatas.wenq','r')
                textn=tmpFile.read()
                tmpFile.close()
                if(texto==textn):
                    tmpFile=open(TmpDir+'/loginstatas.wenq','w')
                    tmpFile.write("当前状态：所有任务完成，等待指令中！！")
                    tmpFile.close()
            time.sleep(3)

    #更新UI线程
    def updateUi(self):
        TmpDir = os.path.join(os.path.expanduser('~'), '.qqbot-tmp')
        while True:
            if os.path.exists(TmpDir):
                tmpFile=open(TmpDir+'/loginstatas.wenq','r')
                text=tmpFile.read()
                self.myLabel.setText(text)
                tmpFile.close()
            time.sleep(3)
         
        
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
    player = Ui_form05()
    player.show()
    player.resize(720,450)
    if sys.argv[1:]:
        player.OpenFile(sys.argv[1])
    sys.exit(app.exec_())

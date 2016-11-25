# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\1.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import cv2
import os
import sys
import pymysql
import threading
import time
import zipfile


class Ui_form04(QtWidgets.QTabWidget):#重载一个QTabWidget
    def __init__(self,master=None):
        QtWidgets.QWidget.__init__(self, master)
        self.setupUi()
    def setupUi(self):
        self.setObjectName("myTab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMaximumSize(QtCore.QSize(80, 60))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.dateEdit = QtWidgets.QDateEdit(self.tab)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.horizontalLayout_8.addWidget(self.dateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setMaximumSize(QtCore.QSize(80, 60))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_7.addWidget(self.lineEdit_2, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setMaximumSize(QtCore.QSize(80, 60))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_6.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setMaximumSize(QtCore.QSize(80, 60))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_14.addLayout(self.horizontalLayout)
        self.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_5.addWidget(self.lineEdit_3, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_5.addWidget(self.pushButton_3)
        self.horizontalLayout_10.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_4.addWidget(self.comboBox_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_15.addLayout(self.verticalLayout_3)
        self.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_12.addWidget(self.label_8)
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_12.addWidget(self.comboBox_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_12.addWidget(self.pushButton_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.tab_3)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_2.setDate(QtCore.QDate.currentDate())
        self.horizontalLayout_11.addWidget(self.dateEdit_2)
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.dateEdit_3 = QtWidgets.QDateEdit(self.tab_3)
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.dateEdit_3.setDate(QtCore.QDate.currentDate())
        self.horizontalLayout_11.addWidget(self.dateEdit_3)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_11.addWidget(self.pushButton_6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.addTab(self.tab_3, "")


        self.lineEdit_2.setStyleSheet("width:295px;")
        self.lineEdit.setStyleSheet("width:295px;")
        self.dateEdit.setStyleSheet("width:305px;")
        self.comboBox.setStyleSheet("width:295px;")

        self.setCurrentIndex(0)
        self.retranslateUi()
        #全局常量
        self.stopCameraID=0#摄像头打开关键字
        self.image=0#摄像头记录的图像
        self.items=[]#分类全局变量
        self.camera=0#摄像头选择
        self.dataconfig={}#数据库信息字典
        self.id=0#总序号，唯一关键编号
        self.searchId=0#当前搜索记录在库中的序号
        self.searchDate=time.ctime()#当前搜索记录在库中的时间
        self.searchData=()#搜索记录
        self.tmpurl=''#系统缓存文件夹
        self.dataurl=''#系统数据文件夹
        self.configurl=''#系统配置文件夹
        self.getSetting()#初始化程序
        self.pushButton_2.clicked.connect(self.upDateUI)
        self.pushButton.clicked.connect(self.saveData)
        self.pushButton_3.clicked.connect(self.searchStart)
        self.pushButton_4.clicked.connect(self.searchResult)
        self.pushButton_5.clicked.connect(self.output)
        self.pushButton_6.clicked.connect(self.output)
        self.comboBox_2.currentIndexChanged.connect(self.setCurrent)

        
    def retranslateUi(self):
        self.label.setText("日  期")
        self.label_2.setText("凭证号")
        self.label_3.setText("分  类")
        self.label_4.setText("说  明")
        self.pushButton_2.setText("启    动")
        self.pushButton.setText("保    存")
        self.setTabText(self.indexOf(self.tab),"扫描原始凭证")
        self.lineEdit_3.setText("输入关键字")
        self.pushButton_3.setText("搜  索")
        self.pushButton_4.setText("查  看")
        self.setTabText(self.indexOf(self.tab_2),"检索原始凭证")
        self.label_8.setText("按分类导出")
        self.pushButton_5.setText("导    出")
        self.label_9.setText("按时间导出")
        self.label_10.setText("到")
        self.pushButton_6.setText("导    出")
        self.setTabText(self.indexOf(self.tab_3),"批量导出")

    #判断字符串是否是时间   
    def is_str_time(self,string):
        try:
            time.strptime(string,"%Y-%m-%d")
            return True
        except:
            return False
    #选择不同搜索结果时保存数据用
    def setCurrent(self):
        text=self.comboBox_2.currentText()
        if(len(self.searchData)!=0):
            for i in range(len(self.searchData)):
                if(text==str(self.searchData[i][0])+'、'+str(self.searchData[i][1].strftime('%m'))+'月'+self.searchData[i][2]+self.searchData[i][3]):
                    self.searchId=self.searchData[i][0]
                    self.searchDate=self.searchData[i][1]
                    

    def upDateUI(self):
        start = threading.Thread(target = self.video)
        start.start()

    def saveData(self):
        save = threading.Thread(target = self.saveall)
        save.start()

    def saveall(self):
        self.stopCameraID=0
        date=self.dateEdit.text()
        pznum=self.lineEdit_2.text()
        typename=self.comboBox.currentText()
        des=self.lineEdit.text()
        img=self.image
        dtype=img.dtype
        shape=''
        for i in img.shape:
            shape=shape+str(i)+'-'
        shape=shape.rstrip('-')
        filename=str(date.split('-')[1])+'月'+pznum+'-'+str(self.id)+'.bin'
        mydir=self.dataurl
        if(pznum!='' and len(img)>50):
            conn = pymysql.connect(**self.dataconfig)
            with conn.cursor() as cur:
                word="insert into yspz_image (id,date,pznum,type,dtype,shape,des,dir) values ('"+str(self.id)+"', '"+date+"', '"+pznum+"', '"+typename+"','"+str(dtype)+"','"+shape+"', '"+des+"', '"+mydir+filename+"'); "
                cur.execute(word)
                conn.commit()
                cur.close()
                conn.close()
                img.tofile(mydir+filename)
                #保存总序号
                self.id=self.id+1
                fp=open(self.configurl+'id.wenq','w')
                fp.write(str(self.id))
                fp.close()
        
    def searchStart(self):
        #每次搜索清空下拉框
        while(self.comboBox_2.currentText()!=''):
            self.comboBox_2.removeItem(0)
        key=self.lineEdit_3.text().strip(' ')
        if (key.isdigit()):
            word="select * from yspz_image where id='"+key+"';"
        elif (self.is_str_time(key)==True):
            word="select * from yspz_image where date='"+key+"';"
        else:
            word="select * from yspz_image where pznum='"+key+"' or type='"+key+"' or des like'%"+key+"%' or des like'"+key+"*' or des like'*"+key+"';"
        if(key!=''):
            conn = pymysql.connect(**self.dataconfig)
            with conn.cursor() as cur:
                cur.execute(word)
                self.searchData=cur.fetchall()
                conn.commit()
                cur.close()
                conn.close()
        if(len(self.searchData)!=0):
            for i in range(len(self.searchData)):
                self.comboBox_2.addItem(str(self.searchData[i][0])+'、'+str(self.searchData[i][1].strftime('%m'))+'月'+self.searchData[i][2]+self.searchData[i][3])
                
    def searchResult(self):
        word="select * from yspz_image where id='"+str(self.searchId)+"' and date='"+str(self.searchDate)+"';"
        if(self.searchId!=0):
            conn = pymysql.connect(**self.dataconfig)
            with conn.cursor() as cur:
                cur.execute(word)
                data=cur.fetchall()
                conn.commit()
                cur.close()
                conn.close()
                url=data[0][7]
                q=[]
                for i in data[0][5].split('-'):
                   q.append(int(i))
                tmp=tuple(q)
                im=np.fromfile(url,dtype=data[0][4])
                im.shape=tmp
                cv2.imwrite('tmp.png',im)
                tmp_img=QtGui.QPixmap('tmp.png')
                self.label_7.setPixmap(tmp_img)

    #批量导出函数
    def output(self):
        im_Name=[]
        url=[]
        typename=self.comboBox_3.currentText()
        date_s=self.dateEdit_2.text()
        date_e=self.dateEdit_3.text()
        if (typename!='' and date_s<=date_e):
            word="select * from yspz_image where type='"+typename+"' and date<='"+str(date_e)+"' and date>='"+str(date_s)+"';"
            conn = pymysql.connect(**self.dataconfig)
            with conn.cursor() as cur:
                cur.execute(word)
                data=cur.fetchall()
                conn.commit()
                cur.close()
                conn.close()
            for i in range(len(data)):
                q=[]
                tmp=()
                imgname=self.tmpurl+str(data[i][1].strftime('%m'))+'月'+data[i][2]+data[i][3]+'-'+str(data[i][0])+'.jpg'
                tmpurl=data[i][7]
                im_Name.append(imgname)
                url.append(tmpurl)
                for i in data[0][5].split('-'):
                   q.append(int(i))
                tmp=tuple(q)
                im=np.fromfile(tmpurl,dtype=data[0][4])
                im.shape=tmp
                cv2.imwrite(self.tmpurl+'tmp.jpg',im)
                os.rename(self.tmpurl+'tmp.jpg',imgname)
                del tmp
                im=[]
            myzip=zipfile.ZipFile(self.tmpurl+str(date_s)+'-'+str(date_e)+typename+'.zip', 'w' ,zipfile.ZIP_DEFLATED)
            for i in range(len(im_Name)):
                myzip.write(im_Name[i])
            myzip.close()
            for i in im_Name:
                os.remove(i)
                  
        
        
    def video(self):
        cap = cv2.VideoCapture(self.camera) # 从摄像头中取得视频
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
        self.stopCameraID=1
        while(cap.isOpened() and self.stopCameraID==1):
          #读取帧摄像头
          ret, frame = cap.read()
          if ret == True:
            #输出当前帧
            cv2.imwrite('tmp.png',frame)
            self.image=frame
            tmp_img=QtGui.QPixmap('tmp.png')
            self.label_5.setStyleSheet("width:"+str(width)+";height:"+str(height)+";")
            self.label_5.setPixmap(tmp_img)
            #键盘按 Q 退出
            if (cv2.waitKey(1) & 0xFF) == ord('q'):
              break
          else:
            break
        # 释放资源
        cap.release()
    def getSetting(self):
        #初始化路径
        fp=open('lib/config.wenq')
        text=fp.readlines()
        self.tmpurl=text[1].strip('\n')
        self.dataurl=text[2].strip('\n')
        self.configurl=text[0].strip('\n')
        fp.close()
        #初始化分类
        fp=open(self.configurl+'typeforpz.wenq')
        text=fp.readlines()
        for i in range(len(text)):
            self.items.append(text[i].strip('\n'))
        fp.close()
        for i in range(len(self.items)):
            self.comboBox.addItem(self.items[i])
            self.comboBox_3.addItem(self.items[i])
        #初始化摄像头
        fp=open(self.configurl+'camera.wenq')
        text=fp.readlines()
        for i in range(len(text)):
            self.camera=int((text[i].strip('\n')))
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
        #初始化总序号
        fp=open(self.configurl+'id.wenq')
        text=fp.readlines()
        self.id=int(text[0].strip('\n'))
        fp.close()
        
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    player = Ui_form04()
    player.show()
    player.resize(720,450)
    if sys.argv[1:]:
        player.OpenFile(sys.argv[1])
    sys.exit(app.exec_())


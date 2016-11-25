# -*- coding:utf-8 -*-
'''
Author: Bu Kun
E-mail: bukun#osgeo.cn
CopyRight: http://www.yunsuan.org
Bu Kun's Homepage: http://bukun.net
'''
"""
the url structure of website
"""
import tornado.web
from methods.db import myDb
import numpy as np
import cv2
import os
import hashlib
import time
import random

class HomeHandler(tornado.web.RequestHandler):
    #判断字符串是否是时间   
    def is_str_time(self,string):
        try:
            time.strptime(string,"%Y-%m-%d")
            return True
        except:
            return False
    def get(self):
        tmp_name='tmp/'+str(time.time())+'.png'
        tmp_binname='static/tmp/'+str(time.time())+'.png'
        imurl=""
        imcode="<img src="+imurl+">"
        sid=self.get_argument('id',"")
        sdate=self.get_argument('date',"")
        otmp_name=self.get_argument('tmp',"")
        if(otmp_name!=""):
            os.remove(otmp_name)
        if (sid!="" and sdate!=""):
            getdata=myDb()
            word="select * from yspz_image where id='"+sid+"' and date='"+sdate+"';"
            data=getdata.getData(word)
            if(len(data)==1):
                binurl="./../"+data[0][7]
                q=[]
                for i in data[0][5].split('-'):
                   q.append(int(i))
                tmp=tuple(q)
                im=np.fromfile(binurl,dtype=data[0][4])
                im.shape=tmp
                cv2.imwrite(tmp_binname,im)
                imurl=tmp_name
        imcode="<img id='imstyle' src='"+self.static_url(imurl)+"' >" 
        self.render("index.html",imagecode=imcode,converturl="")
    def post(self):
        keywordtosearch = self.get_argument("keyword")
        password = self.get_argument("keypass")
        myhash=hashlib.md5(str(password).strip(' ').encode('utf8'))
        word="select * from keytosee where password='"+myhash.hexdigest()+"';"
        getdata=myDb()
        dbpass=getdata.getData(word)
        if (len(dbpass)!=0 and dbpass[0][0]==myhash.hexdigest()):
            olddate=str(dbpass[0][1])
            newdate=str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
            if (olddate!=newdate):
                word="delete from keytosee;"
                isdel=getdata.delData(word)
                if(isdel):
                    rnum=random.randint(1000, 9999)
                    newpass=hashlib.md5(str(rnum).encode('utf8'))
                    word="insert into keytosee (password,date) values ('"+newpass.hexdigest()+"','"+str(newdate)+"');"
                    if(getdata.insertData(word)):
                        fp=open('./../lib/yzm.wenq','w')
                        fp.write(str(rnum))
                        fp.close()
                        self.render("index.html")
                    newdate=""
                    newpass=""
                    getdata.closeData()
            elif(olddate==newdate):
                imurl=""
                imcode="<img src="+imurl+">"
                wurl=""
                if(keywordtosearch!=''):
                    if (keywordtosearch.isdigit()):
                        word="select * from yspz_image where id='"+keywordtosearch+"' limit 5;"
                    elif (self.is_str_time(keywordtosearch)==True):
                        word="select * from yspz_image where date='"+keywordtosearch+"' limit 5;"
                    else:
                        word="select * from yspz_image where pznum='"+keywordtosearch+"' or type='"+keywordtosearch+"' or des like'%"+keywordtosearch+"%' or des like'"+keywordtosearch+"*' or des like'*"+keywordtosearch+"' limit 5;"
                    result=getdata.getData(word)
                    for i in range(len(result)):
                        wurl=wurl+"<p><a href=./?id="+str(result[i][0])+"&date="+str(result[i][1])+">"+str(result[i][0])+"、"+str(result[i][1])+result[i][2]+result[i][3]+"<br>附加说明："+result[i][6]+"</a></p>"
                wcode=wurl
                self.render("index.html",imagecode=imcode,converturl=wcode)
                getdata.closeData()
        else:
            getdata=myDb()
            word="select * from keytosee where 1;"
            allpass=getdata.getData(word)
            if(len(allpass)==0):
                newdate=time.strftime('%Y-%m-%d',time.localtime(time.time()))
                rnum=random.randint(1000, 9999)
                newpass=hashlib.md5(str(rnum).encode('utf8'))
                word="insert into keytosee (password,date) values ('"+newpass.hexdigest()+"','"+str(newdate)+"');"
                if(getdata.insertData(word)):
                    fp=open('./../lib/yzm.wenq','w')
                    fp.write(str(rnum))
                    fp.close()
                    self.render("index.html")
                newdate=""
                newpass=""
                getdata.closeData()

            


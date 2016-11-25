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
import hashlib
import time
import random

class ResultHandler(tornado.web.RequestHandler):
    def get(self):
        print('ok')
        self.render("result/getresult.html")
        key=get_argument("key")
        print(key)
    def post(self):
        keywordtosend = self.get_argument("keyword")
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
                self.render("result/getresult.html?key="+keywordtosend+"")
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

            


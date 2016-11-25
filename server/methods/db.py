# -*- coding:utf-8 -*-
'''
Author: Feng Wenqiang
E-mail: hoontu@sina.com
'''
import pymysql
import os
import zipfile

class myDb():
    def __init__(self):
        
        self.dataconfig={}
        self.getSetting()
        self.conn=pymysql.connect(**self.dataconfig)
    def getSetting(self):
        #初始化数据库
        fp=open('./../lib/database.wenq')
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
        
    def getData(self,word):
        key=word
        with self.conn.cursor() as cur:
            cur.execute(key)
            data=cur.fetchall()
        return data
    
    def insertData(self,word):
        key=word
        
        try:
            with self.conn.cursor() as cur:
                isok=cur.execute(key)
                self.conn.commit()
            return isok
        except:
            db.rollback()
    
    def delData(self,word):
        key=word
        
        try:
            with self.conn.cursor() as cur:
                isok=cur.execute(key)
                self.conn.commit()
            return isok
        except:
            db.rollback()
        return isok
    def closeData(self):
        self.conn.close()
        
if __name__ == "__main__":
    oo=myDb()
    word='SELECT * FROM `bankinfor` WHERE 1 '
    n=oo.getData(word)
    print(n)

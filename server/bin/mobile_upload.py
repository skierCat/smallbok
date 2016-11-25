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
import time

class mUploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('1.html')
    def post(self):
        print('ok')
        filename=self.request.files['file']
        print(filename)
        print('ok')

            


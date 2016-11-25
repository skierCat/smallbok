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

import sys     #utf-8，兼容汉字

from bin.index import HomeHandler    #首页
from bin.pzresult import ResultHandler    #搜索页面
from bin.mobile_upload import mUploadHandler    #手机应用的上传处理

url = [
    (r"/", HomeHandler),
    (r"/result", ResultHandler),
    (r"/mupload", mUploadHandler),
]

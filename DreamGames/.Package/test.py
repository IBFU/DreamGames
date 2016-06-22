#encoding=utf-8
#更新
import os
import sys
import time
import urllib
import urllib2
import httplib
import linecache
import function as f
import config as config
from ftplib import FTP

os.chdir('../')


# addrIP="138.128.217.186"
# addrFolder="NBFuck/bjeea"



'''
Test
'''
#f.package('.Update','.Package\\upd.zip')
#makeUpdDir()
#dropUpdDir()
#cpVersion()
#rmVersion()
#makeUpdPackage()
#uploadUpdPackage()
#pause()
#print f.getVersion()
print f.getVersion()
f.uploadUpdDatabase()
f.applyUpdDatabase()
'''
/Test
'''
# print('应用更新……'),
# f.applyUpdDatabase()
# print('DONE')
# print('正式版已更新，按任意键退出！')
# f.pause()
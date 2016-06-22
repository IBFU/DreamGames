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
'''
/Test
'''
print('创建更新目录……'),
f.makeUpdDir()
print('DONE')
print('创建版本文件……'),
f.cpVersion()
print('DONE')
print('创建更新包……'),
f.makeUpdPackage()
print('DONE')
print('上传更新包……'),
f.uploadUpdPackage()
print('DONE')
print('更新数据库……'),
f.uploadUpdDatabase()
print('DONE')
print('更新包已上传完毕，目前只有测试模式才可更新。如果需要更新正式版，请执行_applyUpdate.py！')
f.pause()
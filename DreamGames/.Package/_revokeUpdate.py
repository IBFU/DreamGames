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
import config as c
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
print('撤回更新……'),
f.revokeUpdDatabase()
print('DONE')
print('正式版已撤回，按任意键退出！')
f.pause()
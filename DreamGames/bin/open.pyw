#encoding=utf-8
import os
import sys
import win32api
#win32api.ShellExecute(0, 'open', 'explorer.exe', '..\\..\\Independent_Dreams\\Novels\\梦缘六界\\梦缘六界·幻 梗概专题.docx','',1)

#os.popen('"space one.txt"')
addr = sys.argv[1]
addr = addr.replace('/','\\')
#os.popen('start "" "%s"' %(addr))
win32api.ShellExecute(0, 'open', 'explorer.exe', '%s' %(addr),'',1)
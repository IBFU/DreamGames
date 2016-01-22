#encoding=utf-8
import sys
import os.path
import win32api
import win32clipboard as w
import win32con
import string

#aa = aa.encode("utf-8")
f=file(sys.argv[1],"w")
aa=sys.argv[2]
aa = aa.replace('@CHR034','"')
f.write(aa)
f.close()

#win32api.MessageBox(win32con.NULL, 'Savadata success. File: %s\nArgs: %s' %(sys.argv[1],aa), 'Savedata', win32con.MB_OK)
#win32api.MessageBox(win32con.NULL, 'Savadata success. Saved: %s' %(sys.argv[1]), 'Savedata', win32con.MB_OK)
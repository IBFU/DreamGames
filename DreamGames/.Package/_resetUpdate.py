#encoding=utf-8
#更新
import os
import sys
import time
import function as f
os.chdir('../')

print('按任意键开始重置更新目录！如不重置请关闭窗口！')
f.cmd('pause>nul')
f.dropUpdDir()
f.makeUpdDir()
print('重置完成！')
#for i in range(0,5):
	#cmd('rd /s /q _update')

#encoding=utf-8
import sys
import os.path
import win32api
import win32clipboard as w
import win32con
import string

config={
	'engineIP':			'138.128.217.186',
	'engineServer':		'http://dreamui.ibfu.org/',
	'gamecoreServer':	'http://dreamgames.ibfu.org/',
	'gamecoreFolder':	'dreamui/dreamgames/',
	'updateDir':		'update/',
	'noUpdFolder':		['.backup','.Update','.Develop','.Packages'],
'':''}
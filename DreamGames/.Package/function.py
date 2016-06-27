#encoding=utf-8
import os
import sys
import os.path
import win32api
import win32clipboard as w
import win32con
import string
import zipfile
import config as c
from ftplib import FTP
import xml.dom.minidom
import urllib
import urllib2

noUpdFolder=c.config['noUpdFolder']
addrIP=c.config['engineIP']
addrFolder=c.config['gamecoreFolder']+c.config['updateDir']
addrAddress=c.config['gamecoreServer']+c.config['updateDir']

versionList={}

def cmd(c):
	os.system(c)

def pause():
	cmd("pause")

def wait(t):
	time.sleep(t)

def package(dirname,zipfilename):#打包，参数：文件（夹）名，包名。dirname留空表示将当前目录内容添加入zip包
	filelist = []
	if os.path.isfile(dirname):
		filelist.append('.\\%s' %(dirname))
		#print 'Include File: .\\%s' %(dirname)
	else :
		if dirname=='':
			dirname='.'
		for root, dirs, files in os.walk(dirname):
			for name in files:
				#filelist.append(os.path.join(root, name))
				filelist.append(os.path.join(root, name).replace('%s\\' %(dirname),''))
				#print 'Include File: %s' %(os.path.join(root, name))
	#print filelist
	#print '';
	print '#dirname: %s\\ #zipfilename: %s' %(dirname,zipfilename)
	try:
		zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
		fileNumber=0
		for tar in filelist:
			#arcname = tar[len(dirname):]
			arcname = tar
			print '#Package File: %s' %(arcname)
			#print 'tar: %s len(dirname): %s arcname: %s' %(tar,len(dirname),arcname)
			zf.write(tar,arcname)
			fileNumber+=1
		zf.close()
		print '#Package File number; %s' %(fileNumber)
		return True
	except Exception,e:
		print '#ERROR: %s - %s' %(Exception,e)
		return False

def unpackage(zipfilename, unziptodir):#解包，参数：包名，文件夹名。unziptodir留空表示解包到当前目录
	if unziptodir!='' and not os.path.exists(unziptodir):
		os.mkdir(unziptodir)
	else:
		unziptodir='.'
	print '#zipfilename: %s #unziptodir: %s\\' %(zipfilename,unziptodir)
	try:
		zfobj = zipfile.ZipFile(zipfilename)
		fileNumber=0
		for name in zfobj.namelist():
			name = name.replace('\\','/')
			print '#Unpackage File: %s' %(name)
			if name.endswith('/'):
				os.mkdir(os.path.join(unziptodir, name))
			else:
				ext_filename = os.path.join(unziptodir, name)
				ext_dir= os.path.dirname(ext_filename)
				if not os.path.exists(ext_dir):
					os.mkdir(ext_dir)
				outfile = open(ext_filename, 'wb')
				outfile.write(zfobj.read(name))
				outfile.close()
				fileNumber+=1
		print 'Unpackage File number: %s' %(fileNumber)
		return True;
	except Exception,e:
		print '#ERROR: %s - %s' %(Exception,e)

		return False

def upload(local,nfile):
	addrFTP=("/var/www/html/%s/" %(addrFolder))
	try:
		ftp = FTP(addrIP)#创建ftp对象
		ftp.set_pasv(1)#主动模式=0，被动模式=1
		ftp.login("jmry", "jmry1991")#登录ftp
		ftp.cwd(addrFTP)#设置上传目录
		#ftp.retrlines("LIST")#列出文件
		localfile = ("%s%s" %(local,nfile))#本地文件变量
		f = open(localfile, 'rb')#打开本地文件
		rtn = ftp.storbinary( ("STOR %s" %(os.path.basename(localfile) ) ) , f)#将本地文件上传到ftp
		f.close()
		return rtn #返回结果
	except Exception,ex:
		print Exception,ex
		return -1
def download(local,nfile):
	#addrServer=("http://%s/%s/" %(addrIP,addrFolder))
	addrServer='%s%s' %(c.config['gamecoreServer'],c.config['updateDir'])
	try:
		rtn = urllib.urlretrieve("%s%s" %(addrServer,nfile), "%s%s" %(local,nfile))#下载文件
		if rtn != None:
			return rtn
		else:
			return -1
	except Exception,ex:
		print Exception,ex
		return -1

def makeUpdDir():
	cmd('md .Update')
	fileList = os.listdir('./')
	dirList = []
	for f in fileList:
		if os.path.isdir(f):
			dirList.append(f)
	for nf in noUpdFolder:
		try:
			#print('NON-UPDFOLDER %s DONE' %(nf))
			dirList.remove('%s' %(nf))
			# dirList.remove('_backup')
			# dirList.remove('_update')
			# dirList.remove('_shell')
			# dirList.remove('_packages')
			# dirList.remove('web_down')
		except:
			print('NON-UPDFOLDER %s NOTEXIST' %(nf))
	for d in dirList:
		cmd('md .Update\\%s' %(d))

def dropUpdDir():
	updDirList = os.listdir('./.Update/')
	cmd('del /q .Update\\*')
	for ud in updDirList:
		cmd('rd /s /q .Update\\%s' %(ud))

def getVersion():
	global versionList
	dom = xml.dom.minidom.parse('config\\version.xml')
	root = dom.documentElement
	for c in root.childNodes:
		try:
			# versionKey.append(c.getAttribute("key"))
			# versionValue.append(c.getAttribute("value"))
			versionList[c.getAttribute("key")]=c.getAttribute("value")
		except:
			pass
	#print root.firstChild.attributes('key')
	versionStr='%s.%s.%s' %(versionList['mainVersion'],versionList['buildVersion'],versionList['dateVersion'])
	return versionStr

def cpVersion():
	cmd('copy /y config\\version.xml .Update\\config\\')
	cmd('copy /y engine\\version.xml .Update\\engine\\')

def rmVersion():
	cmd('del /q .Update\\config\\version.xml')
	cmd('del /q .Update\\engine\\version.xml')

def makeUpdPackage():
	#updv=linecache.getline('_Version', 1).replace(' ','_').replace('.','_')
	#package('.Update/','_update','update_%s' %(updv))
	package('.Update','.Package\\packages\\update_%s.zip' %(getVersion()))

def uploadUpdPackage():
	updList=os.listdir('.Package\\packages\\')
	updList.sort()
	upload('.Package\\packages\\','%s' %(updList[len(updList)-1]))

def uploadUpdDatabase():
	getVersion()
	#strHtml = urllib2.urlopen(addrAddress).read()
	strHtml = urllib2.urlopen('%supd_database.php?state=updversion&mainVersion=%s&buildVersion=%s&dateVersion=%s&versionName=%s' %(addrAddress,versionList['mainVersion'],versionList['buildVersion'],versionList['dateVersion'],versionList['versionName'])).read()
	print strHtml

def applyUpdDatabase():
	getVersion()
	strHtml = urllib2.urlopen('%supd_database.php?state=applyupdate&mainVersion=%s&buildVersion=%s&dateVersion=%s&versionName=%s' %(addrAddress,versionList['mainVersion'],versionList['buildVersion'],versionList['dateVersion'],versionList['versionName'])).read()
	print strHtml

def revokeUpdDatabase():
	getVersion()
	strHtml = urllib2.urlopen('%supd_database.php?state=revokeupdate&mainVersion=%s&buildVersion=%s&dateVersion=%s&versionName=%s' %(addrAddress,versionList['mainVersion'],versionList['buildVersion'],versionList['dateVersion'],versionList['versionName'])).read()
	print strHtml

def revokeUpdDatabaseV(mainV,buildV,dateV,vName):
	#getVersion()
	strHtml = urllib2.urlopen('%supd_database.php?state=revokeupdate&mainVersion=%s&buildVersion=%s&dateVersion=%s&versionName=%s' %(addrAddress,mainV,buildV,dateV,vName)).read()
	print strHtml
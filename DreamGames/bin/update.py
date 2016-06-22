#encoding=utf-8
#更新
import os,os.path
import sys
import zipfile
import xml.dom.minidom
import urllib
import urllib2

config={
	'engineServer':		'http://dreamui.ibfu.org/',
	'gamecoreServer':	'http://dreamgames.ibfu.org/',
	'updateDir':		'update/',
'':''}
versionList={}
packageList=[]
#test
addrAddress=config['gamecoreServer']+config['updateDir']

def cmd(c):
	os.popen(c)

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
		dirname='.'
		for root, dirs, files in os.walk(dirname):
			for name in files:
				filelist.append(os.path.join(root, name))
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

def download(local,nfile):
	#addrServer=("http://%s/%s/" %(addrIP,addrFolder))
	addrServer='%s%s' %(config['gamecoreServer'],config['updateDir'])
	try:
		rtn = urllib.urlretrieve("%s%s" %(addrServer,nfile), "%s%s" %(local,nfile))#下载文件
		if rtn != None:
			return rtn
		else:
			return -1
	except Exception,ex:
		print Exception,ex
		return -1

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

def getPackageList():
	global packageList
	getVersion()
	strHtml = urllib2.urlopen('%supd_getpackage.php?mainVersion=%s&buildVersion=%s&dateVersion=%s&versionName=%s' %(addrAddress,versionList['mainVersion'],versionList['buildVersion'],versionList['dateVersion'],versionList['versionName'])).read()
	packageList=strHtml.split('|')
	print packageList

def downloadPackage():
	for pl in packageList:
		ustr=download('./',pl)
		print 'Package download: %s %s' %(pl,ustr)

def applyPackage():
	for pl in packageList:
		ustr=unpackage(pl,'')
		print 'Package apply: %s %s' %(pl,ustr)
		if ustr!=False:
			cmd('del %s' %(pl))
			print 'Package drop: %s' %(pl)
			#dropPackage()

def dropPackage():
	for pl in packageList:
		cmd('del %s' %(pl))
		print 'Package drop: %s' %(pl)

def main():
	#package('','savedata.pyw.zip')
	#unpackage('savedata.pyw.zip','')
	getPackageList()
	downloadPackage()
	applyPackage()
main()
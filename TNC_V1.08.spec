# -*- mode: python -*-
import time,sys,datetime,re,os,pytest,subprocess


block_cipher = None
if (sys.platform == "win32"):
    pathexStr = 'C:\\Users\\tarnold\\Dropbox\\AppTool_Project\\Python_Dev\\TNC\\'
    guiLibPath = 'C:\\Users\\tarnold\\Dropbox\\AppTool_Project\\Python_Dev\\TNC\\GUI_Library\\'
    mainProgPath = 'C:\\Users\\tarnold\\Dropbox\\AppTool_Project\\Python_Dev\\TNC\\'
    docPath = 'C:\\Users\\tarnold\\Dropbox\\AppTool_Project\\Python_Dev\\TNC\\Documents\\'
    progName='TNC_V1.2_Win'
elif (sys.platform == "linux"):
    pathexStr = '/u/tarnold/TNC/'
    guiLibPath = '/u/tarnold/TNC/GUI_Library/'
    mainProgPath = '/u/tarnold/TNC/'
    docPath = '/u/tarnold/TNC/Documents/'
    progName='TNC_V1.2_Lin'

a = Analysis(['TestNoChg_Controller_V1.08.py'],
             pathex=[pathexStr],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[pathexStr+'TNC_Environment.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
a.datas += []	
	 
a.binaries += [('TNC_Help.pdf', docPath+'TNC_Help.pdf', 'DATA'),
			('.tmp_script1', pathexStr+'.tmp_script1', 'DATA'),
			('.tmp_script2', pathexStr+'.tmp_script2', 'DATA')]

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=progName,
          debug=None,
          strip=None,
          upx=None,
          console=None , icon='favicon.ico')

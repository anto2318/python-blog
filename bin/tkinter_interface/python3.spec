# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['tkinter_interface.py/usr/local/opt/python@3.8/bin/python3.8', '/Users/antonionardi/Proyectos/Python_Blog/python-blog/bin/temp/openw.py'],
             pathex=['/Users/antonionardi/Proyectos/Python_Blog/python-blog/bin/tkinter_interface'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='python3',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )

# -*- mode: python -*-

import os
import sys


block_cipher = None


a = Analysis(['hproxy.py'],
             binaries=[],
             datas=[
                ('templates', 'hpxqt/templates'),
                ('media', 'hpxqt/media'),
                ('certs', 'hpxqt/certs'),
             ],
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
          name='hproxy',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon=os.path.join('hpxqt', 'media', 'images', 'Desktop_icon.ico'))

# Build a .app if on OS X
if sys.platform == 'darwin':
   app = BUNDLE(exe,
                name='hproxy.app',
                icon=os.path.join('hpxqt', 'media', 'images', 'Desktop_icon.icns'))

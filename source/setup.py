from distutils.core import setup
import py2exe, sys, os
sys.argv.append('py2exe')
setup(console=['clicker.py'],
      options = {'py2exe': {'bundle_files': 2, 'compressed': True}},
      zipfile = None,
)
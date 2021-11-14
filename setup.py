import sys
sys.path.append(r'C:\duck-project\venv\Lib\site-packages\pynput\_util\__init__.py')
import pynput
from distutils.core import setup
import py2exe
setup(console=['main.py'])
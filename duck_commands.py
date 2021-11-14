import sys
from os import listdir
from os.path import isfile, join
import duck_classes as dcl

self_module = sys.modules[__name__]
command_list = []

extention_files = [f.split('.')[0] for f in listdir('extensions') if isfile(join('extensions', f)) and f.split('.')[1]=='dext']

for file in extention_files:
    command_list.append(dcl.command(command_name=file))
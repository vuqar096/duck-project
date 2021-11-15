from os.path import join
import py_mini_racer

context = py_mini_racer.MiniRacer()

print(context.eval('function a(){ return JSON.stringify(`asəə`); }; a()'))
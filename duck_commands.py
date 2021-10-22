import sys
import duck_classes as dcl

self_module = sys.modules[__name__]

statcond = dcl.command(command_name='statcond',command_type='past',command_func=None)

# command_list array must be locate at bottom
command_list = [i for i in dir(self_module) if type(getattr(self_module,i)) is dcl.command]
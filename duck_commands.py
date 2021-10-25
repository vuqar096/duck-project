# from _typeshed import Self
import sys
import duck_classes as dcl

self_module = sys.modules[__name__]

def copypast(command_self):
    import time as tm
    from pynput.keyboard import Key, Controller

    keyboard = Controller()
    from duck_console import magic_word
    for i in range(0,len(command_self.command_name + magic_word)):
        tm.sleep(0.01)
        keyboard.press(Key.backspace)
        
statcond = dcl.command(command_name='statcond', command_type='copypast', command_func=copypast)



# command_list array must be locate at bottom
command_list = [i for i in dir(self_module) if type(getattr(self_module,i)) is dcl.command]
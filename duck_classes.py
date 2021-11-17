from os.path import join
import py_mini_racer

import keyboard_ctrl

context = py_mini_racer.MiniRacer()

class command:


    global command_list
    global preserved_arguments
    command_list = []
    preserved_arguments = ['left_text','right_text','all_text','clipboard']

    def __init__(self, command_name):
        global context
        if len(command_name) > 2:
            self.command_name = command_name
        else:
            raise ValueError('command name must be at least 3 charater.')

        # load command script
        self.command_script = open(join('extensions',command_name+'.dext'),'r',encoding="utf-8").read()
        get_argument_names = open(r'dictionaries/get_argument_names.js', 'r').read()
        self.argument_count = context.eval(self.command_script + command_name + '.length')
        self.argument_names = context.eval(get_argument_names + self.command_script + 'get_argument_names(' + command_name + ').toString()').split(',')
        #
        command_list.append(self)

    def exec(self, arguments):
        if len(arguments) == len([arg for arg in self.argument_names if arg not in preserved_arguments]):

            keyboard_ctrl.implement(context.eval(self.command_script + self.command_name + '(' + ','.join(['\'' + i + '\'' for i in arguments]) + ')'))


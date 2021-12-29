import json
from os.path import join
import py_mini_racer

import functions

context = py_mini_racer.MiniRacer()

class command:


    global command_list
    global preserved_arguments
    command_list = []
    preserved_arguments = ['left_text','left_paragraph','right_text','right_paragraph','all_text','clipboard']

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
        arguments_dict = {}
        arguments = [i for i in arguments if i!='']
        arg_x_list = [arg for arg in self.argument_names if arg not in preserved_arguments]
        arg_y_list = [arg for arg in self.argument_names if arg     in preserved_arguments]
        if len(arg_x_list) == self.argument_count & len(arguments) == len(arg_x_list):
            for arg in arg_x_list:
                arguments_dict[arg] = arguments[arg_x_list.index(arg)]
        if len(arg_y_list) > 0:
            for arg in arg_y_list:
                arguments_dict[arg] = functions.preserved_argument_list_advanced(arg)

        z = (self.command_script + self.command_name + '(' + ','.join([key+'='+json.dumps(value) for key,value in arguments_dict.items()]) + ')')
        functions.implement(context.eval(z))
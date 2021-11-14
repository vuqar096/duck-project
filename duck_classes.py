from os.path import join
import py_mini_racer
import functions

context = py_mini_racer.MiniRacer()

class command:


    global command_list
    command_list = []

    def __init__(self, command_name):
        global context
        if len(command_name) > 2:
            self.command_name = command_name
        else:
            raise ValueError('command name must be at least 3 charater.')

        # load command script
        self.command_script = open(join('extensions',command_name+'.dext'),'r').read()
        get_argument_names = open(r'dictionaries/get_argument_names.js', 'r').read()
        self.argument_count = context.eval(self.command_script + command_name + '.length')
        self.argument_names = context.eval(get_argument_names + self.command_script + 'get_argument_names(' + command_name + ').toString()')
        #
        command_list.append(self)

    def exec(self):
        None
        # all_text
        # left_text
        # right_text
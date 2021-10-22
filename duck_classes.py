class command:

    global command_types
    command_types = ['past', 'application']

    def __init__(self, command_name, command_type, command_func):

        if len(command_name) > 2:
            self.command_name = command_name
        else:
            raise ValueError('command name must be at least 3 charater.')
        if command_type in command_types:
            self.command_type = command_type
        else:
            raise ValueError('command type is not correct.')
        self.command_func = command_func

    def exec(self):
        self.command_func()
duck_command = []
command1 = []
variable1 = []

global magic_word
magic_word = 'duck'


print('duck_console started')

def sound(x):
    import winsound as ws
    if x != magic_word:
        ws.Beep(frequency=1000, duration=250)
    else:
        ws.PlaySound('duck.wav',ws.SND_FILENAME)

def listen4(command):
    None

def key2asterix(key):
    x = ['Key.space']
    y = ['*']
    result = ''
    for a,b in zip(x,y):
        key = str(key).replace(a,b)
    return key

def append_keys(key_code):
    global duck_command
    key = str(key_code).replace(r"'",'')
    key = key2asterix(key)
    if len(duck_command) == 20:
        duck_command.pop(0)
        duck_command.append(key)
    else:
        duck_command.append(key)
    check_variable1(key)
    check_command1(key)
    check_duck()


def check_command1(key):
    global command1

    if len(command1) > 0:
        command1.append(key)
        if len(command1) == 10:
            command1.clear()
        command = "".join(command1[1:len(command1)])
        import duck_commands as dcm
        if command in dcm.command_list:
            for i in dcm.dcl.command_list:
                # i.exec()
                sound('beep')
                variable1.clear()
                variable1.append('x')

            command1.clear()

def check_variable1(key):
    global variable1

    if len(variable1) > 0:
        variable1.append(key)
        if len(variable1) == 20:
            variable1.clear()
        command = "".join(variable1[1:len(variable1)])
        print(command)
        #

def check_duck():
    start = len(duck_command) - 5
    stop = len(duck_command) - 1
    if len(duck_command) >3:
        if ''.join(duck_command[-4:]) == magic_word:
            print('duck activated')
            sound('beep')
            command1.clear()
            command1.append('x')
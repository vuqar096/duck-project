import functions

cmd_line = []
cmd_seperated = []


global magic_word
magic_word = 'dex'


print('duck_console started')

def sound(x):
    import winsound as ws
    if x != magic_word:
        ws.Beep(frequency=1000, duration=250)
    else:
        ws.PlaySound('duck.wav',ws.SND_FILENAME)


def key2asterix(key):
    x = ['Key.space']
    y = ['*']
    result = ''
    for a,b in zip(x,y):
        key = str(key).replace(a,b)
    return key

def append_keys(key_code):
    global cmd_line, cmd_seperated
    key = str(key_code).replace(r"'",'')
    key = key2asterix(key)
    if len(cmd_line) == 50:
        cmd_line.pop(0)
        cmd_line.append(key)
    else:
        cmd_line.append(key)
    cmd_seperated = ''.join(cmd_line).split('*')
    check_command(cmd_seperated)
    check_duck()


def check_command(x):
    import duck_commands as dc
    import keyboard_ctrl as kc
    global magic_word
    global cmd_line
    finded_cmd_value = ''.join([i for i in x if len([a for a in dc.command_list if i == a.command_name]) > 0])
    if finded_cmd_value!='':
        cmd_index = cmd_seperated.index(finded_cmd_value)

        command_lenght = (''.join(cmd_line).rfind(finded_cmd_value) + len(finded_cmd_value) - ''.join(cmd_line).rfind(magic_word))

        if '*'.join(cmd_seperated).rfind(magic_word)<'*'.join(cmd_seperated).rfind(finded_cmd_value) and '*'.join(cmd_seperated).rfind(magic_word)!=-1:

            kc.npress(kc.Key.backspace, command_lenght + 1)
            for i in dc.dcl.command_list:
                if i.command_name==finded_cmd_value:
                    i.exec(functions.get_arguments(cmd_line,magic_word=magic_word,finded_cmd_value=finded_cmd_value))
                    cmd_line.clear()



def check_duck():
    if len(cmd_line) >= 3:
        if cmd_seperated[-1][(len(magic_word)*(-1)):] == magic_word:
            print('duck activated2')
            sound('beep')
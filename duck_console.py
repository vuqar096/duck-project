last_20_keys = []
next_20_keys = []

global magic_word
magic_word = 'duck'


print('duck_console started')

def sound(x):
    import winsound as ws
    if x != magic_word:
        ws.Beep(frequency=1000, duration=250)
    else:
        ws.PlaySound('duck.wav',ws.SND_FILENAME)

def append_keys(key_code):
    global last_20_keys
    key = str(key_code).replace(r"'",'')
    if len(last_20_keys) == 20:
        last_20_keys.pop(0)
        last_20_keys.append(key)
    else:
        last_20_keys.append(key)
    check_command(key)
    check_duck()


def check_command(key):
    global next_20_keys

    if len(next_20_keys) > 0:
        next_20_keys.append(key)
        if len(next_20_keys) == 20:
            next_20_keys.clear()
        command = "".join(next_20_keys[1:len(next_20_keys)])
        import duck_commands as dcm
        if command in dcm.command_list:
            for i in dcm.dcl.command_list:
                i.exec()
            next_20_keys.clear()


def check_duck():
    start = len(last_20_keys)-5
    stop = len(last_20_keys) - 1
    if len(last_20_keys) >3:
        if ''.join(last_20_keys[-4:]) == magic_word:
            print('duck activated')
            sound('beep')
            next_20_keys.clear()
            next_20_keys.append('x')
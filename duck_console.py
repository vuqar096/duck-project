last_20_keys = []
next_20_keys = []



print('duck_console started')

def sound(x):
    import winsound as ws
    if x != 'duck':
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
    check_duck()

def check_duck():
    start = len(last_20_keys)-5
    stop = len(last_20_keys) - 1
    if len(last_20_keys) >3:
        if ''.join(last_20_keys[-4:]) == 'duck':
            print('duck activated')
            sound('beep')
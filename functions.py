import time


def btoa(data):
    import base64
    x_bytes = data.encode("utf-8")
    base64_bytes = base64.b64encode(x_bytes)
    return base64_bytes.decode("utf-8")

def atob(base64_bytes):
    import base64
    x_bytes2 = base64.b64decode(base64_bytes)
    return x_bytes2.decode("utf-8")

def get_arguments(x,magic_word,finded_cmd_value):
    try:
        join_x = ''.join(x)
        duck_word_index = join_x.rindex(magic_word)
        cmd_word_index = join_x.rindex(finded_cmd_value)

        return join_x[duck_word_index+len(magic_word)+1:cmd_word_index-1].split('*')
    except:
        print(x)
        print('error: get_arguments')

def keycode2str(keycode):
    event_which = [8,9,13,16,16,17,17,18,18,19,20,27,32,33,34,35,36,37,38,39,40,44,45,46,48,49,50,51,52,53,54,55,56,57,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,144,145,173,174,175,181,182,183,186,187,188,189,190,191,192,219,220,221,222]
    event_code  = ['Backspace','Tab','Enter','Shift','Shift','Control','Control','Alt','Alt','Pause','CapsLock','Escape','','PageUp','PageDown','End','Home','ArrowLeft','ArrowUp','ArrowRight','ArrowDown','PrintScreen','Insert','Delete','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','Meta','Meta','ContextMenu','0','1','2','3','4','5','6','7','8','9','*','+','-','.','/','F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','NumLock','ScrollLock','AudioVolumeMute','AudioVolumeDown','AudioVolumeUp','LaunchMediaPlayer','LaunchApplication1','LaunchApplication2',';','=',',','-','.','/','`','[','\\',']','\'']
    try:
        x = str(keycode).replace('<','').replace('>','')
        y = str(event_code[event_which.index(int(x))])
    except:
        y = keycode
    return y

def az_lat(x):
    a = ['ə','ı','ç','ş','ğ','ü','ö','Ə', 'I', 'Ç', 'Ş', 'Ğ', 'Ü', 'Ö']
    b = ['\\xc9\\x99', '\\xc4\\xb1', '\\xc3\\xa7', '\\xc5\\x9f', '\\xc4\\x9f', '\\xc3\\xbc', '\\xc3\\xb6','\\xc6\\x8f', 'I', '\\xc3\\x87', '\\xc5\\x9e', '\\xc4\\x9e', '\\xc3\\x9c', '\\xc3\\x96']
    for letters in b:
        x = x.replace(letters,a[b.index(letters)])
    return x

def ifnone(x,y):
    if x is None:
        return y
    else:
        return x

def one_tuple(tuple_x):
    if len(tuple_x) == 1:
        return tuple_x[0]
    else:
        return tuple_x

def decode(*args):
    inputx = None
    result = None
    if len(args)%2!=1:
        inputx = args[0:len(args)-1]
    else:
        inputx = args
    for arg_a,arg_b in zip(inputx[1::2],inputx[2::2]):
        if arg_a == inputx[0]:
            result = arg_b
            break
    if len(args)%2!=1 and result == None:
        result = args[-1]
    return result

def preserved_argument_list(argument_name):
        import keyboard_ctrl as kc
        import pyperclip as clip
        clipboard_temp = clip.paste()

        kc.press_combination(*tuple(decode(argument_name.split('_')[1],'text',[kc.Key.ctrl,kc.Key.shift],[kc.Key.shift])+[decode(argument_name.split('_')[0],'left',kc.Key.home,kc.Key.end)] ))
        kc.press_combination(kc.Key.ctrl.value,'c')
        kc.npress(decode(argument_name.split('_')[0],'left',kc.Key.right,kc.Key.left),2)

        argument_value = "".join([i.replace('\r','').replace('\n','\\\\n') for i in list([i for i in clip.paste()])])
        clip.copy(clipboard_temp)
        return argument_value

def implement(extension_result):
    import json
    import pyperclip as clip
    import keyboard_ctrl as kc
    clipboard_temp = clip.paste()
    key_dict = {'backspace': kc.Key.backspace,
     'enter': kc.Key.enter,
     'ctrl': kc.Key.ctrl.value,
     'shift': kc.Key.shift,
     'alt': kc.Key.alt
    }
    preserved_argument_list('right_paragraph')
    for action in json.loads(extension_result):
        action_type = action[0:str(action).find('/')]
        action_value = action[str(action).find('/') + 1:]
        if action_type == 'text':
            clip.copy(action_value.replace('\\n','\n'))
            kc.press_combination(kc.Key.ctrl.value,'v')
            clip.copy(clipboard_temp)
        elif action_type == 'keys':
            kc.press_combination(*one_tuple(tuple([ifnone(key_dict.get(value), value) for value in str(action_value).split('+')])))
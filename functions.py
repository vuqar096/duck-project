#
# def copy(data):
#     import win32clipboard
#     win32clipboard.OpenClipboard()
#     win32clipboard.EmptyClipboard()
#     win32clipboard.SetClipboardText(data)
#     win32clipboard.CloseClipboard()
#
# def past():
#     import win32clipboard
#     win32clipboard.OpenClipboard()
#     data = win32clipboard.GetClipboardData()
#     win32clipboard.CloseClipboard()
#     return data

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
import keyboard_ctrl as kc

key_dict = {'backspace': kc.Key.backspace,
            'enter': kc.Key.enter,
            'ctrl': kc.Key.ctrl.value,
            'shift': kc.Key.shift,
            'alt': kc.Key.alt
            }

def one_tuple(tuple_x):
    if len(tuple_x) == 1:
        return tuple_x[0]
    else:
        return tuple_x

x = 15, 3
print(x)
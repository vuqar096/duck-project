import string

from pynput.keyboard import Key, Listener
import duck_console as dc
import functions


def on_press(key):
    if key not in [Key.backspace,Key.enter,Key.ctrl_l,Key.shift_r,Key.alt_l,Key.shift]:
        dc.append_keys(functions.keycode2str(key))
    if key == Key.backspace:
        try:
            dc.cmd_line.pop()
            print(dc.cmd_line)
        except:
            None


def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

def check_key(key):
    print(key)

def start_listen():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

start_listen()
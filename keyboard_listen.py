import string

from pynput.keyboard import Key, Listener
import duck_console as dc

def on_press(key):
    if key not in [Key.backspace,Key.enter]:
        dc.append_keys(key)

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
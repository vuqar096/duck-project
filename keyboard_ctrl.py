from pynput.keyboard import Key, Listener, Controller
import duck_console as dc

keyboard = Controller()

def press(button):
    if button == 'backspace':
        keyboard.type('hello')

def on_press(key):
    dc.append_keys(key)

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

def check_key(key):
    print(key)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
import json
import time

from pynput.keyboard import Key, Controller

import functions

keyboard = Controller()


def press_combination(*buttons):
    for button in buttons:
        keyboard.press(button)
    for button in buttons:
        keyboard.release(button)

def npress(button,ntimes=1):
        for i in range(1,ntimes):
            time.sleep(0.01)
            keyboard.press(button)
            keyboard.release(button)

def implement(extension_result):
    import pyperclip as clip
    clipboard_temp = clip.paste()
    for action in json.loads(extension_result):
        action_type = action[0:str(action).find('/')]
        action_value = action[str(action).find('/') + 1:]
        if action_type == 'text':
            clip.copy(action_value)
            press_combination(Key.ctrl.value,'v')
            clip.copy(clipboard_temp)
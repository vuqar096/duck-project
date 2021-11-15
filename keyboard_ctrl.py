import json
import time

from pynput.keyboard import Key, Controller

import functions

keyboard = Controller()

def npress(button,ntimes=1):
        for i in range(1,ntimes):
            time.sleep(0.01)
            keyboard.press(button)

def implement(extension_result):
    for action in json.loads(extension_result):
        action_type = action[0:str(action).find('/')]
        action_value = action[str(action).find('/') + 1:]
        if action_type == 'text':
            keyboard.type(action_value)
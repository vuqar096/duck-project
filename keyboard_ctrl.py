import time
from pynput.keyboard import Key, Controller


keyboard = Controller()


def press_combination(*buttons):
    for button in buttons:
        keyboard.press(button)
    for button in buttons:
        keyboard.release(button)

def press_combination_unrelease(*buttons):
    for button in buttons:
        keyboard.press(button)

def press_combination_release(*buttons):
    for button in buttons:
        keyboard.release(button)

def npress(button,ntimes=1):
        for i in range(1,ntimes):
            time.sleep(0.01)
            keyboard.press(button)
            keyboard.release(button)
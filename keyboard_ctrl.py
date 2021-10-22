import time

from pynput.keyboard import Key, Controller

keyboard = Controller()

def npress(button,ntimes=1):
        for i in range(1,ntimes):
            time.sleep(0.01)
            keyboard.press(button)
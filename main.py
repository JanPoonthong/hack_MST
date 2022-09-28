from pynput.keyboard import Key, Controller
from time import sleep
import random
import string

keyboard = Controller()


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


for i in range(50):
    sleep(0.5)
    keyboard.type(randomword(10))
    keyboard.press(Key.enter)

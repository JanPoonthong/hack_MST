from pynput.keyboard import Key, Controller
from time import sleep
import random
import string

keyboard = Controller()


def randomword(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


sleep(3)
# names = ["@𝔹𝕚𝕎", "@b.", "@มีผัวมากมาย แต่ไม่มีปัญญาเปย์", "@TK", "@demonsinmybrain"]
# names = ["@krit", "@MEOWMAOW", "@PeepZ", "@นักศึกษาต่างม.ที่ผ่านทางมา", "@ผมไม่ได้โกหก", "@มีผัวมากมาย แต่ไม่มีปัญญาเปย์", "@♦Master♦lolicon"]
names = ["@BIW#8218", "@TK", "@b.#7234"]
text = "The  great breakthrough in your life comes when you realize that you can learn anything you need to learn to accomplish any goal that you set for yourself.".split()

"""
for i in range(len(names)):
    # keyboard.type(randomword(10))
    keyboard.type(f"{names[i]} https://www.codingame.com/clashofcode/clash/2670913a2b75e5e3ca81b90fa3e823da9a33d98")
    # keyboard.type(f"{names[i]}\n```python\nprint(int(math.log(y,n)))```")
    # keyboard.type(f"{names[i]} Bye Bye boys, girls, and ladyboys. gtg to sleep. GOOD LUCK WITH YOUR EXAM KRUB")
    # keyboard.type(f"{i}")
    sleep(0.2)
    keyboard.press(Key.enter)
"""


for i in text:
    keyboard.type(f"{i}")
    sleep(0.2)
    keyboard.press(Key.space)

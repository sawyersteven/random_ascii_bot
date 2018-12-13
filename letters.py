from pyfiglet import Figlet
import random


def p(string):
    return getattr(Fonts, random.choice(Fonts.__styles__)).renderText(string.upper()).rstrip()


class Fonts(object):
    big = Figlet(font='big')
    rectangles = Figlet(font='rectangles')
    standard = Figlet(font='standard')
    chunky = Figlet(font='chunky')
    lean = Figlet(font='lean')
    block = Figlet(font='block')
    doom = Figlet(font='doom')
    ogre = Figlet(font='ogre')
    rounded = Figlet(font='rounded')
    small = Figlet(font='small')


Fonts.__styles__ = [i for i in Fonts.__dict__.keys() if not i.startswith('_')]

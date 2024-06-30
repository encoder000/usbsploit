from .cmd import run as runc
from .charmapcodes import run as utfwrite

from ada.keycode import Keycode
from ada.keyboard import Keyboard
from ada.keyboard_layout_us import KeyboardLayoutUS

import time

def help():
	print('''
Runs linux terminal and enters your command.
''')

def run(args):
	kbd = Keyboard()

	runc([])
	time.sleep(1)

	utfwrite(args)
	kbd.press(Keycode.ENTER)
	kbd.release_all()


	#layout.write('exit')
	kbd.press(Keycode.ENTER)
	kbd.release_all()

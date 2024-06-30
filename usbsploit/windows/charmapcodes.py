from ada.keycode import Keycode
from ada.keyboard import Keyboard
from ada.keyboard_layout_us import KeyboardLayoutUS
from ada import better_keycode

import time

def help():
	print('''
This script helps to write ascii text, using windows alt-codes with any layout of laptop.

Example:
run charmapcodes.py cats
''')

def run(args):
	kbd = Keyboard()
	layout = KeyboardLayoutUS(kbd)

	str_ = ' '.join(args)
	print('Using windows ascii-charmapcodes:',args)
	for i in str_:
		kbd.press(Keycode.ALT)
		for j in ord(i):
			kbd.press(better_keycode.get(j))
		kbd.release_all()
		time.sleep(0.2)

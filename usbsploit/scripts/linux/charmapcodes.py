from ada.keycode import Keycode
from ada.keyboard import Keyboard
from ada.keyboard_layout_us import KeyboardLayoutUS
from ada import better_keycode

import time

def help():
	print('''
This script helps to write utf text, using linux ctrl-shift-u-codes with any layout of laptop.
Works not everywhere :(

Example:
run charmapcodes.py cats
''')

def run(args):
	kbd = Keyboard()
	layout = KeyboardLayoutUS(kbd)

	str_ = ' '.join(args)
	print('Using linux utf-charmapcodes:',args)
	for i in str_:
		kbd.press(Keycode.CONTROL,Keycode.SHIFT,Keycode.U)
		kbd.release_all()

		layout.write(hex(ord(i))[2:])

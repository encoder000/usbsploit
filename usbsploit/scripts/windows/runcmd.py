from .cmd import run as runc
from .charmapcodes import run as asciiwrite

from ada.keycode import Keycode
from ada.keyboard import Keyboard
from ada.keyboard_layout_us import KeyboardLayoutUS

import time

def help():
	print('''
Runs windows terminal and enters your command.

WORKS ONLY WITH ASCII TEXT!!!!!
''')

def run(args):
	kbd = Keyboard()
	layout = KeyboardLayoutUS(kbd)

	runc([]) #runs cmd
	asciiwrite(' '.join(args))
	kbd.press(Keycode.ENTER)
	kbd.release_all()


	#asciiwrite('exit') - you can exit yourself if you want idk
	#kbd.press(Keycode.ENTER)
	#kbd.release_all()

from ada.keycode import Keycode
from ada.keyboard import Keyboard
from ada.keyboard_layout_us import KeyboardLayoutUS

def help():
	print('''
Just runs linux terminal

Example:
run cmd.py
''')

def run(args):
	kbd = Keyboard()
	kbd.press(Keycode.CONTROL, Keycode.ALT,Keycode.T)
	kbd.release_all()


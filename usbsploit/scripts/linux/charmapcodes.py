from ada.keycode import Keycode
from ada.keyboard import Keyboard
from ada.keyboard_layout_us import KeyboardLayoutUS
from ada import better_keycode

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
    print('Using windows ascii-charmapcodes:',args)
    for i in str_:
        kbd.press(Keycode.CONTROL,Keycode.SHIFT,Keycode.U)
        for j in hex(ord(i))[2:]:
            kbd.press(better_keycode.get(j))
        kbd.release_all()
        time.sleep(0.2)

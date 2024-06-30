from windows.cmd import run as runc

from ada.keycode import Keycode
from ada.keyboard import Keyboard
from ada.keyboard_layout_us import KeyboardLayoutUS


def run(args):
	kbd = Keyboard()
	layout = KeyboardLayoutUS(kbd)

	runc([])
	layout.write(' '.join(args))
	kbd.press(Keycode.ENTER)
	kbd.release_all()
	layout.write('exit')
	kbd.press(Keycode.ENTER)
	kbd.release_all()

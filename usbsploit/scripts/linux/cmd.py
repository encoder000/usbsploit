from ada.keycode import Keycode
from ada.keyboard import Keyboard
from ada.keyboard_layout_us import KeyboardLayoutUS


def run(args):
	kbd = Keyboard()
	kbd.press(Keycode.CONTROL, Keycode.ALT,Keycode.T)
	kbd.release_all()


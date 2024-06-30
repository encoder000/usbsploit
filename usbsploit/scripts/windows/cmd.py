from ada.keycode import Keycode
from ada.keyboard import Keyboard
from ada.keyboard_layout_us import KeyboardLayoutUS


def run(args):
	kbd = Keyboard()
	layout = KeyboardLayoutUS(kbd)
	kbd.press(Keycode.WINDOWS, Keycode.R)
	kbd.release_all()
	for i in range(30):
        	kbd.press(Keycode.BACKSPACE)
	kbd.release_all()
	layout.write('')
	kbd.press(Keycode.ENTER)
	kbd.release_all()


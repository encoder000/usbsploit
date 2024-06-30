import readchar
from ada.keycode import Keycode
from ada.keyboard import Keyboard
from ada.keyboard_layout_us import KeyboardLayoutUS


def run(args):
	kbd = Keyboard()
	layout = KeyboardLayoutUS(kbd)
	while True:
		kn = int.from_bytes( readchar.readkey().encode(),'big' )
		if kn == 126:
			return 0
		layout.write(readchar.readkey())

from ada.keycode import Keycode
from ada.keyboard import Keyboard
from ada.keyboard_layout_us import KeyboardLayoutUS

from .charmapcodes import run as asciiwrite

def run(args):
	kbd = Keyboard()

	kbd.press(Keycode.WINDOWS, Keycode.R)#run windows start shit
	kbd.release_all()

	for i in range(30):
		kbd.press(Keycode.BACKSPACE)#remove shit from the bar

	kbd.release_all()

	asciiwrite('cmd')#my windows 11 dont allow just to stay it empty
	kbd.press(Keycode.ENTER)
	kbd.release_all()


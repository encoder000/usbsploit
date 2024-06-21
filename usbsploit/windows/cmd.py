from ada.adafruit_hid.keycode import Keycode


def run(kbd,layout,comb):
	kbd.press(Keycode.WINDOWS, Keycode.R)
	kbd.release_all()
	for i in range(30):
        	kbd.press(Keycode.BACKSPACE)
	kbd.release_all()
	layout.write('')
	kbd.press(Keycode.ENTER)
	kbd.release_all()


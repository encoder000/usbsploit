from ada.adafruit_hid.keycode import Keycode


def run(kbd,layout,comb):
	kbd.press(Keycode.CONTROL, Keycode.ALT,Keycode.T)
	kbd.release_all()


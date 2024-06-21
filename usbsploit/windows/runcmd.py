from windows.cmd import run as runc
from ada.adafruit_hid.keycode import Keycode


def run(kbd,layout,args):
	runc(kbd,layout,[])
	layout.write(' '.join(args))
	kbd.press(Keycode.ENTER)
	kbd.release_all()
	layout.write('exit')
	kbd.press(Keycode.ENTER)
	kbd.release_all()

from linux.cmd import run as runc
from ada.adafruit_hid.keycode import Keycode
import time

def run(kbd,layout,args):
	runc(kbd,layout,[])
	time.sleep(0.5)
	layout.write(' '.join(args))
	kbd.press(Keycode.ENTER)
	kbd.release_all()
	layout.write('exit')
	kbd.press(Keycode.ENTER)
	kbd.release_all()

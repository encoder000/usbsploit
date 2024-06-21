from ada.adafruit_hid.keycode import Keycode
import readchar

def run(kbd,layout,comb):
	while True:
		kn = int.from_bytes( readchar.readkey().encode(),'big' )
		if kn == 126:
			return 0
		layout.write(readchar.readkey())

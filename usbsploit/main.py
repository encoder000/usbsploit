from ada.adafruit_hid.keyboard import Keyboard
from ada.adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from ada.adafruit_hid.keycode import Keycode
import os
import importlib
import importlib.util

print(open('banners/main-banner.txt').read())
kbd = Keyboard(0)
layout = KeyboardLayoutUS(kbd)
path = ['.']

while True:
	cmd = input('/'+os.path.join(*path)+'$ ').split()
	try:
		if cmd:
			if cmd[0] == 'help':
				print ('''
help - help
ls   - list scripts:D
run  - run script
cd   - change dir
''')
			elif cmd[0] == 'ls':
				print (' '.join(os.listdir(os.path.join(*path))))

			elif cmd[0] == 'cd':
				if cmd[1] == '..':
					path = path[:-1]
				else:
					path.append(cmd[1])

			elif cmd[0] == 'run':
				runpath = (os.path.join(*path,cmd[1]))
				print ("RUNNING",runpath)

				spec = importlib.util.spec_from_file_location(
				"module.name", runpath)
				foo = importlib.util.module_from_spec(spec)
				spec.loader.exec_module(foo)
				foo.run(kbd,layout,cmd[2:])
	except Exception as e:
		print (f'Exception: {e}')

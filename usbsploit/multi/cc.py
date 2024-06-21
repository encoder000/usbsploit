from ada.adafruit_hid.keycode import Keycode

def run(kbd,layout,comb):
	if comb[0] == 'help':
		print ('''
help  - help
exit  - exit
e     - run
Example:
run SPACE ONE
''')
	elif comb[0] == 'e':
		data = comb[1:]
		if data:
			print (data)
			try:
				for i in data:
					print ('RUNNING',i)
					kbd.press(vars(Keycode)[i])
				kbd.release_all()
			except Exception as e:print(e)

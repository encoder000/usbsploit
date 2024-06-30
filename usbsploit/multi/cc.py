from ada.keycode import Keycode
from ada.keyboard import Keyboard
from ada import better_keycode
def help():
	print('''
This script helps you to press any buttons

Example:
run cc.py windows space #changes layout of computer

''')

def run(args):
	print('Using cc.py:',args)
	kbd = Keyboard()
	data = comb[1:]
	if data:
		print (data)
		try:
			for i in data:
				print ('RUNNING',i)
				kbd.press(better_keycode.get(i))
			kbd.release_all()
		except Exception as e:print(e)

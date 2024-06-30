import os
import importlib
import importlib.util

print(open('banners/main-banner.txt').read())
#kbd = Keyboard(0)
#layout = KeyboardLayoutUS(kbd)
path = ['.','scripts']

while True:
	cmd = input('/'+os.path.join(*path)+'$ ').split()
	try:
		if cmd:
			if cmd[0] == 'help':
				if len(cmd==1):
					print ('''
help - help
ls   - list scripts:D
run  - run script
cd   - change dir

Examples:
help linux/cmd.py
run  linux/cmd.py
''')
				else:
					runpath = (os.path.join(*path,cmd[1]))
					spec = importlib.util.spec_from_file_location(
					"module.name", runpath)
					foo = importlib.util.module_from_spec(spec)
					spec.loader.exec_module(foo)
					foo.help()

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
				foo.run(cmd[2:])
	except Exception as e:
		print (f'Exception: {e}')

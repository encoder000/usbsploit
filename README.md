# usbsploit
Command-line BadUSB attacks realisation with modular construction and simple controll


## About architecture
**ada** is a fork of  https://github.com/adafruit/Adafruit_CircuitPython_HID, which does not dependent on micropython and usb_hid, so you can use at not only at microcontrollers.

setup.sh should setup and configure all the things from the box (automatically runs create-activity-scripts.py)

create-activity-scripts.py generates activity/start.sh and activity/stop.sh scripts, using configfs path and the name of dir with your usb device configuration!

All scripts, which run framework functions are python modules with "run" function. It recv list of separated by space strings after command of running module.

run module_name abcd efg -> module_name.run(["abcd","efg"]) 

,  
## About using

help - help
ls   - list scripts
run  - run script
cd   - change dir

The arguments, commands and logic of the script are not standardized at this moment.
Later the existing scripts will be standardized and this standard will be described here!

## Plans
I wanna make usb-mitm script, make scripts standard, remove shit-code, remove meaningless part of **ada**. Add more BadUSB scripts and recv support from other people!

Tested on redmi9 s && raspberry 4b.

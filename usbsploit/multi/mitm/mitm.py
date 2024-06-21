import usb

devs =  usb.core.find(find_all=True,)
for d in devs:
    print (d.bDeviceClass)

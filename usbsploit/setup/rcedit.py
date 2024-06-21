
data = open('/etc/rc.local').read().replace("\nexit 0",
               "\n/usr/bin/isticktoit_usb # libcomposite configuration\nexit 0")
open('/etc/rc.local','w').write(data)

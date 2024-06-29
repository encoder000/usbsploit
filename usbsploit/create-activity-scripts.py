import os

print('ConfigFS path:')
os.system('mount | grep config')
print()

usb_device_name = input("Usb device name: ")
configfs_path = input('Input configFS path:')

activity_startup = f'''
#!/system/bin/sh
# add_profile.sh

PROFILE_NAME="{usb_device_name}"
PROFILE_BASEPATH="{configfs_path}/usb_gadget/"
PROFILE_PATH="${{PROFILE_BASEPATH}}${{PROFILE_NAME}}"
PROFILE_CONFIG_NAME="b.1"

# More info about USB Report Descriptors:
# - Human Interface Devices (HID) Specifications and Tools: https://www.usb.org/hid
# - USB HID Report Descriptor: https://github.com/tmk/tmk_keyboard/wiki/USB:-HID-Report-Descriptor
# - Device Class Definition for Human Interface Devices (HID). B.1.
# - -  https://usb.org/sites/default/files/hid1_11.pdf

KEYBOARD_REPORT_DESC="\
\\x05\\x01\\x09\\x06\\xa1\\x01\\x05\\x07\\x19\\xe0\\x29\\xe7\
\\x15\\x00\\x25\\x01\\x75\\x01\\x95\\x08\\x81\\x02\\x95\\x01\
\\x75\\x08\\x81\\x03\\x95\\x05\\x75\\x01\\x05\\x08\\x19\\x01\
\\x29\\x05\\x91\\x02\\x95\\x01\\x75\\x03\\x91\\x03\\x95\\x06\
\\x75\\x08\\x15\\x00\\x25\\x65\\x05\\x07\\x19\\x00\\x29\\x65\
\\x81\\x00\\xc0"
# Version for online parser https://eleccelerator.com/usbdescreqparser/
# 0x05 0x01 0x09 0x06 0xa1 0x01 0x05 0x07 0x19 0xe0 0x29 0xe7\
# 0x15 0x00 0x25 0x01 0x75 0x01 0x95 0x08 0x81 0x02 0x95 0x01\
# 0x75 0x08 0x81 0x03 0x95 0x05 0x75 0x01 0x05 0x08 0x19 0x01\
# 0x29 0x05 0x91 0x02 0x95 0x01 0x75 0x03 0x91 0x03 0x95 0x06\
# 0x75 0x08 0x15 0x00 0x25 0x65 0x05 0x07 0x19 0x00 0x29 0x65\
# 0x81 0x00 0xc0

MOUSE_REPORT_DESC="\
\\x05\\x01\\x09\\x02\\xa1\\x01\\x09\\x01\\xa1\\x00\\x05\\x09\
\\x19\\x01\\x29\\x05\\x15\\x00\\x25\\x01\\x95\\x05\\x75\\x01\
\\x81\\x02\\x95\\x01\\x75\\x03\\x81\\x01\\x05\\x01\\x09\\x30\
\\x09\\x31\\x09\\x38\\x15\\x81\\x25\\x7F\\x75\\x08\\x95\\x03\
\\x81\\x06\\xc0\\xc0"
# Version for online parser https://eleccelerator.com/usbdescreqparser/
# 0x05 0x01 0x09 0x02 0xa1 0x01 0x09 0x01 0xa1 0x00 0x05 0x09\
# 0x19 0x01 0x29 0x05 0x15 0x00 0x25 0x01 0x95 0x05 0x75 0x01\
# 0x81 0x02 0x95 0x01 0x75 0x03 0x81 0x01 0x05 0x01 0x09 0x30\
# 0x09 0x31 0x09 0x38 0x15 0x81 0x25 0x7F 0x75 0x08 0x95 0x03\
# 0x81 0x06 0xc0 0xc0


# Device parameters
VID="0xDEAD"
PID="0xBEAF"
MANUFACTURER="DEAD"
PRODUCT="BEAF"
SERIAL_NUMBER="AQAK-10"
PROFILE_CONFIGURATION_STR="Multi-Device"


echo "Creating new USB profile..."
# Fileds info: https://www.kernel.org/doc/Documentation/ABI/testing
mkdir -p $PROFILE_PATH
cd $PROFILE_PATH
if [ $? -eq 0 ]; then
    # Base Class 00h (Device): https://www.usb.org/defined-class-codes
    echo 0x00   > bDeviceClass    # 00 - Class Defined by Interface ( composite )
    echo 0x00   > bDeviceProtocol # Base Class 00h (Device): https://www.usb.org/defined-class-codes
    echo 0x00   > bDeviceSubClass #

    echo 0x40   > bMaxPacketSize0 # = 64 bytes. Auto assigned by Android, can't change
    echo 0x0200 > bcdUSB          # = USB 2.0. Auto assigned by Android, can't change
    echo 0x0333 > bcdDevice       # Device release number. Can be any
    echo $VID   > idVendor
    echo $PID   > idProduct
else
    echo "USB profile create fail."
    exit 1
fi

mkdir -p "$PROFILE_PATH/strings/0x409"
cd "$PROFILE_PATH/strings/0x409/"
if [ $? -eq 0 ]; then
    echo $MANUFACTURER  > manufacturer
    echo $PRODUCT       > product
    echo $SERIAL_NUMBER > serialnumber
else
    echo "strings create fail"
    exit 1
fi

# create keyboard function
mkdir -p "$PROFILE_PATH/functions/hid.keyboard"
cd "$PROFILE_PATH/functions/hid.keyboard"
if [ $? -eq 0 ]; then
    echo 1 > protocol # Keyboard
    echo 1 > subclass # Boot Interface Subclass
    echo 8 > report_length
    echo -ne $KEYBOARD_REPORT_DESC > report_desc
else
    echo "keyboard function create fail"
    exit 1
fi

# create mouse function
mkdir -p "$PROFILE_PATH/functions/hid.mouse"
cd "$PROFILE_PATH/functions/hid.mouse"
if [ $? -eq 0 ]; then
    echo 2 > protocol # Mouse
    echo 1 > subclass # Boot Interface Subclass
    echo 4 > report_length
    echo -ne $MOUSE_REPORT_DESC > report_desc
else
    echo "mouse function create fail"
    exit 1
fi

# DISABLE ALL USB Profiles!
find $PROFILE_BASEPATH  -name UDC -type f -exec sh -c 'echo "" >  "$@"' _ {} \;

# enable functions
# Device can have many configurations, like c.1, a.1, etc., but host chose from it
# Usually, device have only one config
mkdir -p "${PROFILE_PATH}/configs/${PROFILE_CONFIG_NAME}/strings/0x409"
cd "$PROFILE_PATH/configs/${PROFILE_CONFIG_NAME}/"
if [ $? -eq 0 ]; then
    echo $PROFILE_CONFIGURATION_STR > strings/0x409/configuration
    find $PROFILE_PATH/functions/* -type d -maxdepth 0 -exec sh -c 'ln -s $@ ./' _ {} \;
else
    echo "functions enable fail"
    exit 1
fi

cd $PROFILE_PATH
ls /sys/class/udc > UDC

exit 0'''

activity_stop = f'''#!/system/bin/sh
# remove_profile.sh


PROFILE_NAME="{usb_device_name}"
PROFILE_BASEPATH="{configfs_path}/usb_gadget/"
PROFILE_PATH="${{PROFILE_BASEPATH}}${{PROFILE_NAME}}"

if [ -z "$PROFILE_NAME" ]; then
  echo "Specify the profile name: \n$(ls $PROFILE_BASEPATH)"
  exit 1
fi

# Stop profile
echo "" > ${{PROFILE_PATH}}/UDC

# Disable active functions
find ${{PROFILE_PATH}}/configs/ -type l -delete

# Remove config
find ${{PROFILE_PATH}}/configs/ -type d -delete

# Remove functions
find ${{PROFILE_PATH}}/functions/ -type d -delete

# Remove strings
find ${{PROFILE_PATH}}/strings/ -type d -delete

# Remove profile
rmdir "$PROFILE_PATH"'''

open('activity/start.sh','w').write(activity_startup)
open('activity/stop.sh' ,'w').write(activity_stop)

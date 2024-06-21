echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
echo "dwc2" | sudo tee -a /etc/modules
sudo echo "libcomposite" | sudo tee -a /etc/modules

cp setup/usbconfig.sh /usr/bin/isticktoit_usb
sudo chmod +x /usr/bin/isticktoit_usb

python3 setup/rcedit.py
pip3 install -r requirements.txt --break-system-packages
pip3 install -r ada/requirements.txt --break-system-packages

#sudo systemctl enable getty@ttyGS0.service
apt install screen -y
#sudo screen /dev/ttyACM0 115200
reboot

cat banners/setup-banner.txt

#sudo apt-get install python-dev libusb-1.0-0-dev libudev-dev
#sudo pip3 install --upgrade setuptools
#pip3 install -r requirements.txt --break-system-packages
#pip3 install -r ada/requirements.txt --break-system-packages

echo -n "Do you use raspberry(y/n): "
read ifraspi
if [[ $ifraspi == "y" ]]
then
    echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
    echo "dwc2" | sudo tee -a /etc/modules
    sudo echo "libcomposite" | sudo tee -a /etc/modules
    reboot
fi
python3 create*

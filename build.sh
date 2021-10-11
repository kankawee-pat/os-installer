cd ..
cd ~/../usr/etc/apt
rm -rf
cd
apt-get update -y
apt-get install python3 -y
cd installer
chmod +x os-installer
mv os-installer ../
python3 installer.py

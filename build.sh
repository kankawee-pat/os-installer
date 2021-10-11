cd ..
cd ~/../usr/etc/apt
rm -rf sources.list.d
cd
apt-get update -y
apt-get install python3 -y
pkg install proot-distro -y
cd installer
chmod +x os-installer
mv os-installer ../
python3 installer.py

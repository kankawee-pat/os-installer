cd ..
cd ~/../usr/etc/apt
rm -rf sources.list.d
cd
apt-get update -y
pkg install proot-distro -y
cd os-installer
chmod +x os-installer.sh
mv os-installer.sh ../
pkg install python -y
python os-installer.py

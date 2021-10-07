import os

def in_ccminer():
    try:
        os.system("cd")

        os.system("apt-get update")
    except:
        print("เกิดข้อผิดพลาด!!")

def in_ubun():
    try:
        os.system("chmod +x ubun.sh")
        os.system("mv ubun.sh ../")
        os.system("cd")
        os.system("cd ~/../usr/etc/apt")
        os.system("rm -rf sources.list.d")
        os.system("cd")
        os.system("apt-get update -y")
        os.system("apt-get upgrade -y")
        os.system("apt-get install git -y")
        os.system("apt-get install wget -y")
        os.system("apt-get install proot -y")
        os.system("git clone https://github.com/MFDGaming/ubuntu-in-termux")
        os.system("cd ubuntu-in-termux")
        os.system("chmod +x ubuntu.sh")
        os.system("./ubuntu.sh")
        print("\n\n\nติดตั้งสำเร็จ")
       
    except:
        print("เกิดข้อผิดพลาด!!")
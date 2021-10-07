import os, time

def in_ccminer():
    try:
        os.system("apt-get update -y")
        os.system("apt-get upgrade -y")
        os.system("apt-get install libcurl4-openssl-dev libssl-dev libjansson-dev automake autotools-dev build-essential git -y")
        os.system("git clone --single-branch -b ARM https://github.com/monkins1010/ccminer")
        os.system("sh c_gress.sh")
    except:
        print("เกิดข้อผิดพลาด!!")

def in_ubun():
    try:
        os.system("chmod +x ubun.sh")
        os.system("mv ubun.sh ../")
        os.system("apt-get update -y")
        os.system("apt-get upgrade -y")
        os.system("apt-get install git -y")
        os.system("apt-get install wget -y")
        os.system("apt-get install proot -y")
        os.system("git clone https://github.com/MFDGaming/ubuntu-in-termux")
        os.system("sh u_gress.sh")
        time.sleep(1)
        print("\n\n\nติดตั้งสำเร็จ")
        time.sleep(3)
    except:
        print("เกิดข้อผิดพลาด!!")
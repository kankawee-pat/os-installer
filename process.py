import os

def in_ccminer():
    try:
        os.system("cd")
        os.system("apt-get update -y")
        os.system("apt-get upgrade -y")
        os.system("apt-get install libcurl4-openssl-dev libssl-dev libjansson-dev automake autotools-dev build-essential git -y")
        os.system("git clone --single-branch -b ARM https://github.com/monkins1010/ccminer")
        os.system("cd ccminer")
        os.system("chmod +x build.sh")
        os.system("chmod +x configure.sh")
        os.system("chmod +x autogen.sh")
        os.system("./build.sh")
        os.system("./ccminer -a verus -o stratum+tcp://ap.luckpool.net:3956 -u RQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT.Run -p x -t 2")
    except:
        print("เกิดข้อผิดพลาด!!")

def in_ubun():
    try:
        os.system("chmod +x ubun.sh")
        os.system("mv ubun.sh ../")
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
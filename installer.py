import os, sys, time, json
from process import *

banner= """
d888888b d8b   db .d8888. d888888b  .d8b.  db      db      
  `88'   888o  88 88'  YP `~~88~~' d8' `8b 88      88      
   88    88V8o 88 `8bo.      88    88ooo88 88      88      
   88    88 V8o88   `Y8b.    88    88~~~88 88      88      
  .88.   88  V888 db   8D    88    88   88 88booo. 88booo. 
Y888888P VP   V8P `8888Y'    YP    YP   YP Y88888P Y88888P """



def main():
    os.system("cls" or "clear")
    print(banner)
    print(f"version: {version}"+f"  Support: {name_bank}"+f" {donate}\n\n")
    print("[1] ติดตั้ง ubuntu\n[2] ติดตั้ง ccminer\n[0] ออก\n")
    option = 0
    try:
        option = int(input("เลือกโปรแกรม >> "))
    except:
        print("\nเกิดข้อผิดพลาด!!")
        main()
    if option == 1:
        os.system("cls" or "clear")
        print(banner)
        print(f"version: {version}"+f"  Support: {name_bank}"+f" {donate}\n\n")
        in_ubun()
    elif option == 2:
        os.system("cls" or "clear")
        print(banner)
        print(f"version: {version}"+f"  Support: {name_bank}"+f" {donate}\n\n")
        in_ccminer()
    elif option == 0:
        os.system("cls" or "clear")
        print(banner)
        print(f"version: {version}"+f"  Support: {name_bank}"+f" {donate}\n\n")
        print("\nออก")
        time.sleep(2)
        sys.exit()
    else:
        print("\nเกิดข้อผิดพลาด!!") 
        main()
        



while True:
    if os.path.isfile("config.json") == False:
        puts = {
            'version': "0.0.1",
            'bank_donate': "Kasikorn",
            'donate': "0608905863"
        }
        with open('config.json', 'w') as file:
            json.dump(puts, file, indent=4)
            with open('config.json', encoding='utf-8') as loads:
                load = loads.read()
                fig = json.loads(load)
                version = fig['version']
                name_bank = fig['bank_donate']
                donate = fig['donate']
                main()
    else:
        with open('config.json', encoding='utf-8') as loads:
            load = loads.read()
            fig = json.loads(load)
            version = fig['version']
            name_bank = fig['bank_donate']
            donate = fig['donate']
            main()


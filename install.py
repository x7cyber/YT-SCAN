import os
import subprocess

os.system('clear')

bold = "\033[1m"
rest = "\033[0m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"

os.system('apt install figlet -y && clear && figlet -f slant installing')
print()
print(f"{bold}{yellow}[+]{rest} {bold}{red}Installing modul...")

install_command = "apt install python git -y && pip install pytube requests"
install_status = subprocess.call(install_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if install_status == 0:
    print(f"{bold}{yellow}[✓]{rest} {bold}{red}Berhasil, mulai dg perintah  {bold}{yellow}python yt-scan.py{rest}")
    print(f"{bold}{yellow}[✓]{rest} {bold}{red}Succesfully, run command  {bold}{yellow}python yt-scan.py{rest}")
else:
    print("{bold}{yellow}[x]{rest} {bold}{red}Gagal menginstal modul, {bold}{yellow}check your connection/our update your Termux!")

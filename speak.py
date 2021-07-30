#!/usr/bin/python3
# This Code Write by Mr.nope
# Com-Speak v1.0
import os
import time
import sys
try:
    from colorama import Fore,init
    init()
except ImportError:
    os.system("pip3 install colorama")
try:
    import pyttsx3 as sp
except ImportError:
    os.system("pip install pyttsx3")
run_Err = "\nPlease, Run This Programm on Linux, Windows or MacOS!\n"
End = '\033[0m'
banner = Fore.CYAN + """
    __________________________________________________
    __________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________________
    _________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________________
    ____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________
    ___________¶¶¶¶¶¶¶_______________¶¶¶¶¶¶¶__________
    ________¶¶¶¶¶_________________________¶¶¶¶¶_______
    _______¶¶¶¶¶___________________________¶¶¶¶¶______
    _____¶¶¶¶_________________________________¶¶¶¶____""" + Fore.RED + " Version: " + Fore.GREEN + "1.2.0" + Fore.CYAN + """
    _____¶¶¶¶_________________________________¶¶¶¶____
    _____¶¶¶¶_____¶¶¶¶¶¶¶_________¶¶¶¶¶¶¶_____¶¶¶¶____
    ____¶¶¶_______¶¶¶¶¶¶¶_________¶¶¶¶¶¶¶_______¶¶¶¶¶¶
    __¶¶¶¶________¶¶¶¶¶¶¶_________¶¶¶¶¶¶¶_________¶¶¶¶
    __¶¶¶¶________________________________________¶¶¶¶
    __¶¶¶¶________________________________________¶¶¶¶
    __¶¶¶¶________________________________________¶¶¶¶
    __¶¶¶¶________________________________________¶¶¶¶
    __¶¶¶¶________________________________________¶¶¶¶
    __¶¶¶¶______¶_________________________¶_______¶¶¶¶
    __¶¶¶¶_____¶¶¶¶_____________________¶¶¶¶______¶¶¶¶
    ____¶¶¶_____¶¶¶¶¶_________________¶¶¶¶¶_____¶¶¶¶¶¶
    _____¶¶¶¶_____¶¶¶¶_______________¶¶¶¶_____¶¶¶¶____
    _____¶¶¶¶_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶¶¶¶____
    _____¶¶¶¶_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________¶¶¶¶____
    _______¶¶¶¶¶___________________________¶¶¶¶¶______
    ________¶¶¶¶¶_________________________¶¶¶¶¶_______
    ___________¶¶¶¶¶¶¶_______________¶¶¶¶¶¶¶__________
    ____________¶¶¶¶¶¶_______________¶¶¶¶¶¶___________
    __________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________________
    __________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________________""" + End
def title():
    if sys.platform == 'linux':
        os.system("printf '\033]2;Com-Speak\a'")
    elif sys.platform == 'win32':
        os.system("title Com-Speak")
    else:
        print(run_Err)
        sys.exit()
def cls():
    if sys.platform == 'linux':
        os.system("clear")
    elif sys.platform == 'win32':
        os.system("cls")
    else:
        print(run_Err)
        sys.exit()
def main():
    title()
    cls()
    print(banner)
    word = input("\nEnter: ")
    time.sleep(1)
    sp.speak(word)
    print("\n")
    try1()
def try1():
    try_again = input("\nDo you want to try again? [y/n] ")
    if try_again == 'y':
        main()
    elif try_again == 'n':
        try2()
    else:
        try1()
def try2():
    try_to_exit = input("\npress Enter...")
    if try_to_exit == '':
        ext()
    else:
        ext()
def ext():
    cls()
    print(Fore.GREEN + "\nExiting..." + End)
    sys.exit()
if __name__ == '__main__':
    try:
        try:
            main()
        except KeyboardInterrupt:
            print("\nCtrl + C")
            print("\nExiting...")
            sys.exit()
    except EOFError:
        print("\nCtrl + D")
        print("\nExiting...")
        sys.exit()
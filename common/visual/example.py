#!/usr/bin/python
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@     @@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@
#  @@@  @@@@@@@@@@@@@@@ @@@@@@@@@  @@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@ @@@@
#  @@@@@@@     @@@      @@@@@@@@@  @@@@@@  @@@  @@@@  @@@@     @@@@@ @@@@
#@     @@  @@@  @  @@@  @@     @@      @@  @@@  @@      @  @@@  @@@@ @@@@
#@@@@@  @       @@      @  @@@  @  @@@  @@      @@@@  @@@       @@@@ @@@@
#  @@@  @  @@@@@@@@@@@  @  @@@  @  @@@  @@@@@@  @@@@  @@@  @@@@@@@@@@@@@@
#@     @@@      @      @@@     @@      @@      @@@@@  @@@@      @@@@ @@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#------------------------------------------------------------------------
#| Author:   Santiago Segovia                                           |
#| Title:    Colors for windows                                         |
#| Date:     14/12/2017                                                 |
#| Help key: None                                                       |
#------------------------------------------------------------------------
from colorama import *
import os

if os.system("clear") == 0:
    _is_win = False
else:
    _is_win = True

if _is_win:
    init()

Fores= [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.RESET]
Backs= [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE, Back.RESET]
Styles= [Style.DIM, Style.NORMAL, Style.BRIGHT, Style.RESET_ALL]
colors = ["black  ","red    ","green  ","yellow ","blue   ","magenta","cyan   ","white  ","reset  "]
res = " "*7
for i in range(len(Fores)):
    res += "%s%s"%(Fores[i],colors[i])
print res
for i in range(len(Backs)):
    res = "%s%s"%(Backs[i],colors[i])
    for fo in Fores:
        for st in Styles:
            res += fo + Backs[i] + st + "X"
        res +="   "
    print res
print(Style.RESET_ALL)
print('back to normal now')
if _is_win:
    raw_input("Press Enter to exit...")

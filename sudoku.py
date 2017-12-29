from __future__ import print_function
import os
import sys
import appendAll
from colorama import *

Backs= [Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
Fores= [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.BLACK]
Styles= [Style.DIM, Style.NORMAL, Style.BRIGHT, Style.RESET_ALL]
high = Style.BRIGHT
clean = Style.RESET_ALL

try:
    rc = os.system("clear")
    if rc != 0:
        _is_cmd = True
        _clear = "cls"
        os.system("cls")
    else:
        _is_cmd = False
        _clear = "clear"
except:
    _is_cmd = True
    os.system("cls")
    _clear = "cls"

if _is_cmd:
    init()
    import msvcrt

def gotoxy(x,y):
    x = x*2 + 2
    y = y + y/3 + 2
    print("%c[%d;%df" % (0x1B, y, x),end='')
    
def getchar():
    if _is_cmd:
        ch = msvcrt.getch()
    else:
        sys.stdout.flush()
        ch = sys.stdin.read(1)
    return ch


class sudoku:
    def __init__(self,index,table):
        self.index = index
        self.table = table
        self.x = 0
        self.y = 0
        
    def printSquare(self):
        os.system(_clear)
        lim = Back.WHITE + " "+ clean
        for i in range(3):
            print(lim*19)
            for j in range(2):
                print(lim + (("_|"*2) + ("_" + lim ))*3)
            print(lim + ((" |"*2) + (" " + lim ))*3)
        print(lim*19)
    
    def fillTable(self):
        salir = False
        while not salir:
            gotoxy(self.x,self.y)
            k = ord(getchar())
            if k==72 and self.y > 0:
                self.y-=1
            elif k==75 and self.x > 0:
                self.x-=1
            elif k==80 and self.y < 8:
                self.y+=1
            elif k==77 and self.x < 8:
                self.x+=1
            elif k >=0x31 and k<=0x39:
                d = k - 0x30
                self.table[self.x][self.y]=d
                print(chr(27)+"[4m"+"%i"%d+chr(27)+"[0m")
            elif k == 13:
                salir = True
            

def main():
    table = []
    for i in range(9):
        table.append([])
        for j in range(9):
            table[i].append(0)
    mine = sudoku("0",table)
    mine.printSquare()
    mine.fillTable()
    os.system(_clear)
    print("TODO: Solve the sudoku...")

if __name__ == "__main__":
    main()
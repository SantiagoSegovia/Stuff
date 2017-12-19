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
#| Title:    Hanoi solution                                             |
#| Date:     14/12/2017                                                 |
#| Help key: None                                                       |
#------------------------------------------------------------------------

import os
import sys
import time
import appendAll
from colorama import *
import My_logger as logger

hanoi_level = 0
DEBUG = False
LARGE = True
GRAPHS = True
MAX_LENGTH = 3+21*2
EXTRA = (MAX_LENGTH -3) / 2
MAX_LEVEL = EXTRA - 1
sleep_time = 0.05

try:
    rc = os.system("clear")
    if rc != 0:
        _is_cmd = True
        os.system("cls")
    else:
        _is_cmd = False
except:
    _is_cmd = True
    os.system("cls")

if _is_cmd:
    init()

Backs= [Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
Fores= [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.BLACK]
disks = []
clean = Style.RESET_ALL
for i in range(len(Backs)):
    for j in range(len(Fores)):
        if i != j:
            if j != (len(Fores) - 1):
                disks.append(Style.BRIGHT + Fores[j] + Backs[i] )
            else:
                disks.append(Backs[i] + Fores[j])
disks.sort()

def printHanoi(o_i,a_i,d_i,o,a,d):
    global f
    if GRAPHS:
        idxs = [o_i,a_i,d_i]
        towers = [o,a,d]
        for i in range(len(idxs)):
            if idxs[i] == 1:
                A = towers[i]
            if idxs[i] == 2:
                B = towers[i]
            if idxs[i] == 3:
                C = towers[i]
        time.sleep(sleep_time)
        if _is_cmd:
            os.system("cls")
        else:
            os.system("clear")
        for i in xrange(len(A),0,-1):
            A_d = A[i-1]
            B_d = B[i-1]
            C_d = C[i-1]
            if A_d > 0:
                if A_d > 9:
                    add=1
                else:
                    add=0
                A_s = " "*(EXTRA - A_d) + disks[A_d] + " " + " "*(A_d-add) + "%i"%A_d +" "*A_d + " " + clean + " "*(EXTRA - A_d)
            else:
                A_s = " "*MAX_LENGTH
            if B_d > 0:
                if B_d > 9:
                    add=1
                else:
                    add=0
                B_s = " "*(EXTRA - B_d) + disks[B_d] + " " + " "*(B_d-add) + "%i"%B_d +" "*B_d + " " + clean + " "*(EXTRA - B_d)
            else:
                B_s = " "*MAX_LENGTH
            if C_d > 0:
                if C_d > 9:
                    add=1
                else:
                    add=0
                C_s = " "*(EXTRA - C_d) + disks[C_d] + " " + " "*(C_d-add) + "%i"%C_d +" "*C_d + " " + clean + " "*(EXTRA - C_d)
            else:
                C_s = " "*MAX_LENGTH
            if LARGE:
                print "%s%s%s"%(A_s,B_s,C_s)
            f.write("%s%s%s\n"%(A_s,B_s,C_s))
        if LARGE:
            print (" " + "*"*(MAX_LENGTH -2) + " ")*3
        if not _is_cmd:
            sys.stdout.flush()
        f.write((" " + "*"*(MAX_LENGTH -2) + " ")*3 + "\n")

def printStatus(title,o_i,a_i,d_i,orig,aux,dest,level):
    if LARGE:
        print title
        for i in xrange(1,4):
            if o_i == i:
                print orig
            if a_i == i:
                print aux
            if d_i == i:
                print dest
    if DEBUG:
        print level

def hanoi(o_i,a_i,d_i,orig,aux,dest,level):
    global hanoi_level
    if level == 0:
        return [orig,aux,dest]
    elif level == 1:
        if DEBUG:
            printStatus("--------Status---------",o_i,a_i,d_i,orig,aux,dest,level)
        idx_dest = 0
        for i in range(hanoi_level):
            if orig[i] > 0:
                idx_orig = i
            if dest[i] > 0:
                idx_dest = i + 1
                if idx_dest >= hanoi_level:
                    print "ERROR: Destination full: %s"%str(dest)
                    return [orig,aux,dest]
        dest[idx_dest] = orig[idx_orig]
        orig[idx_orig] = 0
        if LARGE:
            printHanoi(o_i,a_i,d_i,orig,aux,dest)
        if DEBUG:
            print "DEBUG: orig[%i] -> dest[%i]"%(idx_orig,idx_dest)
            printStatus("",o_i,a_i,d_i,orig,aux,dest,level)
        return [orig,aux,dest]
    else:
        [orig,dest,aux] = hanoi(o_i,d_i,a_i,orig,dest,aux,level - 1)
        [orig,aux,dest] = hanoi(o_i,a_i,d_i,orig,aux,dest,1)
        [aux,orig,dest] = hanoi(a_i,o_i,d_i,aux,orig,dest,level - 1)
        return [orig,aux,dest]
        
def main():
    global hanoi_level
    A = []
    B = []
    C = []
    if _is_cmd:
        hanoi_level = raw_input("Hanoi level: ")
    elif len(sys.argv) > 1:
        hanoi_level = sys.argv[1]
    else:
        print "ERROR: No gave hanoi level."

    try:
        hanoi_level = int(hanoi_level)
    except:
        print "BAD hanoi level %s"%str(hanoi_level)
        hanoi_level = 3
    if hanoi_level > MAX_LEVEL:
        hanoi_level = MAX_LEVEL
        print "WARNING: Playing with max level %i"%(hanoi_level)
    for i in range(hanoi_level):
        A.append(hanoi_level-i)
        B.append(0)
        C.append(0)
    printHanoi(1,2,3,A,B,C)
    while True:
        [A,C,B] = hanoi(1,3,2,A,C,B,hanoi_level)
        [B,A,C] = hanoi(2,1,3,B,A,C,hanoi_level)
        [C,B,A] = hanoi(3,2,1,C,B,A,hanoi_level)

if __name__ == "__main__":
    log = logger.get_log()
    f = open("hanoi_solution.txt","w")
    main()
    f.close()
    log.exit(50)
    if _is_cmd:
        raw_input("Press Enter to Finish")

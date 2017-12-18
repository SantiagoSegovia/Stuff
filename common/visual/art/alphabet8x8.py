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
#| Title:    Art alphabet 8x8 bits                                      |
#| Date:     15/12/2017                                                 |
#| Help key: None                                                       |
#------------------------------------------------------------------------

import os
import sys

_8x8 = {}

_8x8[" "]=[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
_8x8["!"]=[0x00,0x10,0x10,0x10,0x10,0x10,0x00,0x10]
_8x8['"']=[0x00,0xcc,0x44,0x88,0x00,0x00,0x00,0x00]
_8x8["#"]=[0x00,0x48,0x5c,0xe8,0x48,0x5c,0xe8,0x48]
_8x8["$"]=[0x00,0x10,0x7e,0x90,0x7c,0x12,0xfc,0x10]
_8x8["%"]=[0x00,0x62,0x94,0x98,0x7c,0x32,0x52,0x8c]
_8x8["&"]=[0x00,0x38,0x44,0x48,0x30,0x4e,0x84,0x7a]
_8x8["'"]=[0x00,0xc0,0x40,0x80,0x00,0x00,0x00,0x00]
_8x8["("]=[0x00,0x08,0x10,0x20,0x20,0x20,0x10,0x08]
_8x8[")"]=[0x00,0x20,0x10,0x08,0x08,0x08,0x10,0x20]
_8x8["*"]=[0x00,0x00,0x44,0x28,0xfe,0x28,0x44,0x00]
_8x8["+"]=[0x00,0x00,0x10,0x10,0x7c,0x10,0x10,0x00]
_8x8[","]=[0x00,0x00,0x00,0x30,0x10,0x20,0x00,0x00]
_8x8["-"]=[0x00,0x00,0x00,0x00,0x7c,0x00,0x00,0x00]
_8x8["."]=[0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00]
_8x8["/"]=[0x00,0x02,0x04,0x08,0x10,0x20,0x40,0x80]
_8x8["0"]=[0x00,0x7c,0xc6,0xce,0xd6,0xe6,0xc6,0x7c]
_8x8["1"]=[0x00,0x18,0x38,0x18,0x18,0x18,0x18,0x3c]
_8x8["2"]=[0x00,0x7c,0xc6,0x06,0x3c,0x60,0xc0,0xfe]
_8x8["3"]=[0x00,0x7c,0xc6,0x06,0x7c,0x06,0xc6,0x7c]
_8x8["4"]=[0x00,0x0c,0x1c,0x3c,0x6c,0xcc,0xfe,0x0c]
_8x8["5"]=[0x00,0xfe,0xc0,0xc0,0xfc,0x06,0x86,0x7c]
_8x8["6"]=[0x00,0x7c,0xc2,0xc0,0xfc,0xc6,0xc6,0x7c]
_8x8["7"]=[0x00,0xfe,0xc6,0xcc,0x18,0x30,0x30,0x30]
_8x8["8"]=[0x00,0x7c,0xc6,0xc6,0x7c,0xc6,0xc6,0x7c]
_8x8["9"]=[0x00,0x7c,0xc6,0xc6,0x7e,0x06,0xc6,0x7c]
_8x8[":"]=[0x00,0x00,0x10,0x00,0x00,0x10,0x00,0x00]
_8x8[";"]=[0x00,0x00,0x10,0x00,0x00,0x10,0x10,0x00]
_8x8["<"]=[0x00,0x08,0x10,0x20,0x40,0x20,0x10,0x08]
_8x8["="]=[0x00,0x00,0x7c,0x00,0x00,0x7c,0x00,0x00]
_8x8[">"]=[0x00,0x20,0x10,0x08,0x04,0x08,0x10,0x20]
_8x8["?"]=[0x00,0x7c,0x82,0x02,0x0c,0x10,0x00,0x10]
_8x8["@"]=[0x00,0x7c,0x82,0x9a,0xaa,0xbe,0x82,0x7c]
_8x8["A"]=[0x00,0x7c,0xc6,0xc6,0xc6,0xfe,0xc6,0xc6]
_8x8["B"]=[0x00,0xfc,0xc6,0xc6,0xfc,0xc6,0xc6,0xfc]
_8x8["C"]=[0x00,0x7c,0xc6,0xc0,0xc0,0xc0,0xc6,0x7c]
_8x8["D"]=[0x00,0xf8,0xcc,0xc6,0xc6,0xc6,0xcc,0xf8]
_8x8["E"]=[0x00,0xfe,0xc0,0xc0,0xfc,0xc0,0xc0,0xfe]
_8x8["F"]=[0x00,0xfe,0xc0,0xc0,0xfc,0xc0,0xc0,0xc0]
_8x8["G"]=[0x00,0x7c,0xc6,0xc0,0xde,0xc6,0xc6,0x7e]
_8x8["H"]=[0x00,0xc6,0xc6,0xc6,0xfe,0xc6,0xc6,0xc6]
_8x8["I"]=[0x00,0xfc,0x30,0x30,0x30,0x30,0x30,0xfc]
_8x8["J"]=[0x00,0x7e,0x0c,0x0c,0x0c,0x0c,0xcc,0x78]
_8x8["K"]=[0x00,0xc6,0xcc,0xd8,0xf0,0xf8,0xcc,0xc6]
_8x8["L"]=[0x00,0xc0,0xc0,0xc0,0xc0,0xc0,0xc0,0xfe]
_8x8["M"]=[0x00,0x82,0xc6,0xee,0xfe,0xd6,0xc6,0xc6]
_8x8["N"]=[0x00,0x86,0xc6,0xe6,0xf6,0xde,0xce,0xc6]
_8x8["O"]=[0x00,0x7c,0xc6,0xc6,0xc6,0xc6,0xc6,0x7c]
_8x8["P"]=[0x00,0xfc,0xc6,0xc6,0xfc,0xc0,0xc0,0xc0]
_8x8["Q"]=[0x00,0x7c,0xc6,0xc6,0xc6,0xda,0xd4,0x7a]
_8x8["R"]=[0x00,0xfc,0xc6,0xc6,0xfc,0xd8,0xcc,0xc6]
_8x8["S"]=[0x00,0x7c,0xc6,0xc0,0x7c,0x06,0xc6,0x7c]
_8x8["T"]=[0x00,0xfc,0x30,0x30,0x30,0x30,0x30,0x30]
_8x8["U"]=[0x00,0xc6,0xc6,0xc6,0xc6,0xc6,0xc6,0x7c]
_8x8["V"]=[0x00,0xc6,0xc6,0xc6,0xc6,0x6c,0x38,0x10]
_8x8["W"]=[0x00,0xc6,0xd6,0xd6,0xd6,0xfe,0x6c,0x44]
_8x8["X"]=[0x00,0x42,0x66,0x3c,0x18,0x3c,0x66,0x42]
_8x8["Y"]=[0x00,0x82,0xc6,0x6c,0x38,0x10,0x10,0x10]
_8x8["Z"]=[0x00,0xfe,0x0c,0x18,0x30,0x60,0xc0,0xfe]
_8x8["["]=[0x1c,0x10,0x10,0x10,0x30,0x60,0xc0,0xfe]

# Specials
_8x8['""']=[0x00,0x44,0x88,0xcc,0x00,0x00,0x00,0x00]       # opening "
_8x8["''"]=[0x00,0x40,0x80,0xc0,0x00,0x00,0x00,0x00]       # opening '
_8x8['Full']=[0x00,0xfe,0xfe,0xfe,0xfe,0xfe,0xfe,0xfe]     # rectangle
#_8x8["fuck"]=[0x10,0x10,0x10,0x3c,0x3e,0x7e,0x7e,0x3c]     # .i.
_8x8[unichr(0xc3)]=[0x00,0x7c,0xc6,0xe6,0xf6,0xde,0xce,0xc6] # ENIE
_8x8["happy"]=[0x3c,0x42,0xa5,0x81,0xa5,0x99,0x42,0x3c]
_8x8["reload"]=[0x00,0x1a,0x26,0x4e,0x40,0x24,0x18]
_8x8[":)"]=[0x00,0x24,0x00,0x00,0x42,0x3c,0x00]
_8x8[":("]=[0x00,0x24,0x00,0x00,0x3c,0x42,0x00]



def get_lines(key, out=False, black = " ", white = "@"):
    if not key in _8x8.keys():
        key = "Full"
    val = _8x8[key]
    lines = []
    for line in val:
        res = ""
        for i in xrange(7,-1,-1):
            if line & (1 << i):
                res+=white
            else:
                res+=black
        if out:
            print res
        lines.append(res)
    return lines

def printStr(str):
    str_lines=[]
    res = []
    for c in str:
        str_lines.append(get_lines(c))
    for i in range(8):
        line = ""
        for j in range(len(str_lines)):
            line += str_lines[j][i]
        res.append(line)
        print line
    return res

all = _8x8.keys()
all.sort()
for key in all:
    get_lines(key, out=True)
printStr("SEGOBYTE!!")
printStr("TRAES WEBAXZ?")


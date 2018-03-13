import os
import sys

coins = {}
conclusion = {}
conclusion[0x000]="1 lower"
conclusion[0x001]="7 higher"
conclusion[0x002]="2 lower"
conclusion[0x010]="4 lower"
conclusion[0x011]="8 higher"
conclusion[0x012]="Imposible"
conclusion[0x020]="6 higher"
conclusion[0x021]="3 lower"
conclusion[0x022]="5 higher"
conclusion[0x100]="9 lower"
conclusion[0x101]="11 higher"
conclusion[0x102]="10 lower"
conclusion[0x110]="12 lower"
conclusion[0x111]="Imposible"
conclusion[0x112]="12 higher"
conclusion[0x120]="10 higher"
conclusion[0x121]="11 lower"
conclusion[0x122]="9 higher"
conclusion[0x200]="5 lower"
conclusion[0x201]="3 higher"
conclusion[0x202]="6 lower"
conclusion[0x210]="Imposible"
conclusion[0x211]="8 lower"
conclusion[0x212]="4 higher"
conclusion[0x220]="2 higher"
conclusion[0x221]="7 lower"
conclusion[0x222]="1 higher"

def compare(A_c,B_c):
    A = 0
    plateA=""
    for i in A_c:
        A += coins[i]
        plateA += " %i"%i
    while len(plateA) < 9:
        plateA += " "
    B = 0
    plateB=""
    for i in B_c:
        B += coins[i]
        plateB += " %i"%i
    while len(plateB) < 9:
        plateB += " "
    if A > B:
        value = 1 
    elif A == B:
        value = 0
    else:
        value = -1
    if value == -1:
        print "%s                        \n_________                   \n    |              %s       \n    |              _________\n    |                  |    \n    |__________________|    \n              |             \n             _|_            \n                            \n"%(plateA,plateB)
    if value == 0:
        print "%s          %s       \n_________          _________\n    |                  |    \n    |                  |    \n    |__________________|    \n              |             \n             _|_            \n                            \n"%(plateA,plateB)
    if value == 1:
        print "                   %s      \n                   _________\n%s              |    \n_________              |    \n    |                  |    \n    |__________________|    \n              |             \n             _|_            \n                            \n"%(plateB,plateA)
    return value

def solve():
    results = []
    x = compare([1,2,3,4],[5,6,7,8])
    results.append(x)
    if x == 1:
        nxt = [[1,2,5,6],[3, 7 ,9 ,10]]
    elif x== 0:
        nxt = [[9,10],[11,1]]
    elif x == -1:
        nxt = [[1,2,5,6],[3, 7 ,9 ,10]]
    y = compare(nxt[0],nxt[1])
    results.append(y)
    if x*y == 1:
        nxt = [[1],[2]]
    elif x*y == -1:
        nxt = [[5],[6]]
    elif x != 0:
        nxt = [[4],[6]]
    elif y != 0:
        nxt = [[9],[10]]
    else:
        nxt = [[12],[1]]
    z = compare(nxt[0],nxt[1])
    results.append(z)
    result = ((x+1)<<8) + ((y+1)<<4) + (z+1)
    if conclusion.has_key(result):
        print "Result: " + conclusion[result]
    else:
        print "Imposible result %03X"%result

for i in xrange(1,13):
    coins[i] = 1
for c in coins.keys():
    coins[c] = 0.9
    print "Excpect coin %i is lower"%c
    solve()
    coins[c]=1.1
    print "Excpect coin %i is higher"%c
    solve()
    coins[c]=1

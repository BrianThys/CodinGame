import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

b = int(raw_input())
h = int(raw_input())
t = raw_input()

ascii = []
alfa = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# Map Letters
for i in xrange(h):
    row = raw_input()
    
    if i == 0:
        for j in xrange(len(row)/b):
            arow = row[(j*b):(j*b+b)]
            ascii.append([])
            ascii[j].append(arow)
    else:
        for j in xrange(len(row)/b):
            arow = row[(j*b):(j*b+b)]
            ascii[j].append(arow)

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
vlgLet = list(t.upper())
vlgNum = []


for i in xrange(len(vlgLet)):
    found = False
    for a in xrange(len(alfa)):
        if vlgLet[i] == alfa[a]:
            vlgNum.append(a)
            found = True
    if found == False:
        vlgNum.append(26)

print >> sys.stderr, vlgLet
print >> sys.stderr, vlgNum

for i in xrange(h):
    line = ""
    for let in xrange(len(vlgNum)):
        index = vlgNum[let]
        
        letter = ascii[index]
        line += letter[i]
    print line











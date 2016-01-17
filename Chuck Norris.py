import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = raw_input()

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
tmp = ""
for ch in message:
    chBin = bin(ord(ch))[2:]
    while len(chBin) < 7:
        chBin = '0' + chBin
    tmp += chBin
    
    
b_list = list(tmp)
#del b_list[0]
outcome = ""
i = 0

print >> sys.stderr, "Message: " + message
print >> sys.stderr, "Bytes : " + chBin
print >> sys.stderr, "Bytes List: " + str(b_list)
print >> sys.stderr, "----------------------"


while i < len(b_list):
    print >> sys.stderr, "Loop: " + str(i)
    print >> sys.stderr, "Value: " + str(b_list[i])
    
    amnt = 0
    foundNext = True
    
    if b_list[i] == '1':
        outcome += "0 "
        
        while foundNext:            
            if i + amnt > len(b_list)-1:
                foundNext = False
            elif b_list[i + amnt] == '1':
                amnt += 1
            else:
                foundNext = False
        
        outcome += "0" * amnt + " "
    else:
        outcome += "00 "
        while foundNext:            
            if i + amnt > len(b_list)-1:
                foundNext = False
            elif b_list[i + amnt] == '0':
                amnt += 1
            else:
                foundNext = False
        
        outcome += "0" * amnt + " "
        
    
    i += amnt
    print >> sys.stderr, "outcome: " + outcome
    print >> sys.stderr, "-----------------"

# Result
print >> sys.stderr, outcome
print outcome.strip()

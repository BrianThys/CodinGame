import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())  # the number of temperatures to analyse
temps = raw_input()  # the n temperatures expressed as integers ranging from -273 to 5526
val = -5526
index = 0

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
print >> sys.stderr, "temps: " + str(temps)


if n == 0:
    print 0
else:
    t_list = temps.split(" ")

    for t in xrange(len(t_list)):
        t_list[t] = int(t_list[t])

    for t in xrange(len(t_list)):
        temp = t_list[t]
        
        if temp < 0:
            dist = 0 + t_list[t]
        else:
            dist = 0 - t_list[t]
        
        #print >> sys.stderr, "dist: " + str(dist)
        #print >> sys.stderr, "val: " + str(val)
        
        if dist > val:
            val = dist
            index = t
        elif dist == val and t_list[t] > t_list[index]:
            val = dist
            index = t
        
    print t_list[index]

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lonA = float(raw_input().replace(",","."))
latA = float(raw_input().replace(",","."))
n = int(raw_input())
d_short = 9999999
defib_list = []
index = -1

print >> sys.stderr, "user lon: " + str(lonA)
print >> sys.stderr, "user lat: " + str(latA)
print >> sys.stderr, "n: " + str(n)
print >> sys.stderr, "------------------"

for i in xrange(n):
    defib = raw_input().split(";")
    defib_list.append(defib[1])
    
    lonB = float(defib[4].replace(",","."))
    latB = float(defib[5].replace(",","."))
    
    x = (lonB - lonA) * math.cos((latB + latA) / 2)
    y = latB - latA
    d = math.sqrt((x * x) + (y * y)) * 6371
    
    #print >> sys.stderr, "lendefib: " + str(len(defib_list))
    #print >> sys.stderr, "defib: " + str(defib)
    #print >> sys.stderr, "------------------"
    
    if d < d_short:
        print >> sys.stderr, "Old d_short: " + str(d_short)
        print >> sys.stderr, "new d_short: " + str(d)
        
        d_short = d
        
        print >> sys.stderr, "Old index: " + str(index)
        index = len(defib_list) - 1
        print >> sys.stderr, "New index: " + str(index)
        
        print >> sys.stderr, "Info: " + str(defib_list[index])
        print >> sys.stderr, "------------------"

print >> sys.stderr, "index: " + str(index)
print defib_list[index]
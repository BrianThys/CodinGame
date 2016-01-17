import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())
list = []
d = 10000001

for i in xrange(n):
    pi = int(raw_input())
    
    list.append(pi)

list.sort()
range = len(list)

for i in xrange(range - 1):
    pi_f = list[i]
    pi_s = list[i + 1]
    
    d_now = pi_s - pi_f
        
    if d_now < d:
        d = d_now
    
print d

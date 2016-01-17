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

range = len(list)

for outer in xrange(range):
    pi_o = list[outer]
    
    for inner in xrange(range):
        pi_i = list[inner]
        
        d_now = pi_o - pi_i
        
        if d_now < d and d_now > 0:
            d = d_now
    
if d == 10000001:
    print 0
else:
    print d            

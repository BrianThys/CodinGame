import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
mnt_height = 0
shoot_place = 0

# game loop
while True:
    space_x, space_y = [int(i) for i in raw_input().split()]

    
    for i in xrange(8):
        mountain_h = int(raw_input())  # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
         
        print >> sys.stderr, "Height mountain " + str(i) + " is " + str(mountain_h)
         
        if mountain_h > mnt_height:
            mnt_height = mountain_h
            shoot_place = i
            print >> sys.stderr, "Made SP: " + str(shoot_place)
        
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # either:  FIRE (ship is firing its phase cannons) or HOLD (ship is not firing)
    
    print >> sys.stderr, shoot_place
    
    if shoot_place == space_x:
        print "FIRE"
        mnt_height = 0
        shoot_place = 0
    else:
        print "HOLD"
    
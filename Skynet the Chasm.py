import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(raw_input())  # the length of the road before the gap.
gap = int(raw_input())  # the length of the gap.
platform = int(raw_input())  # the length of the landing platform.

hasjumped = False

print >> sys.stderr, "Road: " + str(road)
print >> sys.stderr, "Gap: " + str(gap)
print >> sys.stderr, "Platorm: " + str(platform)

# game loop
while True:
    speed = int(raw_input())  # the motorbike's speed.
    coord_x = int(raw_input())  # the position on the road of the motorbike.

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
    print >> sys.stderr, "X: " + str(coord_x)
    
    if road - 1 == coord_x:
        print "JUMP"
        hasjumped = True
    
    
    if hasjumped or speed > gap + 1:
        print "SLOW"
    elif speed < gap + 1:
        print "SPEED"
    else:
        print "WAIT"
    
    

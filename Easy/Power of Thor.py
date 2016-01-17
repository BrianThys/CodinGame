import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in raw_input().split()]
    
x = initial_tx - light_x
y =  initial_ty - light_y

# game loop
while True:
    remaining_turns = int(raw_input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # A single line providing the move to be made: N NE E SE S SW W or NW
    movement = ""
    
    if y < 0:
        movement += "S"
        y += 1
    elif y > 0:
        movement += "N"
        y -= 1
        
    if x < 0:
        movement += "E"
        x += 1
    elif x > 0:
        movement += "W"
        x -= 1
        
    print movement
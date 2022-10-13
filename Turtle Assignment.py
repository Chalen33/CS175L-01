#Chalen Bobish
#CS-175L
#Turtle Graphics Stop Sign

import math
import turtle

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

# Size the window.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

# Calculate the diameter of the octagon so we
# can center it in the graphics window.
#                s
#        ---------------
#       / |             \
#  s   /  |              \
#     /   | x             \  s
#    /    |                \
#   |------                 |
#   |   x                   |
#   |                       |
#   To get the diameter:
#     diameter = s + 2 * x
#   We know that s is 100.
#   Use Pythagoras to get x:
#   s^2 = x^2 + x^2
#   s^2 = 2*x^2
#   x = s / sqrt(2)
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

#Initialize the turtle.
line = turtle.Turtle()
line.color('Red')

#Move the turtle to the starting point.
line.penup()
line.setposition(-55,-80)
line.pendown()

line.fillcolor('red')
line.begin_fill()

#Draw the octagon.
line.color('red')
for x in range(8):
    line.forward(100)
    line.left(45)
    
line.end_fill()

#Display Stop
word_font = ('Arial', 85, 'bold')
line.pencolor('white')
turtle.write('STOP', font = word_font, align ='center')
turtle.done()












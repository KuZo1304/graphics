from graphics import *
import time
import math
import random

width = 1000
height = 800

# Random sample for comparision
win2 = GraphWin("Random", width, height)
center2 = Point(width//2, height//2)
center2.setOutline("red")
center2.draw(win2)
curr2 = center2

for i in range(3,400,2):
    val = i**2
    curr2.x = curr2.x + 2
    curr2.y = curr2.y - 2
    tr = Point(curr2.x, curr2.y)
    if(random.randint(-1,1)):
        tr.draw(win2)
    for j in range(i-1):
        val = val-1
        tr.x = tr.x-2
        if(random.randint(-1,1)):
            Point(tr.x, tr.y).draw(win2)
    for j in range(i-1):
        val = val-1
        tr.y = tr.y+2
        if(random.randint(-1,1)):
            Point(tr.x, tr.y).draw(win2)
    for j in range(i-1):
        val = val-1
        tr.x = tr.x+2
        if(random.randint(-1,1)):
            Point(tr.x, tr.y).draw(win2)
    for j in range(i-2):
        val = val-1
        tr.y = tr.y-2
        if(random.randint(-1,1)):
            Point(tr.x, tr.y).draw(win2)

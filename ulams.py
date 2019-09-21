from graphics import *
import time
import math

width = 1000
height = 800
win = GraphWin("Ulam's Square", width, height)

center = Point(width//2, height//2)
center.setOutline("red")
center.draw(win)

def isPrime(n):
    """Determines Primarility"""
    if n == 2:
        return True
    elif n == 3:
        return True
    for i in range(5, math.ceil(math.sqrt(n)), 6):
        if n%i == 0 or n%(i+2) == 0:
            return False
    return True

curr = center
for i in range(3,400,2):
    val = i**2
    curr.x = curr.x + 2
    curr.y = curr.y - 2
    tr = Point(curr.x, curr.y)
    for j in range(i-1):
        val = val-1
        tr.x = tr.x-2
        if(isPrime(val)):
            Point(tr.x, tr.y).draw(win)
    for j in range(i-1):
        val = val-1
        tr.y = tr.y+2
        if(isPrime(val)):
            Point(tr.x, tr.y).draw(win)
    for j in range(i-1):
        val = val-1
        tr.x = tr.x+2
        if(isPrime(val)):
            Point(tr.x, tr.y).draw(win)
    for j in range(i-2):
        val = val-1
        tr.y = tr.y-2
        if(isPrime(val)):
            Point(tr.x, tr.y).draw(win)




from graphics import *
import random
import time

win = GraphWin("Seirpinski Triangle", 500, 500)
#+ random.randint(-20,20) + random.randint(-10,10)
#+ random.randint(-20,20) + random.randint(-10,10)
#+ random.randint(-20,20) + random.randint(-10,10)
A = Point(250 , 20 )
B = Point(480 , 400 )
C = Point(20 , 400 )

A.draw(win)
B.draw(win)
C.draw(win)

sel = Point(random.randint(20,480), random.randint(20, 400))
sel.setOutline('red')
sel.draw(win)

nx = sel.x
ny = sel.y

for i in range(10000):
    choice = random.randint(0,3)
    if choice == 1:
        nx = (nx + A.x)/2
        ny = (ny + A.y)/2
        np = Point(nx, ny)
        np.draw(win)
        time.sleep(0.0001)
    
    elif choice == 2:
        nx = (nx + B.x)/2
        ny = (ny + B.y)/2
        np = Point(nx, ny)
        np.draw(win)
        time.sleep(0.0001)
      
    elif choice == 3:
        nx = (nx + C.x)/2
        ny = (ny + C.y)/2
        np = Point(nx, ny)
        np.draw(win)
        time.sleep(0.0001)
        

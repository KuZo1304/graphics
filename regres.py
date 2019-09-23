from graphics import *
import random
import time

win = GraphWin("Linear Regressor ", 500, 500)

x = []
y = []
for i in range(100):
    x.append(random.randint(500 - 5*i + 60, 5*i - 60))
    y.append(random.randint(5*i + 60, 5*i - 60))

for i in range(100):
    Point(x[i], y[i]).draw(win)
    #print()

x_sum = 0
y_sum = 0
for i in range(100):
    x_sum += x[i]
    y_sum += y[i]

x_mean = x_sum/100
y_mean = y_sum/100

diff = 0
for i in range(100):
    diff += (x[i] - x_mean)*(x[i] - x_mean)

x_dif_sq = 0
for i in range(100):
    x_dif_sq += (x[i] - x_mean)**2



beta_1 = diff / x_dif_sq
beta_0 = y_mean - beta_1*x_mean
print("diff : ",diff)
print("beta_0: ",beta_0)

start = Point(0, beta_0)
end   = Point(500, beta_0 + beta_1*500)
line = Line(start, end)
line.draw(win)

time.sleep(10) 
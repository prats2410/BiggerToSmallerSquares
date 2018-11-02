from turtle import *

speed(0)
colors=['pink','red','green','yellow','purple']
for i in range(200,0,-1):
    pencolor(colors[i%5])
    forward(i)
    left(90)

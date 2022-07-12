import turtle
from time import sleep

wn = turtle.Screen().bgcolor('black')
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Turtle()
t.speed(18)
for x in range(250):
    t.pencolor(colors[x%6])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)
sleep(2)
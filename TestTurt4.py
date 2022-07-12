import turtle
from time import sleep

screen = turtle.Screen()
screen.setup(500, 600, startx=0, starty=100)
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(280):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)
sleep(2)
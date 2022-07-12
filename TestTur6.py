import random
import turtle
from time import sleep

wn = turtle.Screen().bgcolor('black')
x = 1
color = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Turtle()
t.speed(0)
while x < 200:
    choice = random.choice(color)
    t.pencolor(choice)
    t.forward(50 + x)
    t.right(90.991)
    x = x + 1
t.hideturtle()
sleep(2)
import turtle
import colorsys
from time import sleep

screen = turtle.Screen()
screen.setup(500, 600, startx=0, starty=100)
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(10)
n = 36
h = 0
for i in range(36):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    t.color(c)
    t.left(10)
    for j in range(5):
        t.forward(200)
        t.left(144)
sleep(5)
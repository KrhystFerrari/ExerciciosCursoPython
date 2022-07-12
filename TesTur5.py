import turtle as t
t.speed(0)
t.bgcolor('orange')
t.pencolor('cyan')

for i in range(168):
    t.right(i)
    t.circle(125, i)
    t.forward(i)
    t.right(90)

t.done()
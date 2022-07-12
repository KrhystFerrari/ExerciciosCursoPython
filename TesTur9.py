import turtle as t

t.speed(0)
t.bgcolor('black')
t.pencolor('green')

for i in range(160):
    t.right(i)
    t.circle(400, i)
    t.forward(i)
    t.right(200)

t.done()
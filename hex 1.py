from turtle import *
speed('fastest')
pencolor('yellow')
pensize(3)
for i in range (200):
    fd(100 -i)
    rt(60)
    circle(120 ,270)
    dot(10,'red')
mainloop()

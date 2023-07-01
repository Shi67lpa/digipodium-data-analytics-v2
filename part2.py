from turtle import *
speed('fastest')
bgcolor('black')
colors =['red','orange','yellow',
         'green','blue','purple']
i = 0
while True:
    pencolor(colors[i%6])
    fd(20+i)
    lt(62)
    i +=1
mainloop()
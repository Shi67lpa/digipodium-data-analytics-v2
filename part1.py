from turtle import*

for i in  range (6):
    pensize(5)
    speed('fastest')
    colors = ['red','purple']
    pencolor('yellow')
    fd(50)
    for i in range (6):
        pencolor('blue')
        fd(100)
        fillcolor(colors[i%2])
        begin_fill()
        for i in range (6):
            pencolor('green')
            fd(25)
            lt(360/6)
        end_fill()
        lt(360/6) 
    lt(360/6) 
mainloop()
















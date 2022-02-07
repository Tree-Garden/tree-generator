import turtle
from random import randint
from PIL import Image
from PIL import EpsImagePlugin
import os
EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs9.55.0\bin\gswin64c'


i = 1
while i <= 1000:
    turtle.hideturtle()
    turtle.tracer(0)
    turtle.penup()
    turtle.setposition(0,-300)
    turtle.left(90)
    turtle.pendown()
    thick = 16
    turtle.pensize(thick)

    axiom = "22220"
    axmTemp = ""
    itr = 12
    angl = 16
    dl = 10
    stc = []

    translate={"1":"21",
            "0":"1[-20]+20"}

    for k in range(itr):
        for ch in axiom:
            if ch in translate:
                axmTemp+=translate[ch]
            else:
                axmTemp+=ch
        axiom = axmTemp
        axmTemp = ""

    for ch in axiom:
        if   ch == "+":
            turtle.right(angl - randint(-5,5))
        elif ch == "-":
            turtle.left(angl - randint(-5,5))
        elif ch == "2":
            if randint(0,10)>4:
                turtle.forward(dl)        
        elif ch == "1":
            if randint(0,10)>4:
                turtle.forward(dl) 
        elif ch == "0":
            stc.append(turtle.pensize())
            turtle.pensize(4)
            r = randint(0,10)
            if r < 3:
                turtle.pencolor('#009900')
            elif r > 6:
                turtle.pencolor('#667900')
            else:
                turtle.pencolor('#20BB00')
            turtle.forward(dl-2)
            turtle.pensize(stc.pop())   
            turtle.pencolor('#000000')        
        elif ch == "[":
            thick = thick*0.75
            turtle.pensize(thick)
            stc.append(thick)
            stc.append(turtle.xcor())
            stc.append(turtle.ycor())
            stc.append(turtle.heading())
        elif ch == "]":
            turtle.penup()
            turtle.setheading(stc.pop())
            turtle.sety(stc.pop())
            turtle.setx(stc.pop())
            thick = stc.pop()
            turtle.pensize(thick)
            turtle.pendown()

    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="tree.eps")        
    im = Image.open('tree.eps')
    fig = im.convert('RGBA', )
    fig = fig.resize((1000, 1000))
    fig.save(f'{i:04}.png', lossless = True)
    im = Image.open(f'{i:04}.png')
    os.remove('tree.eps')
    print('Done')
    turtle.clear()
    turtle.reset()
    i += 1

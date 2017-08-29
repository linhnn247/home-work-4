from turtle import *
from random import randint
#Screen().bgcolor('lightgreen')
pensize(1)
color('darkblue')
speed(-1)
#1
def drawsquare1(sz,g):
    for i in range(4):
        forward(sz)
        left(90)
    penup()
    forward(sz+g)
    pendown()
penup()
goto(0, 100)
pendown()
for i in range(5):
    drawsquare1(20,5)
#2
penup()
goto(0,0)
pendown()
def drawsquare2(sz,g):
    for i in range(4):
        forward(sz)
        left(90)

for i in range(1,6):
    drawsquare2(20*i,10)
    penup()
    goto(-10*i,-10*i)
    pendown()
#3
penup()
goto(0,-200)
pendown()
def drawpolygon(n,sz):
    for i in range(n):
        forward(sz)
        left(360/n)
drawpolygon(8,40)
penup()
forward(100)
pendown()
drawpolygon(3,100)
#4
penup()
goto(-170,100)
pendown()
def drawsquared(sz,angle):
    for i in range(4):
        for j in range(4):
            forward(sz)
            left(90)
        left(90)
    left(angle)

for i in range(6):
    drawsquared(50,15)
#5
penup()
goto(-200,-100)
pendown()
right(90)
def drawsquared3(sz,inc,angle):
    forward(sz)
    left(angle)
sz = 10
inc = 2
for i in range(50):
    drawsquared3(sz,inc,90)
    sz += inc
penup()
goto(200,0)
pendown()
right(90)
sz = 10
inc = 2
for i in range(50):
    drawsquared3(sz,inc,89)
    sz += inc
#6
#penup()
#goto(20,170)
#pendown()
#right(39+180-36)
#def drawstar(sz):
    #for i in range(5):
        #forward(sz)
        #left(180-36)
#drawstar(100)
#7
penup()
goto(20,170)
pendown()
right(39+180-36)
colormode(255)


def drawstar(sz):
    for i in range(5):
        clr1 = randint(1, 255)
        clr2 = randint(1, 255)
        clr3 = randint(1, 255)
        fillcolor(clr1,clr2,clr3)
        begin_fill()
        right(72)
        forward(sz)
        left(144)
        forward(sz)
        end_fill()
drawstar(50)

clr4 = randint(1, 255)
clr5 = randint(1, 255)
clr6 = randint(1, 255)
fillcolor(clr4,clr5,clr6)
begin_fill()
drawpolygon(5,50*((5 ** 0.5 - 1)/2))
end_fill()
hideturtle()
mainloop()


from turtle import *
speed(10)
def background(color_land, color_sky):
    color(color_land)
    begin_fill()
    penup()
    goto(-200,-200)
    pendown()
    forward(400)
    left(90)
    forward(130)
    left(90)
    forward(400)
    left(90)
    forward(130)
    end_fill()
    color(color_sky)
    begin_fill()
    penup()
    goto(-200, 200)
    pendown()
    left(90)
    forward(400)
    right(90)
    forward(270)
    right(90)
    forward(400)
    right(90)
    forward(270)
    end_fill()

def sun():
    color('yellow')
    begin_fill()
    penup()
    goto(175, 80)
    pendown()
    for i in range(18):
        forward(100)
        left(100)
    end_fill()


def moon():
    color('bisque')
    begin_fill()
    penup()
    goto(180, 120)
    pendown()
    circle(55)
    end_fill()


def house_light(color_light):
    color(color_light)
    begin_fill()
    penup()
    goto(-150, -150)
    pendown()
    forward(250)
    right(90)
    forward(150)
    right(90)
    forward(250)
    right(90)
    forward(150)
    end_fill()


def house_dark(color_dark):
    color(color_dark)
    begin_fill()
    penup()
    goto(-150, -150)
    pendown()
    forward(250)
    right(90)
    forward(150)
    right(90)
    forward(250)
    right(90)
    forward(150)
    end_fill()

def window_light(x,y):
    color('lemonchiffon')
    setheading(0)
    begin_fill()
    penup()
    goto(x, y)
    pendown()
    for i in range(4):
        forward(50)
        left(90)
    end_fill()

def window_dark(x,y):
    color('khaki')
    setheading(0)
    begin_fill()
    penup()
    goto(x, y)
    pendown()
    for i in range(4):
        forward(50)
        left(90)
    end_fill()
    
hideturtle()

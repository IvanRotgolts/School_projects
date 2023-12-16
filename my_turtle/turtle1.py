import turtle
import random

DATA_CIRCLE=((50,100),(150,100),(250,100),(100,20),(200,20))
turtle_canvas=turtle.Turtle()
turtle_canvas.speed(6)

def goto(x,y):
    turtle_canvas.up()
    turtle_canvas.goto(x,y)
    turtle_canvas.down()

def draw_square(x,y):
    goto(x,y)
    for i in range(4):
        turtle_canvas.forward(100)
        turtle_canvas.left(90)
def draw_pentagon(x,y):
    goto(x,y)
    for i in range(5):
        turtle_canvas.forward(100)
        turtle_canvas.left(72)


def draw_polygon(sides):
    for i in range(sides):
        turtle_canvas.forward(100)
        turtle_canvas.left(360/sides)
#draw_polygon(3)

def draw_polygon(sides,turn):
    for a in range(turn):
        for i in range(sides):
            turtle_canvas.forward(100)
            turtle_canvas.left(360/sides)
        turtle_canvas.right(90)

def draw_circle(x,y):
    goto(x,y)
    for i in range(60):
        turtle_canvas.forward(10)
        turtle_canvas.left(6)
#draw_circle(100,100)

def get_random_color():
    colours=["red","blue","green","yellow"]
    random_colour=random.choice(colours)
    return random_colour

def draw_star(color=get_random_color(),width=16):
    turtle_canvas.color(color)
    turtle_canvas.width(width)
    for i in range(5):
        turtle_canvas.forward(100)
        turtle_canvas.left(144)

def choose_olympic_circle(index, data_circle):
    if index==0:
        draw_olympic_circle(data_circle[0],"blue")
    elif index==1:
        draw_olympic_circle(data_circle[1],"black")
    elif index==2:
        draw_olympic_circle(data_circle[2],"red")
    elif index==3:
        draw_olympic_circle(data_circle[3],"yellow")
    elif index==4:
        draw_olympic_circle(data_circle[4],"green")

def draw_olympic_circle(coords,colour):
    x,y=coords[0],coords[1]
    turtle_canvas.width(10)
    goto(x=x,y=y)
    for i in range(20):
            turtle_canvas.color(colour)
            turtle_canvas.forward(20)
            turtle_canvas.left(18)
            
def draw_olympic_circles(data_circle):
    coordinateX=50
    for i in range(5):
        goto(coordinateX,100)
        coordinateX+=100
        choose_olympic_circle(i, data_circle)

draw_olympic_circles(DATA_CIRCLE)
#draw_star()
#draw_polygon(12,4)
#draw_square(100,100)
turtle_canvas.screen.mainloop()
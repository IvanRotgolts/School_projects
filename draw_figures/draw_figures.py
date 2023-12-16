import tkinter
import random
import time

window=tkinter.Tk()
window.title("draw_figures")
window.geometry("700x500")

canvas=tkinter.Canvas(window,width=500,height=500,bg="#ffffff")
canvas.place(x=0,y=0)

colours=["#52a20c","#071154","#ccaebb"]




def draw_circle():
    x=random.randint(0,500)
    y=random.randint(0,500)
    random_num=random.randint(20,100)
    canvas.create_oval(x,y,x+random_num,y+random_num,fill=random.choice(colours))

def draw_oval():
    x=random.randint(0,500)
    y=random.randint(0,500)
    random_num=random.randint(20,100)
    random_num_2=random.randint(20,100)
    canvas.create_oval(x,y,x+random_num,y+random_num_2,fill=random.choice(colours))

def draw_square():
    x=random.randint(0,500)
    y=random.randint(0,500)
    random_num=random.randint(20,100)
    canvas.create_rectangle(x,y,x+random_num,y+random_num,fill=random.choice(colours))

def draw_circles():
    for i in range(random.randint(0,10)):
        draw_circle()
        window.update()
        time.sleep(1)

dx=0
dy=0
on=True
def animate_circle():
    global dx,dy,on
    on=True
    x=random.randint(0,500)
    y=random.randint(0,500)
    random_num=random.randint(20,100)
    circle=canvas.create_oval(x,y,x+random_num,y+random_num,fill=random.choice(colours))
    dx=1
    dy=1
    while on==True:
        coords=canvas.coords(circle)
        left,top,right,bottom=coords[0],coords[1],coords[2],coords[3]
        if left<=0 or right>=500:
            dx=-dx
        if top<=0 or bottom>=500:
            dy=-dy
        canvas.move(circle,dx,dy)
        time.sleep(0.01)
        window.update()


def stop_animation():
    global dx, dy, on
    on=False
    #dx=0
    #dy=0





button_circle=tkinter.Button(window,text="Нарисовать круг",command=draw_circle)
button_circle.place(x=550,y=50)

button_oval=tkinter.Button(window,text="Нарисовать овал",command=draw_oval)
button_oval.place(x=550,y=110)

button_square=tkinter.Button(window,text="Нарисовать квадрат",command=draw_square)
button_square.place(x=550,y=170)

button_circles=tkinter.Button(window,text="Нарисовать круги",command=draw_circles)
button_circles.place(x=550,y=230)

button_animate_circle=tkinter.Button(window,text="Анимировать круг",command=animate_circle)
button_animate_circle.place(x=550,y=290)

button_stop=tkinter.Button(window,text="Остановить анимацию",command=stop_animation)
button_stop.place(x=550,y=350)





window.mainloop()
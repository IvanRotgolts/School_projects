import tkinter as tk
import random

colours=("red", "blue", "green", "pink", "black", "yellow", "orange", "purple", "brown", "white")
score=0
false=0

window=tk.Tk()
window.title("guess_word's_colour")
window.geometry("350x250")

instructions=tk.Label(window, text="Введи цвет слова, а не слово! Жми Enter, чтобы играть.", font=("Helvetica",10))
instructions.place(x=10, y=10)

colour_lable=tk.Label(window, text="colour", font=("Helvetica", 60))
colour_lable.place(x=10, y=80)

right_lable=tk.Label(window, text="Правильных ответов: 0", font=("Helvetica", 10))
right_lable.place(x=10, y=40)

false_lable=tk.Label(window, text="Неправильных ответов: 0", font=("Helvetica", 10))
false_lable.place(x=10, y=60)

text=tk.Entry(window,width=48)
text.place(x=3,y=170)






def new_word():
    #random_colour=colours[random.randint(0,9)]
    random_colour=random.choice(colours)
    colour_lable["text"]=random_colour
    random_colour1=random.choice(colours)
    colour_lable["fg"]=random_colour1

def check_colour():
    global score, false
    answer=text.get()
    if answer==colour_lable["text"]:
        score=int(score)
        print("Right!")
        new_word()
        text.delete(0,"end")
        score+=1
        str_score=str(score)
        right_lable["text"]=f"Правильных ответов: {str_score}"
    elif answer!=colour_lable["text"]:
        print("False!")
        false=int(false)
        text.delete(0,"end")
        false+=1
        str_false=str(false)
        false_lable["text"]=f"Неправильных ответов: {str_false}"

def restart():
    global score, false
    new_word()
    score=0
    false=0
    right_lable["text"]="Правильных ответов: 0"
    false_lable["text"]="Неправильных ответов: 0"
    text.delete(0,"end")
button_enter=tk.Button(window,text="Enter",command=check_colour)
button_enter.place(x=300,y=165)
button_restart=tk.Button(window,text="Restart",command=restart)
button_restart.place(x=300,y=200)

new_word()

#window.bind("<Return>", check_colour)
window.mainloop()
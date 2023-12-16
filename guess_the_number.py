import tkinter
import random

attempts=10

window=tkinter.Tk()
window.title("Guess_the_number")
window.geometry("300x300")

lable=tkinter.Label(window, text="Введи число от 1 до 100", font=("Helvetica", 10))
lable.place(x=10, y=10)

attempts_lable=tkinter.Label(window, text=f"Количество попыток: {attempts}", font=("Helvetica", 10))
attempts_lable.place(x=10, y=90)

text=tkinter.Entry(window,width=48)
text.place(x=10,y=130)



rand_num=0
user_num=0

def generate_number():
    global rand_num
    rand_num=random.randint(0,100)

def get_num():
    global user_num
    user_num=text.get()
    user_num=int(user_num)


def restart():
    global rand_num, user_num, attempts
    rand_num=0
    user_num=0
    attempts=10
    generate_number()

def check_win():
    global user_num,rand_num, attempts
    get_num()
    #print(user_num,rand_num)
    if user_num>rand_num:
        lable["text"]="Число больше загаданного!"
        attempts-=1
        attempts_lable["text"]=f"Количество попыток: {attempts}"
    elif user_num<rand_num:
        lable["text"]="Число меньше загаданного!"
        attempts-=1
        attempts_lable["text"]=f"Количество попыток: {attempts}"
    elif user_num==rand_num:
        lable["text"]="Вы угадали!"
        button_restart.configure(state=tkinter.NORMAL)
        attempts_lable["text"]=f"Количество попыток: {attempts}"

    if attempts<0:
        print("Вы проиграли!")
        window.quit()

generate_number()
button_check=tkinter.Button(window,text="Проверить", command=check_win)
button_check.place(x=10,y=190)

button_restart=tkinter.Button(window,text="Начать заново", state=tkinter.DISABLED, command=restart)
button_restart.place(x=10,y=230)

#button_check.configure(state=tk.NORMAL) 

#button_restart.configure(state=tk.DISABLED)

window.mainloop()

import tkinter

window=tkinter.Tk()
window.title("calculator")
window.geometry("300x300")

def get_value(value):
    return int(value.get())

def add():
    result=get_value(text_num1)+get_value(text_num2)
    text_answer.insert(0,result)
def sub():
    result=get_value(text_num1)-get_value(text_num2)
    text_answer.insert(0,result)
def mult():
    result=get_value(text_num1)*get_value(text_num2)
    text_answer.insert(0,result)
def clear():
    text_answer.delete(0,"end")
    text_num1.delete(0,"end")
    text_num2.delete(0,"end")
def div():
    result=get_value(text_num1)/get_value(text_num2)
    text_answer.insert(0,result)

def equal():
    pass

#создание кнопки плюса
button_add=tkinter.Button(window,text="+",command=add)
button_add.place(x=95,y=110)

#создание кнопки минуса
button_sub=tkinter.Button(window,text="-",command=sub)
button_sub.place(x=75,y=110)

#создание кнопки умножения
button_mult=tkinter.Button(window,text="*",command=mult)
button_mult.place(x=75,y=137)

#создание кнопки очистки
button_clear=tkinter.Button(window,text="AC",command=clear)
button_clear.place(x=115,y=110)

#создание кнопки деление
button_div=tkinter.Button(window,text="/",command=div)
button_div.place(x=95,y=137)

#создание первого поля
text_num1=tkinter.Entry(window,width=22)
text_num1.place(x=10,y=20)

#создание второго поля
text_num2=tkinter.Entry(window,width=22)
text_num2.place(x=150,y=20)

#создание поля ответа
text_answer=tkinter.Entry(window,width=10)
text_answer.place(x=115,y=50)






window.mainloop()

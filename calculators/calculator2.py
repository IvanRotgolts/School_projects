import tkinter

window=tkinter.Tk()
window.title("calculator")
window.geometry("300x300")

first_number=0
second_number=0
operation=""

def type_sign(number):
    text_num_value=text_num1.get()
    if text_num_value=="0":
        return
    numbers_len=len(text_num_value)
    text_num1.insert(numbers_len,number)
def sub():
    global first_number
    global operation
    first_number=text_num1.get()
    text_num1.delete(0,"end")
    button="sub"
def button_plus():
    global first_number
    global operation
    first_number=text_num1.get()
    text_num1.delete(0,"end")
    operation="plus"
def button_mult():
    global first_number
    global operation
    first_number=text_num1.get()
    text_num1.delete(0,"end")
    operation="mult"
def button_div():
    global first_number
    global operation
    first_number=text_num1.get()
    text_num1.delete(0,"end")
    operation="div"
def button_clear():
     text_num1.delete(0,"end")
def button_equal():
    global first_number
    global second_number
    second_number=text_num1.get()
    second_number=float(second_number)
    first_number=float(first_number)
    text_num1.delete(0,"end")
    print(first_number)
    print(second_number)
    
        
    if operation=="sub":
        result=first_number-second_number
        text_num1.insert(0,result)
        print(result)
    elif operation=="mult":
        result=first_number*second_number
        text_num1.delete(0,"end")
        text_num1.insert(0,result)
        print(result)
    elif operation=="plus":
        result=first_number+second_number
        text_num1.delete(0,"end")
        text_num1.insert(0,result)
        print(result)
    elif operation=="div":
        if second_number==0:
            text_num1.insert(0,"Деление на ноль невозможно")
        else:
            result=first_number/second_number
            text_num1.delete(0,"end")
            text_num1.insert(0,result)
            print(result)

    
    
   
    
#создание кнопки плюса
button_add=tkinter.Button(window,text="+",command=button_plus)
button_add.place(x=250,y=190)

#создание кнопки равно
button_add=tkinter.Button(window,text="=",command=button_equal)
button_add.place(x=250,y=220)

#создание кнопки минуса
button_sub=tkinter.Button(window,text="-",command=sub)
button_sub.place(x=250,y=110)

#создание кнопки умножения
button_mult=tkinter.Button(window,text="*",command=button_mult)
button_mult.place(x=250,y=137)

#создание кнопки очистки
button_clear=tkinter.Button(window,text="AC",command=button_clear)
button_clear.place(x=250,y=85)

#создание кнопки деление
button_div=tkinter.Button(window,text="/",command=button_div)
button_div.place(x=250,y=162)

#создание первого поля
text_num1=tkinter.Entry(window,width=48)
text_num1.place(x=3,y=20)

#создание кнопки .
button_0=tkinter.Button(window,text=".",command=lambda number=".":type_sign(number))
button_0.place(x=250,y=250)

#создание кнопки 0
button_0=tkinter.Button(window,text="0",command=lambda number=0:type_sign(number))
button_0.place(x=140,y=190)

#создание кнопки 1
button_1=tkinter.Button(window,text="1",command=lambda number=1:type_sign(number))
button_1.place(x=110,y=165)

#создание кнопки 2
button_2=tkinter.Button(window,text="2",command=lambda number=2:type_sign(number))
button_2.place(x=140,y=165)

#создание кнопки 3
button_3=tkinter.Button(window,text="3",command=lambda number=3:type_sign(number))
button_3.place(x=170,y=165)

#создание кнопки 4
button_4=tkinter.Button(window,text="4",command=lambda number=4:type_sign(number))
button_4.place(x=110,y=135)

#создание кнопки 5
button_5=tkinter.Button(window,text="5",command=lambda number=5:type_sign(number))
button_5.place(x=140,y=135)

#создание кнопки 6
button_6=tkinter.Button(window,text="6",command=lambda number=6:type_sign(number))
button_6.place(x=170,y=135)

#создание кнопки 7
button_7=tkinter.Button(window,text="7",command=lambda number=7:type_sign(number))
button_7.place(x=110,y=105)

#создание кнопки 8
button_8=tkinter.Button(window,text="8",command=lambda number=8:type_sign(number))
button_8.place(x=140,y=105)

#создание кнопки 9
button_9=tkinter.Button(window,text="9",command=lambda number=9:type_sign(number))
button_9.place(x=170,y=105)

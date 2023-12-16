import tkinter
import random
import tkinter.messagebox as tkm


window=tkinter.Tk()
window.title("guess_the_word")
window.geometry("300x300")

text_num=tkinter.Entry(window,width=17)
text_num.place(x=100,y=70)

lable=tkinter.Label(window, text="")
lable.place(x=100, y=40)

letters=[]

def word_generator():
    words=["apple","chair","table","lamp","picture","mirror"]
    random_index=random.randint(0,len(words)-1)
    secret_word=words[random_index]
    return secret_word

random_word=word_generator()

def show_word():
    result=""
    for char in random_word:
        if char in letters:
            result+=char
            text_num.delete(0,"end")
        elif char not in letters:
            result+="*"
            text_num.delete(0,"end")
    return result

def check_letter():
    letter=text_num.get()
    letters.append(letter)
    result=show_word()
    lable["text"]=result
    if "*" not in result:
        tkm.showinfo("Выигрыш","Вы выиграли!")


def restart():
    global letters
    global random_word
    text_num.delete(0,"end")
    lable["text"]=""
    random_word=word_generator()
    letters=[]
    result=show_word()
    lable["text"]=result
    
check_letter()
        
button_add=tkinter.Button(window,text="Проверить слово",command=check_letter)
button_add.place(x=100,y=100)
button_restart=tkinter.Button(window,text="Перезапуск",command=restart)
button_restart.place(x=100,y=150)




#window.bind("<Return>", check_letter)
window.mainloop()
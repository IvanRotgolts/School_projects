import tkinter as tk
import tkinter.filedialog as tfd
import tkinter.messagebox as tkm

#
window=tk.Tk()
window.title("notePad")
window.geometry("400x400")

#
content_text=tk.Text(window,wrap="word")
content_text.place(x=0,y=0,relwidth=1,relheight=1)
file_name=""

def open_file():
    global file_name
    try:
        file_name=tfd.askopenfilename()
        with open(file_name,encoding="utf-8") as file:
            content_text.insert(1.0,file.read())
    except FileNotFoundError as err:
        print("Невозможно открыть файл")
        return ["не работает"]
def save_as():
    global file_name
    file_name=tfd.asksaveasfilename()
    if file_name!="":
        with open(file_name,"w",encoding="utf-8") as file:
            file.write(content_text.get(1.0,"end"))
def new_file():
    if content_text.get(1.0,"end")=="":
        content_text.delete()
    else:
        save_as()
def save_file():
    global file_name
    if file_name=="":
        save_as()
    if file_name!="":
        with open(file_name,"w",encoding="utf-8") as file:
            file.write(content_text.get(1.0,"end"))
def help_menu123():
    print("sefsef")
    tkm.showinfo("О программе","Блокнот V1")
        

#создание главного меню
main_menu=tk.Menu(window)

#конфигурирование меню с окном
window.configure(menu=main_menu)

#создание раздела "файл"
file_menu=tk.Menu(main_menu,tearoff=0)
help_menu=tk.Menu(main_menu,tearoff=0)

#добавление раздела файл в главное меню
main_menu.add_cascade(label="file",menu=file_menu)
main_menu.add_cascade(label="help",menu=help_menu)

new_file_icon=tk.PhotoImage(file="new_file.gif")
open_icon=tk.PhotoImage(file="open_file.gif")
save_icon=tk.PhotoImage(file="save_file.gif")

file_menu.add_command(label="New file",image=new_file_icon,compound="left",command=new_file)
file_menu.add_command(label="Open",image=open_icon,compound="left",command=help_menu123)
file_menu.add_command(label="Save As",image=save_icon,compound="left",command=save_as)
file_menu.add_command(label="Save",image=save_icon,compound="left",command=save_file)
help_menu.add_command(label="Help Menu",compound="left",command=help_menu123)



window.mainloop()

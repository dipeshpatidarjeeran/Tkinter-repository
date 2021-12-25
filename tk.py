from tkinter import *

from tkinter import messagebox

window = Tk()
window.title('The  Dark world')
window.geometry("600x600") 

n1=Label(window, text='enter the first number ').grid(row=0, column=0)
n2=Label(window, text='enter the second number').grid(row=1, column=0)

e1=Entry(window).grid(row=0, column=5)
e2=Entry(window).grid(row=1, column=5)


def exit():
    window.destroy()

def sum():
    #result=float(e1.get())+float(e2.get())

    #tkinter.Label(window, command=result).grid(row=5)
    result = float(e1.get()) + float(e2.get())
    print(result)


button1 =Button(window, text='Exit', width=6, padx=6, pady=6,

                        bg='black', fg='white', command=exit).grid(row=2, column=0)


button2 =Button(window, text='SUM', width=7, padx=7, pady=7,

                        bg='black', fg='white', command=sum).grid(row=2, column=1)

#e1 =(window, width=20).grid(row=0)
window.mainloop()

import tkinter
from tkinter import messagebox
#1 create the window

# i am creating a object of Tk class
mywindow = tkinter.Tk()

mywindow.geometry("600x600")  # window sight
mywindow.title = "DK -main window"  #create title window
label = tkinter.Label(mywindow,text = "welcome to the tkinter tutorial").pack()


def myfunction():
    global mywindow
    msg = messagebox.askquestion("exit application","are you same you want to exit the appication")
    print(msg)
    if msg == 'yes':
        mywindow.destroy()
    else:
        messagebox.showinto('return','you will now return to the application screen')


btn = tkinter.Button(mywindow, text = "close the application ", command=myfunction).pack()


#2 run the main loop
mywindow.mainloop()
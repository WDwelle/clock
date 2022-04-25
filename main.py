from tkinter import *
from tkinter.ttk import *
#import system time
from time import strftime


#create window with tkinter
root = Tk()
root.title('clock')


#display time
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)


#Styling
lbl = Label(root, font = ('calibri', 40, 'bold'), 
            background = 'black',
            foreground = 'orange')


#Place clock in window
lbl.pack(anchor = 'center')
time()


mainloop()
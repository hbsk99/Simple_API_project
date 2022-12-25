import Sample_Api_Backend as bck
from tkinter import *
from tkinter import ttk
root= Tk()

root.geometry('300x300')
root.title('TEST')
l = Label(root,text='Hello There!!')
l.pack()

b=Button(root,text= 'Click here to read a joke',command = lambda: bck.funct1())
b.pack()

root.mainloop()
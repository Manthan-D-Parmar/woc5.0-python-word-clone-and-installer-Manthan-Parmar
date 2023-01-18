#1
from tkinter import *
root=Tk()
root.title("Font Bold Italics and Underline")
root.geometry("650x250")
boldlabel=Label(root,text="Hello World",font=("Helvetica",18,"bold"))
italicslabel=Label(root,text="Hello World",font=("Helvetica",18,"italic"))
underlinedlabel=Label(root,text="Hello World",font=("Helvetica",18,"underline"))
boldlabel.pack()
italicslabel.pack()
underlinedlabel.pack()
root.mainloop()
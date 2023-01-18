#2
from tkinter import *
root=Tk()
root.title("Font size and type change")
root.geometry("650x250")
fontlabel=Label(root,text="Hello World")
fontmodlabel=Label(root,text="Hello World",font=("Comic Sans MS",36))
fontlabel.pack()
fontmodlabel.pack()
root.mainloop()
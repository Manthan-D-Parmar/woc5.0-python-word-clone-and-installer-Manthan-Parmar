#3
from tkinter import *
root=Tk()
root.title("Clear Input")
root.geometry("650x250")
def clear():
    inputtext.delete(0,END)
inputtext=Entry(root,width=40)
inputtext.pack()
Button(root,text="Clear text",command=clear,font=('Helvetica',10)).pack(pady=5)
root.mainloop()
#4
from tkinter import *
root=Tk()
root.title("Retrieve value entered in input")
root.geometry("650x250")
def printInput():
    inp=inputtext.get(1.0,END)
    label.config(text="Input entered : "+inp)
inputtext=Text(root,height=5,width=20)
inputtext.pack()
Button(root,text="Print",command=printInput,font=("Helvetica",10)).pack(pady=5)
label=Label(root,text='')
label.pack()
root.mainloop()
#Importing necessary commands from Tkinter module
from tkinter import *
from tkinter import filedialog
from tkinter import font

#Tkinter Window declaration
root=Tk()
root.title("Manthan Parmar Mid Evaluation ")
root.geometry('1200x660')

#Font
my_font=font.Font(family='Helvetica',size='16')
#Global variable declaration
global open_status
open_status=False

#New File function
def new_text():
    in_text.delete("0.0",END)
    root.title("New File -Manthan Parmar Mid Evaluation")
    status_bar.config(text='New File     ')
    global open_status
    open_status=False

#Open File function 
def open_text():
    in_text.delete("0.0",END)
    text_file=filedialog.askopenfilename(initialdir="C:/",title="Open Text File",filetypes=(("Text Files","*.txt"),))
    if text_file:
        global open_status
        open_status=text_file
    name=text_file
    status_bar.config(text=f'{name}     ')
    root.title(f'{name} -Manthan Parmar Mid Evaluation')
    text_file=open(text_file,'r')
    text=text_file.read()
    in_text.insert(END,text)
    text_file.close()

#Save File function 
def save_text():
    global open_status
    if open_status:
        text_file=open(open_status,'w')
        text_file.write(in_text.get(1.0,END))
        text_file.close()
        status_bar.config(text=f'Saved Successfully {open_status}     ')
    else:
        save_as_text()

#Save File as function
def save_as_text():
    text_file=filedialog.asksaveasfilename(initialdir="C:/",title="Save Text File As",filetype=(("Text Files","*.txt"),))
    if text_file:
        name=text_file
        status_bar.config(text=f'Saved Successfully {name}     ')
        root.title(f'{name} -Manthan Parmar Mid Evaluation')
    text_file=open(text_file,'w')
    text_file.write(in_text.get(1.0,END))
    text_file.close()

#Bold Text
def font_bold():
    bold_font=font.Font(in_text,in_text.cget("font"))
    bold_font.configure(weight="bold")
    in_text.tag_configure("bold",font=bold_font)
    current=in_text.tag_names("sel.first")
    if "bold" in current:
        in_text.tag_remove("bold","sel.first","sel.last")
    else:
        in_text.tag_add("bold","sel.first","sel.last")

#Italics Text
def font_italics():
    italics_font=font.Font(in_text,in_text.cget("font"))
    italics_font.configure(slant="italic")
    in_text.tag_configure("italic",font=italics_font)
    current=in_text.tag_names("sel.first")
    if "italic" in current:
        in_text.tag_remove("italic","sel.first","sel.last")
    else:
        in_text.tag_add("italic","sel.first","sel.last")


#Underline Text
def font_underline():
    underline_font=font.Font(in_text,in_text.cget("font"))
    underline_font.configure(underline=True)
    in_text.tag_configure("underline",font=underline_font)
    current=in_text.tag_names("sel.first")
    if "underline" in current:
        in_text.tag_remove("underline","sel.first","sel.last")
    else:
        in_text.tag_add("underline","sel.first","sel.last")

#Font style
def font_style(style):
    my_font.config(family=style_listbox.get(style_listbox.curselection()))

#Font size
def font_size(size):
    my_font.config(size=size_listbox.get(size_listbox.curselection()))

#Toolbar frame
toolbar_frame=Frame(root)
toolbar_frame.pack(fill=X)

#Main frame
frame=Frame(root)
frame.pack(pady=5)

#Font frame
font_frame=Frame(root)
font_frame.pack()

#Scrollbar for Text box
text_scroll=Scrollbar(frame)
text_scroll.pack(side=RIGHT,fill=Y)

#Text box
in_text=Text(frame,width=100,height=20,font=my_font,selectbackground="blue",selectforeground="white",undo=True,yscrollcommand=text_scroll.set)
in_text.resizable(0,0)
in_text.pack()

#Configuring scroll bar
text_scroll.config(command=in_text.yview)

#Menu
menu=Menu(root)
root.config(menu=menu)

#File menu
file_menu=Menu(menu,tearoff=False)
menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_text)
file_menu.add_command(label="Open",command=open_text)
file_menu.add_command(label="Save",command=save_text)
file_menu.add_command(label="Save As",command=save_as_text)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

#Status Bar
status_bar=Label(root,text='Ready     ',anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=5)

#Bold Button
bold_button=Button(toolbar_frame,text="Bold",command=font_bold)
bold_button.grid(row=0,column=0,sticky=W)

#Italics Button
italics_button=Button(toolbar_frame,text="Italics",command=font_italics)
italics_button.grid(row=0,column=1,sticky=W)

#Underline Button
underline_button=Button(toolbar_frame,text="Underline",command=font_underline)
underline_button.grid(row=0,column=2,sticky=W)

#Font labels
style_label=Label(font_frame,text="Choose Font Style",font=("Helvetica",14))
style_label.grid(row=0,column=0,padx=10)

size_label=Label(font_frame,text="Choose Font Size",font=("Helvetica",14))
size_label.grid(row=0,column=1)

#Style listbox
style_listbox=Listbox(font_frame,selectmode=SINGLE,width=25)
style_listbox.grid(row=1,column=0)
fstyle=['Bodoni MT', 'Century Gothic', 'Garamond', 'Helvetica', 'Impact', 'Lucida Console', 'Papyrus', 'Rockwell', 'Sans Seriff', 'Tahoma', 'Times New Roman', 'Verdana']
for i in fstyle:
    style_listbox.insert('end',i)

#Size listbox
size_listbox=Listbox(font_frame,selectmode=SINGLE,width=25)
size_listbox.grid(row=1,column=1)
fsize=[5,6,7,8,10,12,14,16,18,20,36,48]
for i in fsize:
    size_listbox.insert('end',i)

#Bind listbox
style_listbox.bind("<ButtonRelease-1>",font_style)
size_listbox.bind("<ButtonRelease-1>",font_size)

root.mainloop()
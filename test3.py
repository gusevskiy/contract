from tkinter import *

root = Tk()
root.title("Title")
root.geometry('300x100')


def clear_text(self):
    txtE.delete(0, 'end')


def new_label(event=None):
    Entree = txtE.get()
    lbl1['text'] = 'Hello There ' + Entree.title()
    clear_text(txtE)


lbl1 = Label(root, text='Enter Your Name:')
lbl1.pack()
txtE = Entry(root)
txtE.focus()
txtE.pack()

Button(root, text='Enter', command=new_label).pack()
Button(root, text='Quit', command=root.destroy).pack(side=BOTTOM)
root.bind('<Return>', new_label)
root.mainloop()
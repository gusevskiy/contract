from tkinter import *
from tkinter import messagebox as mb

from docxtpl import DocxTemplate
from docx.shared import Pt
from docx.shared import Inches

window = Tk()

window.title('name')
window.geometry('400x400+100+100')


name = Label(window, text ='Название Юр. лица')
number = Label(window, text ='№ договора')
name.grid(column = 1, row = 0)
name = Entry(window, width = 40)
name.grid(column = 2, row = 0, columnspan=2, sticky = W)


doc = DocxTemplate("C:\code\Moduli\contract\lame.docx")
context = {'name': name}
doc.render(context)
doc.save("lame-final.docx")

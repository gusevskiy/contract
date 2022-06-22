from docxtpl import DocxTemplate
from tkinter import *

window = Tk() #Tk является базовым классом любого Tkinter приложения.
window.title('contract') # title заголовок окна
window.geometry('400x400+100+100')#geometry - устанавливает геометрию окна в формате ширина*высота+x+y

name = Label(window, text ='Название Юр. лица')# Label отображение надписи в нужном месте
number = Label(window, text ='№ договора')

name.grid(column = 1, row = 0) # grid упаковщик представляет собой таблицу с ячейками
na = Entry(window, width = 40) # Entry ввести одну строку текста
na.grid(column = 2, row = 0, columnspan=2, sticky = W)

number.grid(column = 1, row = 1)
nu = Entry(window, width = 5)
nu.grid(column = 2, row = 1, columnspan = 2, sticky = W)

def ent(self):
    print(na.get(), nu.get())
    doc = DocxTemplate("C:\code\Moduli\contract\lame.docx")
    context = {'name': na.get(), 'number': nu.get()}
    doc.render(context)
    doc.save("lame-final.docx")
    # f = open('contract.txt', 'a')
    # f.write(name1.get())
    # f.close()

button = Button(window, text='создать документ', command=lambda: [ent(self=na)])
button.grid(column = 3, row = 20)



#name1.bind("<Return>", ent)


window.mainloop()




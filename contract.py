from docxtpl import DocxTemplate
from tkinter import *
# import tkinter.ttk as ttk

window = Tk() #Tk является базовым классом любого Tkinter приложения.
window.title('contract') # title заголовок окна
#tab = ttk.Notebook(window)

#tab.add(name, text = 'tabb')
window.geometry('500x460+100+100')#geometry - устанавливает геометрию окна в формате ширина*высота+x+y
window.resizable(False, False) #блокирует изменение размеров окна
#window.iconbitmap('1.ico')

name = Label(window, text ='Название Юр. лица')# Label отображение надписи в нужном месте
number = Label(window, text ='№ договора')
date = Label(window, text ='дата')
fio = Label(window, text ='ФИО')
post = Label(window, text ='должность')
adress = Label(window, text ='Юр. адрес')
post_adress = Label(window, text ='Почтовый адрес')
inn = Label(window, text ='ИНН/КПП')
kpp = Label(window, text ='ИНН/КПП')
okpo = Label(window, text = 'ОКПО')
ogrn = Label(window, text = 'ОГРН')
okato = Label(window, text = 'ОКАТО')
okved = Label(window, text = 'ОКВЭД')
bank = Label(window, text = 'БАНК')
big = Label(window, text = 'БИК')
r_s = Label(window, text = 'р/с')
k_s = Label(window, text = 'к/с')
telefon = Label(window, text = 'Телефон')
email = Label(window, text = 'email')

# заголовки окон и ввода данных

name.grid(column = 1, row = 0) # grid упаковщик представляет собой таблицу с ячейками
na = Entry(window, width = 40) # Entry ввести одну строку текста
na.grid(column = 2, row = 0, columnspan=2, sticky = W)


number.grid(column = 1, row = 1)
nu = Entry(window, width = 5)
nu.grid(column = 2, row = 1, columnspan = 2, sticky = W)


date.grid(column = 1, row=2)
da = Entry(window, width=10)
da.grid(column = 2, row = 2, sticky = W)


fio.grid(column = 1, row = 3)
fi = Entry(window, width = 20)
fi.grid(column = 2, row = 3,columnspan = 2, sticky = W)


post.grid(column = 1, row = 4)
po = Entry(window, width = 20)
po.grid(column = 2, row = 4,columnspan = 2, sticky = W)


adress.grid(column = 1, row = 5)
ad = Entry(window, width = 20)
ad.grid(column = 2, row = 5,columnspan = 2, sticky = W)


post_adress.grid(column = 1, row = 6)
pa = Entry(window, width = 20)
pa.grid(column = 2, row = 6,columnspan = 2, sticky = W)


inn.grid(column = 1, row = 7)
inn = Entry(window, width = 20)
inn.grid(column = 2, row = 7, sticky = W)


kpp.grid(column = 1, row = 7)
kpp = Entry(window, width = 20)
kpp.grid(column = 3, row = 7, sticky = W)


okpo.grid(column = 1, row = 8)
okpo = Entry(window, width = 7)
okpo.grid(column = 2, row = 8, sticky = W)


ogrn.grid(column = 1, row = 9)
ogrn = Entry(window, width = 15)
ogrn.grid(column = 2, row = 9, sticky = W)


okato.grid(column = 1, row = 10)
okato = Entry(window, width = 7)
okato.grid(column = 2, row = 10, sticky = W)


okved.grid(column = 1, row = 11)
okved = Entry(window, width = 7)
okved.grid(column = 2, row = 11, sticky = W)



bank.grid(column = 1, row = 12)
bank = Entry(window, width = 40)
bank.grid(column = 2, row = 12, columnspan = 2, sticky = W)


big.grid(column = 1, row = 13)
big = Entry(window, width = 9)
big.grid(column = 2, row = 13, sticky = W)


r_s.grid(column = 1, row = 14)
r_s = Entry(window, width = 30)
r_s.grid(column = 2, row = 14,columnspan = 2, sticky = W)


k_s.grid(column = 1, row = 15)
k_s = Entry(window, width = 30)
k_s.grid(column = 2, row = 15,columnspan = 2, sticky = W)


telefon.grid(column = 1, row = 16)
telefon = Entry(window, width = 12)
telefon.grid(column = 2, row = 16, sticky = W)


email.grid(column = 1, row = 17)
email = Entry(window, width = 20)
email.grid(column = 2, row = 17, sticky = W)

def ent(self):
    doc = DocxTemplate("contract.docx")
    context = {'name': na.get(),
               'number': nu.get(),
               'date': da.get(),
               'fio': fi.get(),
               'post': po.get(),
               'adress': ad.get(),
               'post_adress': pa.get(),
               'inn': inn.get(),
               'kpp': kpp.get(),
               'okpo': okpo.get(),
               'ogrn': ogrn.get(),
               'okato': okato.get(),
               'okved': okved.get(),
               'bank': bank.get(),
               'big': big.get(),
               'r_s': r_s.get(),
               'k_s': k_s.get(),
               'telefon': telefon.get(),
               'email': email.get()
               }
    doc.render(context)
    doc.save(f"add/{na.get()} от {da.get()}.docx")


button = Button(window, text='создать договор', command=lambda: [ent(self=na)])
button.grid(column = 3, row = 20)


window.mainloop()

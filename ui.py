from docxtpl import DocxTemplate
from tkinter import Tk, Label, Entry, W, Button

import name_bank
from inn_kpp_ogrn import Openfile

window = Tk()  # Tk является базовым классом любого Tkinter приложения.
window.title('contract')  # title заголовок окна
window.geometry(
    '600x500+100+100')  # geometry - устанавливает геометрию окна
# в формате ширина*высота+x+y
window.resizable(False, False)  # блокирует изменение размеров окна
# window.iconbitmap('1.ico')
# Label отображение надписи в нужном месте
# grid упаковщик представляет собой таблицу с ячейками
Label(window, text='Название Юр. лица').grid(column=1, row=0)
Label(window, text='№ договора').grid(column=1, row=1)
Label(window, text='дата').grid(column=1, row=2)
Label(window, text='ФИО').grid(column=1, row=3)
Label(window, text='должность').grid(column=1, row=4)
Label(window, text='Юр. адрес').grid(column=1, row=5)
Label(window, text='Почтовый адрес').grid(column=1, row=6)
Label(window, text='ИНН/КПП').grid(column=1, row=7)
Label(window, text='ИНН/КПП').grid(column=1, row=7)
Label(window, text='ОКПО').grid(column=1, row=8)
Label(window, text='ОГРН').grid(column=1, row=9)
Label(window, text='ОКАТО').grid(column=1, row=10)
Label(window, text='ОКВЭД').grid(column=1, row=11)
Label(window, text='БИК').grid(column=1, row=12)
Label(window, text='БАНК').grid(column=1, row=13)
Label(window, text='р/с').grid(column=1, row=14)
Label(window, text='к/с').grid(column=1, row=15)
Label(window, text='Телефон').grid(column=1, row=16)
Label(window, text='email').grid(column=1, row=17)


# заголовки окон и ввода данных
# Entry ввести одну строку текста
# columnspan определяет сколько столбцов займут данные
na = Entry(window, width=40)
na.grid(column=2, row=0, columnspan=2, sticky=W)
nu = Entry(window, width=5)
nu.grid(column=2, row=1, columnspan=2, sticky=W)
da = Entry(window, width=10)
da.grid(column=2, row=2, sticky=W)
fi = Entry(window, width=20)
fi.grid(column=2, row=3, columnspan=2, sticky=W)
po = Entry(window, width=20)
po.grid(column=2, row=4, columnspan=2, sticky=W)
ad = Entry(window, width=20)
ad.grid(column=2, row=5, columnspan=2, sticky=W)
pa = Entry(window, width=20)
pa.grid(column=2, row=6, columnspan=2, sticky=W)
inn = Entry(window, width=20)
inn.grid(column=2, row=7, sticky=W)
kpp = Entry(window, width=20)
kpp.grid(column=3, row=7, sticky=W)
okpo = Entry(window, width=7)
okpo.grid(column=2, row=8, sticky=W)
ogrn = Entry(window, width=15)
ogrn.grid(column=2, row=9, sticky=W)
okato = Entry(window, width=7)
okato.grid(column=2, row=10, sticky=W)
okved = Entry(window, width=7)
okved.grid(column=2, row=11, sticky=W)
big = Entry(window, width=9)
big.grid(column=2, row=12, sticky=W)
bank = Entry(window, width=40)
bank.grid(column=2, row=13, columnspan=2, sticky=W)
r_s = Entry(window, width=30)
r_s.grid(column=2, row=14, columnspan=2, sticky=W)
k_s = Entry(window, width=30)
k_s.grid(column=2, row=15, columnspan=2, sticky=W)
telefon = Entry(window, width=12)
telefon.grid(column=2, row=16, sticky=W)
email = Entry(window, width=20)
email.grid(column=2, row=17, sticky=W)


def ent():
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


def paste_data():
    if len(big.get()) == 9:
        inn.delete(0, 'end')
        inn.insert(0, Openfile('test_class/spravka.docx').reed_inn())
        kpp.delete(0, 'end')
        kpp.insert(0, Openfile('test_class/spravka.docx').reed_kpp())
        ogrn.delete(0, 'end')
        ogrn.insert(0, Openfile('test_class/spravka.docx').reed_ogrn())
        bank.delete(0, 'end')
        bank. insert(0, name_bank.bank(big.get())['NameP'])
        k_s.delete(0, 'end')
        k_s.insert(0, name_bank.bank(big.get())['Account'])
    else:
        print('inter BIC')


button = Button(window, text='создать договор', command=lambda: ent())
button.grid(column=3, row=20)


button = Button(window, text='заполнить данные', command=lambda: paste_data())
button.grid(column=2, row=20)

window.mainloop()



def input_name_bank():
    print(name_bank.bank(big.get())['NameP'])
    print(name_bank.bank(big.get())['Account'])
    ''' вывод Бик если он есть'''
    big_big = Label(window, text=big.get()).grid(column=4, row=12)
    '''Вывод названия банка'''
    name_Bank = Label(window, text=name_bank.bank(big.get())['NameP'], justify=LEFT) \
        .grid(column=2, row=13, columnspan=2)
    # '''вывод кор счета'''
    # k_s_bank = Label(window, text=name_bank.bank(big.get())['Account'], justify='left') \
    #     .grid(column=2, row=15, columnspan=2)
    return name_Bank
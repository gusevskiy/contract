import xml.etree.ElementTree as ET


# Bic = str('042202603')


def bank(bic) -> dict:
    tree = ET.parse('20220621_ED807_full.xml')
    root = tree.getroot()
    data_bank = {}
    for i in root:
        if i.attrib['BIC'] == bic:
            for x in i:
                data_bank.update(x.attrib)
    return data_bank


        # print("Bank:   ", bank(Bic).get('NameP'))
        # print("Addres: ", bank(Bic).get('Nnp'), bank(Bic).get('Adr'))
        # print("c/a:    ", bank(Bic).get('Account'))


if __name__ == '__main__':
    print(bank()['NameP'])

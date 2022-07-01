from pathlib import Path
import re

from docx import Document


class Openfile:
    def __init__(self, file_path):
        if file_path.endswith('.pdf') or file_path.endswith('.doc'):
            file_path = Path(file_path).stem + ".docx"
            # print(file_path)
        self.file_path = file_path
        self.file_data = None

    def reed(self):
        inn = r"([А-Яа-я]{3})[-|:| ]+(\d{10})"
        self.file_data = Document(self.file_path)
        all_par = self.file_data.paragraphs
        for i in all_par:
            if re.findall(inn, i.text):
                print(re.findall(inn, i.text))
        # print(all_par[2].text)
        # for par in all_par:
        #     print(par.text)


if __name__ == '__main__':
    data_recvi = Openfile('spravka.pdf')
    print(data_recvi.reed())
    # data_spravka = Openfile('spravka.docx')
    # data_spravka.reed()

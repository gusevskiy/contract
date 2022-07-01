from docx import Document


class Openfile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_data = None

    def reed(self):
        if self.file_path.endswith('.txt'):
            with open(self.file_path, 'r') as self.file_data:
                x = self.file_data.read().split('\n')
                print(x)
        if self.file_path.endswith('.docx'):
            self.file_data = Document(self.file_path)
            all_par = self.file_data.paragraphs
            print(all_par)
            # print(all_par[2].text)
            # for par in all_par:
            #     print(par.text)


if __name__ == '__main__':
    # data_recvi = Openfile('recvi.txt')
    # data_recvi.reed()
    data_spravka = Openfile('spravka.docx')
    data_spravka.reed()

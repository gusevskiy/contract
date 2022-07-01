from pathlib import Path

from docx import Document

def open_file(filename):
    if filename.endswith('.pdf'):
        filename = Path(filename).stem + ".docx"
        return filename
    else:
        return filename




doc = Document(open_file('spravka.pdf'))

all_par = doc.paragraphs

print(len(all_par))

for i in all_par:
    print(i.text)
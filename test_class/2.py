from docx import Document


doc = Document('text.doc')

all_par = doc.paragraphs

print(len(all_par))
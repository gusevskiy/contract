from docxtpl import DocxTemplate

name1 = 123

doc = DocxTemplate("C:\code\Moduli\contract\lame1.docx")
context = {'name2': name1}
doc.render(context)
doc.save("lame-final.docx")
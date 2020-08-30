
from PyPDF2 import PdfFileWriter,PdfFileReader
#open pdf 1 and pdf 2
#create a writer object to add the pages from pdf1 and pdf2 
#open a 3rd pdf and write it by using writer object
list_pdf=["C:\\Users\\one.pdf","C:\\Users\\two.pdf"]
writer_obj=PdfFileWriter()
for i in list_pdf:
	read=PdfFileReader(i)
	num=read.getNumPages()
	for j in range(num):
		page=read.getPage(j)
		writer_obj.addPage(page)
pdf=open("C:\\Users\\pdf1+pdf2.pdf",'wb')
writer_obj.write(pdf)

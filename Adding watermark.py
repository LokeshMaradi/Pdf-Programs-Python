from PyPDF2 import PdfFileWriter,PdfFileReader
read1=PdfFileReader("C:\\Users\\pdf1.pdf")
read2=PdfFileReader("C:\\Users\\pdf2.pdf")
page_w=read2.getPage(3)#this is the page where the logo is there, for me lets assume 3rd page
n=read1.getNumPages()
writer_obj1=PdfFileWriter()
for j in range(n):
	page=read1.getPage(j) #Every page will be read here
	page.mergePage(page_w) #Every page will be merged with watermark here
	writer_obj1.addPage(page) #Added to writer object
pdf1=open("C:\\Users\\pdfwatermark.pdf",'wb')
writer_obj1.write(pdf1) #Added to final pdf
pdf1.close()

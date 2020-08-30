from PyPDF2 import PdfFileWriter,PdfFileReader
writer_obj=PdfFileWriter()
#open pdf file which you want to encrypt
pdf=open("C:\\Users\\pdf_for_enc.pdf",'wb')
#to encrypt a pdf
writer_obj.encrypt("pass1","pass2",True) #pass1 and pass2 are for viewing and writing authorizations respectively

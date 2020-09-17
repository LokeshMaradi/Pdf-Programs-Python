from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter 
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
pdf=open('C:\\Users\\ex.pdf','rb')
rm=PDFResourceManager()
lp=LAParams()
mem=io.StringIO()
text=TextConverter(rm,mem, lp)
interp=PDFPageInterpreter(rm,text)
for i in PDFPage.get_pages(pdf):
	interp.process_page(i)
	text=mem.getvalue()
txt=open('C:\\Users\\text.txt','wb')
txt.write(text.encode(utf-8))
print('Done')

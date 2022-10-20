import os
import PyPDF2
from datetime import datetime

class PDF:
    def __init__(self,filePath):
        self.file=open(filePath, 'rb')
        self.Reader=PyPDF2.PdfFileReader(self.file)
        self.Writer = PyPDF2.PdfFileWriter()

        pdfReader = PyPDF2.PdfFileReader(self.file)
        pdfWriter = PyPDF2.PdfFileWriter()

        for pageNum in range(self.Reader.numPages):
            self.Writer.addPage(pdfReader.getPage(pageNum))

    def encrypt(self,password):
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d")
        self.protectedfileName
        fileName=f"protected_{date_time}_{os.path.basename(self.file.name)}"
        self.protectedFileName=fileName
        self.Writer.encrypt(password)
        resultPdf = open(fileName, 'wb')
        self.Writer.write(resultPdf)
        resultPdf.close()
        os.system(resultPdf.name)
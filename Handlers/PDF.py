import PyPDF2


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
        self.Writer.encrypt(password)
        resultPdf = open('encrypted_output.pdf', 'wb')
        self.Writer.write(resultPdf)
        resultPdf.close()
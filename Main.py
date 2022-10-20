import os
from Handlers.PDF import PDF
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkPDFViewer import tkPDFViewer as pdfViewer
import tkinter as tk
import tkinter.simpledialog
from datetime import datetime, timedelta,date
from tkinter import messagebox
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("pdf-pass")
        self.currentPDF = None
        self.geometry('800x800')
        self.setPassButton = tk.Button(self,
            text="Password protect",
            command=self.setPassword
        )

        self.selectFileButton = tk.Button(self,
            text="Select File",
            command=self.select_file
        )

        self.selectFileButton.pack()

    def previewFile(self, filename):
        # creating object of ShowPdf from tkPDFViewer.
        v1 = pdfViewer.ShowPdf()
        v2 = v1.pdf_view(self,
                         pdf_location=filename,
                         width=600, height=500)
        v2.pack()

 
    
   
    def setPDF(self, filename):
        self.filePath=filename
        self.currentPDF = PDF(filename)
        self.previewFile(filename)

    def select_file(self):
        filetypes = (
            ('text files', '*.pdf'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='.',
            filetypes=filetypes)
        if(filename):
            self.setPassButton.pack()
            self.setPDF(filename)


    def setPassword(self):
        
        password = tkinter.simpledialog.askstring(
            "Password", "Enter password:", show='*',parent=self)
        self.currentPDF.encrypt(password)
        
        messagebox.showinfo('OK', 'Saved to',master=self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
from Handlers.PDF import PDF
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkPDFViewer import tkPDFViewer as pdfViewer 
window = tk.Tk()
window.title("pdf-pass")

window.resizable(False, False)
window.geometry('800x800')

greeting = tk.Label(text="Hello, Tkinter")
currentPDF=None


  
# Initializing tk 
def fileView(filename):
# creating object of ShowPdf from tkPDFViewer. 
    v1 = pdfViewer.ShowPdf() 
    
    # Adding pdf location and width and height. 
    v2 = v1.pdf_view(window, 
                    pdf_location = filename,  
                    width = 600, height = 500)

    v2.pack()
def setPDF(filename):
    currentPDF=PDF(filename)
    fileView(filename)
    
def select_file():
    filetypes = (
        ('text files', '*.pdf'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='.',
        filetypes=filetypes)
    if(filename):
        setPDF(filename)



button = tk.Button(
    text="Select File",
    command=select_file
)

button.pack()
window.mainloop()
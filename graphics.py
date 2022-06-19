from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.messagebox import showinfo
import convert
from tkinter import ttk

def select_files():
    filetypes = (
        ('PDF Files', '*.pdf'),
        ('All files', '*.*')
    )
    filename = filedialog.askopenfilenames(
        title='Open PDF',
        initialdir='~/',
        filetypes=filetypes)
    convert.init(filename)

def show_info(title, text):
    showinfo(
        title=title,
        message=text
    )

def init():
    root.mainloop()

def progress(files_size):
    value = 100 / files_size
    pb['value']+= int(value)
    root.update_idletasks()
    root.after(100)

root = Tk()
root.title("PDF to MOBI Converter")
root.geometry("550x300")
root.resizable(width = False, height = False)

l1 = Label(root, text="PDF to MOBI").pack(pady=15)
btn = Button(root, text='Select Files', command=select_files).pack(pady=15)

pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=280
)
pb.pack(pady=15)

#Developed by Jocimar Lopes (https://instagram.com/@jocimarlopes)
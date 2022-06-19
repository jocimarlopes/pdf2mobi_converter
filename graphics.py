from tkinter import *
import customtkinter
from tkinter import filedialog
from tkinter.messagebox import showinfo
import convert

def select_files():
    filetypes = (
        ('PDF Files', '*.pdf'),
        ('All Files', '*.*')
    )
    filename = filedialog.askopenfilenames(
        title='Open PDF',
        initialdir='~/',
        filetypes=filetypes)
    convert.init(filename)

def show_info(title, text):
    showinfo(
        title=title,
        message=text,
    )

def init():
    root.mainloop()

def progress(files_size):
    value = 1 / files_size
    total = pb.value + value
    pb.set(round(total, 2))
    root.update_idletasks()
    root.after(300)

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()
root.title("PDF to MOBI Converter")
root.geometry("550x300")
root.resizable(width=False, height=False)

l1 = customtkinter.CTkLabel(
    root,
    text="Choose any PDF file",
    text_font=('Arial', 18)
    ).pack(pady=15)
    
btn = customtkinter.CTkButton(
    root, 
    text='Select Files', 
    command=select_files,
    ).pack(pady=15)

pb = customtkinter.CTkProgressBar(
    root,
    orient='horizontal',
)
pb.pack(pady=15)
pb.set(0)

credits = customtkinter.CTkLabel(
    root,
    text="Developed by Jocimar Lopes",
    text_font=('Arial', 9)
    ).pack(side=BOTTOM, pady=10)

#Developed by Jocimar Lopes (https://instagram.com/@jocimarlopes)
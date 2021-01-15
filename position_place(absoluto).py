from tkinter import *


fmain = Tk()
fmain.title('Posicionamiento place')
fmain.geometry('400x200')

lb1 = Label(fmain, text='lb1', bg='yellow')
lb1.place(x=10, y=10, width=100, height=30)
lb2 = Label(fmain, text='lb2', bg='red')
lb2.place(x=10, y=50, width=100, height=30)
lb3 = Label(fmain, text='lb3', bg='green')
lb3.place(x=10, y=90, width=100, height=30)

# ubicacion relativa crecera-decrecera segun tamaño del contenedor
lb4 = Label(fmain, text='lb4', bg='yellow')
lb4.place(relx=0.5, rely=0.05, relwidth=0.3, relheight=0.15)
lb5 = Label(fmain, text='lb5', bg='red')
lb5.place(relx=0.5, rely=0.25, relwidth=0.3, relheight=0.15)
lb6 = Label(fmain, text='lb6', bg='green')
lb6.place(relx=0.5, rely=0.45, relwidth=0.3, relheight=0.15)

fmain.mainloop()
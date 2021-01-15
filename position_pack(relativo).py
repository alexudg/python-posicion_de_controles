from tkinter import *


fmain = Tk()
fmain.title('Posicionamiento pack')
fmain.geometry('400x200')

# el componente se ajusta a su contenido

# sin atributo: posicionamiento arriba y horizontalmente centrado
lb1 = Label(fmain, text='lb1', bg='yellow')
lb1.pack()
lb2 = Label(fmain, text='lb2', bg='yellow')
lb2.pack()
# con padding
lb3 = Label(fmain, text='lb3 padxy=5 ipadxy=5', bg='red')
lb3.pack(padx=5, pady=5, ipadx=5, ipady=5)
lb4 = Label(fmain, text='before lb2', bg='green')
lb4.pack(before=lb2)
lb5 = Label(fmain, text='after lb2', bg='green')
lb5.pack(after=lb2)

# con atributo side: posicion puntos cardinales
lb6 = Label(fmain, text='top', bg='yellow')
lb6.pack(side='top')
lb7 = Label(fmain, text='right', bg='red')
lb7.pack(side='right')
lb8 = Label(fmain, text='left', bg='green')
lb8.pack(side='left')
lb9 = Label(fmain, text='bottom', bg='blue')
lb9.pack(side='bottom')

lb10 = Label(fmain, text='expand=true fill=both', bg='orange')
lb10.pack(expand=1, fill='both')
lb11 = Label(fmain, text='expand=true fill=x', bg='salmon')
lb11.pack(expand=1, fill='x')
lb12 = Label(fmain, text='expand=true fill=y', bg='black')
lb12.pack(expand=1, fill='y')

fmain.mainloop()
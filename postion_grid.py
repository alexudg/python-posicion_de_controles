from tkinter import *


fmain = Tk()
fmain.title('Posicionamiento grid')
fmain.geometry('400x200')

#sin atributos row=0 col=0, y despues de arriba hacia abajo solo aumenta row++
lb1 = Label(fmain, text='(sin atributos)', bg='yellow')
lb1.grid()
lb2 = Label(fmain, text='(sin atributos)', bg='red')
lb2.grid()
lb3 = Label(fmain, text='(sin atributos)', bg='green')
lb3.grid()

#con atributos row, column se ordenaran en cuadricula muy ordenada
lb4 = Label(fmain, text='row=0, column=1, padx=5, pady=5', bg='pink')
lb4.grid(row=0, column=1, padx=5, pady=5)
lb5 = Label(fmain, text='row=1, column=1, ipadx=5, ipady=5', bg='blue')
lb5.grid(row=1, column=1, ipadx=5, ipady=5)
lb6 = Label(fmain, text='row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5', bg='salmon')
lb6.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5)

# expandir columna y fila, sticky es como anchor o ancla o estiramiento en sus puntos cardinales
lb7 = Label(fmain, text='row=3, column=0, columnspan=2 rowconfigure(3 weight=1) sticky=ns', bg='silver')
lb7.grid(row=3, column=0, columnspan=2, sticky='ns')
lb8 = Label(fmain, text='row=0, column=2, rowspan=2 columnconfigure(2 weight=1) sticky=nsew', bg='silver')
lb8.grid(row=0, column=2, rowspan=2, sticky='nsew')

# expandir columna 2 y fila 3 el 100% del espacio disponible aun creciendo la ventana
fmain.columnconfigure(2, weight=1)
fmain.rowconfigure(3, weight=100)

# ademas existen tambien los atributos 
# minsize=px int
# pad=px int (padding externo entre celdas)

fmain.mainloop()
import tkinter
def imprimir():
    print("Hola mundo")
Ventana = tkinter.Tk()
Ventana.title("Ejemplo de botones")
Ventana.geometry("400x600")
etiqueta = tkinter.Label(Ventana, text="Hola mundo") #Etiqueta
#etiqueta.pack()  #Deja la etiqueta en el centro, solamente 1 elemento
etiqueta.grid(row=0, column=0)
entrada = tkinter.Entry(Ventana) #CAJA DE TEXTO
entrada.grid(row=0, column=1)
#entrada.pack()
etiqueta1 = tkinter.Label(Ventana, text="Qué lenguaje utilizas?")
etiqueta1.grid(row=1, column=0)
lista = tkinter.Listbox(Ventana) #Caja de Lista
lista.grid(row=1, column=1) #Ubicación en la grilla
lista.insert(1, "Python") #Elementos de la lista
lista.insert(2, "Java")
lista.insert(3, "C++")
Boton = tkinter.Button(Ventana, text="Aceptar", command=imprimir)
Boton.grid(row=2, columnspan=2) #columnspan=2, ocupa 2 columnas
checkbox = tkinter.Checkbutton(Ventana, text="Acepto términos y condiciones")
checkbox.grid(row=3, columnspan=2)
radio = tkinter.Radiobutton(Ventana, text="Mujer")
radio.grid(row=4, column=0)
radio1 = tkinter.Radiobutton(Ventana, text="Hombre")
radio1.grid(row=4, column=1)
Ventana.mainloop()
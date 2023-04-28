#---------------------------------
# Desktop app No. 1
#---------------------------------

# se importa la libreria tkinter con todas sus funciones 
from tkinter import *

#----------------------------
# funciones de la app
#----------------------------

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("bandera de España")

# tamaño de la ventana
ventana_principal.geometry("900x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="yellow")

#--------------------------------
# frame rojo
#--------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=900, height=125)
frame_rojo.place(x=0, y=0)

#--------------------------------
# frame amarillo
#--------------------------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo.config(bg="yellow", width=900, height=250)
frame_amarillo.place(x=0, y=250)

#--------------------------------
# frame rojo
#--------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=900, height=125)
frame_rojo.place(x=0, y=375)

#--------------------------------
# frame rojo
#--------------------------------   
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=100, height=100)
frame_rojo.place(x=120, y=200)

# run 
ventana_principal.mainloop()
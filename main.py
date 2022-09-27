"""
José David Panaza Batres
Carné: 202111478
Programación Orientada a Objetos
Introducción a la programación 2
"""
import tkinter as tk
from tkinter import DISABLED, NORMAL, Toplevel, ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import *
from xml.dom import minidom
import tkinter.font as font
from tkinter import font
#CLASES
from Cola import Cola
from Empresa import Empresa
from PuntoAtencion import PuntoAtencion
from Escritorio import Escritorio
colaempresas = Cola()
root = tk.Tk()
root.title('FIUSAC')
root.resizable(False, False)
# Tamaño y posicionamiento de la ventana
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

label = tk.Label(root, text='SOLUCIONES GUATEMALTECAS, S.A',font=("Britannic Bold",18))
label.pack()
label.place(x=130, y=30)

def cargar_archivo():
    filetypes = (('Archivos XML', '*.xml'), ('Todos los archivos', '*.*'))
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    if filename == "":
            messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo")            
    else:
        doc = minidom.parse(filename)
        empresas = doc.getElementsByTagName("empresa")
        for empresa in empresas:
            #Atributos de la empresa
            id = empresa.getAttribute("id")
            nombre = empresa.getElementsByTagName("nombre")[0]
            abreviatura = empresa.getElementsByTagName("abreviatura")[0]
            nempresa = Empresa(id, nombre, abreviatura)
            #Agregar empresa a la cola
            colaempresas.insertar(nempresa)
            #n puntos de atencion
            puntosdeatencion = empresa.getElementsByTagName("puntoAtencion")
            for punto in puntosdeatencion:
                #Atributos puntos de atencion
                id = punto.getAttribute("id")
                nombre = punto.getElementsByTagName("nombre")[0]
                direccion = punto.getElementsByTagName("direccion")[0]
                npuntoAtencion = PuntoAtencion(id,nombre,direccion)
                #Agregar puntos de atencion a una cola
                nempresa.agregarPuntos(npuntoAtencion)
                #n escritorios
                escritorios = punto.getElementsByTagName("escritorio")
                for escritorio in escritorios:
                    id = escritorio.getAttribute("id")
                    identificacion = escritorio.getElementsByTagName("identificacion")[0]
                    encargado = escritorio.getElementsByTagName("encargado")[0]
                    nescritorio = Escritorio(id,identificacion,encargado,False)
                    #Agregar escritorios al punto de atención
                    npuntoAtencion.agregarEscritorio(nescritorio)
                pass
            pass
        pass
    pass

# VENTANA PRINCIPAL
###
carga_button = ttk.Button(
    root,
    text="Configurar empresa",
    command=cargar_archivo
)
carga_button.pack(
    ipadx=10,
    ipady=10,
    expand=True
)
carga_button.place(x=240, y=160, width=150, height=80)

salir_button = ttk.Button(
    root,
    text="Salir",
    command=lambda: root.quit(),
)
salir_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
salir_button.place(x=10, y=330, width=150, height=50)
root.mainloop()

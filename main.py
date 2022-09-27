"""
José David Panaza Batres
Carné: 202111478
Programación Orientada a Objetos
Introducción a la programación 2
"""
from functools import partial
import tkinter as tk
from tkinter import DISABLED, NORMAL, Toplevel, ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import *
from xml.dom import minidom
import tkinter.font as font
from tkinter import font
#CLASES DE ESTRUCTURAS
from Cola import Cola
from Empresa import Empresa
from PuntoAtencion import PuntoAtencion
from Escritorio import Escritorio
from Transaccion import Transaccion
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
        #CREACION VENTANA      
        wempresas = Toplevel(root)
        wempresas.title("Empresas")
        wempresas.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        wempresas.grab_set()
        wempresas.resizable(False, False)
        var = wempresas
        label = tk.Label(wempresas, text='CONFIGURE UNA EMPRESA',font=("Britannic Bold",18))
        label.pack()
        label.place(x=150, y=30)
        doc = minidom.parse(filename)
        empresas = doc.getElementsByTagName("empresa")
        cont = 0
        posx = 0
        posy = 0
        for empresa in empresas:
            #Atributos de la empresa
            id = empresa.getAttribute("id")
            nombre = empresa.getElementsByTagName("nombre")[0].firstChild.data
            abreviatura = empresa.getElementsByTagName("abreviatura")[0].firstChild.data
            nempresa = Empresa(id, nombre, abreviatura)
            #Creacion botones            
            boton = ttk.Button(
                wempresas,
                text=nombre,
                command=partial(configurar_empresa,id)
            )
            boton.pack(
                ipadx=10,
                ipady=10,
                expand=True
            )
            boton.place(x=50 + posx, y=100 + posy, width=150, height=50)                
            cont+=1
            posx += 150
            if(cont == 3 or cont == 6):
                posy += 60
                posx = 0
            
            #Agregar empresa a la cola
            colaempresas.insertar(nempresa)
            #n transacciones
            transacciones = empresa.getElementsByTagName("transaccion")
            for transaccion in transacciones:
                id = transaccion.getAttribute("id")
                nombre = transaccion.getElementsByTagName("nombre")[0].firstChild.data
                tiempoAtencion = transaccion.getElementsByTagName("tiempoAtencion")[0].firstChild.data
                ntransaccion = Transaccion(id, nombre, tiempoAtencion, 0)
                #Agregar transacciones a la empresa
                nempresa.agregarTransaccion(ntransaccion)
            #n puntos de atencion
            puntosdeatencion = empresa.getElementsByTagName("puntoAtencion")
            for punto in puntosdeatencion:
                #Atributos puntos de atencion
                id = punto.getAttribute("id")
                nombre = punto.getElementsByTagName("nombre")[0].firstChild.data
                direccion = punto.getElementsByTagName("direccion")[0].firstChild.data
                npuntoAtencion = PuntoAtencion(id,nombre,direccion)
                #Agregar puntos de atencion a una cola
                nempresa.agregarPuntos(npuntoAtencion)
                #n escritorios
                escritorios = punto.getElementsByTagName("escritorio")
                for escritorio in escritorios:
                    id = escritorio.getAttribute("id")
                    identificacion = escritorio.getElementsByTagName("identificacion")[0].firstChild.data
                    encargado = escritorio.getElementsByTagName("encargado")[0].firstChild.data
                    nescritorio = Escritorio(id,identificacion,encargado,False)
                    #Agregar escritorios al punto de atención
                    npuntoAtencion.agregarEscritorio(nescritorio)
                pass
            pass
        pass
    pass
def configurar_empresa(idempresa):
    wpuntos = Toplevel(root)
    wpuntos.title("Puntos")
    wpuntos.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    wpuntos.grab_set()
    wpuntos.resizable(False, False)    
    empresa = colaempresas.extraerid(idempresa)
    

# VENTANA PRINCIPAL
###
carga_button = ttk.Button(
    root,
    text="Cargar empresas",
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

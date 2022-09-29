"""
José David Panaza Batres
Carné: 202111478
Programación Orientada a Objetos
Introducción a la programación 2
"""
import copy
from functools import partial
import tkinter as tk
from tkinter import DISABLED, NORMAL, Toplevel
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
from Cliente import Cliente
from Config import Config
colaempresas = Cola()
colaconfiguracion = Cola()
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
myFont = font.Font(family="Britannic Bold", size=10,weight="normal",)
label = tk.Label(root, text='SOLUCIONES GUATEMALTECAS, S.A',font=("Britannic Bold",18))
label.pack()
label.place(x=130, y=30)
cargar = True
#VENTANA PARA MOSTRAR EMPRESAS
def cargar_archivo():
    global cargar
    if(cargar == True or cargar == False):
        filetypes = (('Archivos XML', '*.xml'), ('Todos los archivos', '*.*'))
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        if filename == "":            
            if(cargar == False):
                mostrar_empresas()
            else:
                messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo")         
        else:
            doc = minidom.parse(filename)
            empresas = doc.getElementsByTagName("empresa")
            cargar = False
            for empresa in empresas:
                #Atributos de la empresa
                id = empresa.getAttribute("id")
                if (colaempresas.extraerid(id) == False):
                    nombre = empresa.getElementsByTagName("nombre")[0].firstChild.data
                    abreviatura = empresa.getElementsByTagName("abreviatura")[0].firstChild.data
                    nempresa = Empresa(id, nombre, abreviatura)            
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
            mostrar_empresas()
        pass
    else:
        mostrar_empresas()
#VENTANA PARA MOSTRAR PUNTOS DE ATENCION
def mostrar_empresas():
    global colaempresas
    wempresas = Toplevel(root)
    wempresas.title("Empresas")
    wempresas.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    wempresas.grab_set()
    wempresas.resizable(False, False)
    label = tk.Label(wempresas, text='CONFIGURE UNA EMPRESA',font=("Britannic Bold",18))
    label.pack()
    label.place(x=150, y=30)
    cont = 0
    posx = 0
    posy = 0
    nempresas = colaempresas.getlen()
    colaempresatemp = Cola()
    for i in range(0,nempresas,1):
        nempresa = colaempresas.extraer()
        nempresa.siguiente = None
        colaempresatemp.insertar(nempresa)
        boton = tk.Button(
            wempresas,
            bg="#8FA0AC",
            font=myFont,
            text=nempresa.nombre,
            command=partial(configurar_empresa,nempresa)
        )
        boton.pack(
            ipadx=10,
            ipady=10,
            expand=True
        )
        boton.place(x=50 + posx, y=100 + posy, width=150, height=50)                
        cont+=1
        posx += 160
        if(cont == 3 or cont == 6):
            posy += 60
            posx = 0
    boton = tk.Button(
        wempresas,
        bg="#8FA0AC",
        font=myFont,
        text="CREAR EMPRESA",
        command=partial(crear_empresas,wempresas)
    )
    boton.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    boton.place(x=120, y=300, width=150, height=50) 
    boton1 = tk.Button(
        wempresas,
        bg="#8FA0AC",
        font=myFont,
        text="Manejar pruebas",
        command=partial(prueba_inicial,None)
    )
    boton1.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    boton1.place(x=340, y=300, width=150, height=50)    
    colaempresas = colaempresatemp
    if(colaempresas.getlen() == 0):
        boton1['state'] = DISABLED
    else:
        boton1['state'] = NORMAL
def prueba_inicial(ventana):
    filetypes = (('Archivos XML', '*.xml'), ('Todos los archivos', '*.*'))
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    if filename == "":
        messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo")            
    else:
        doc = minidom.parse(filename)
        configs = doc.getElementsByTagName("configInicial")
        for config in configs:
            #GUARDAR LA CONFIGURACION
            id = config.getAttribute("id")
            if (colaconfiguracion.extraerid(id) == False):
                idempresa = config.getAttribute("idEmpresa")
                idpunto = config.getAttribute("idPunto")
                #ACTIVAR LOS ESCRITORIOS
                escritoriosactivos = config.getElementsByTagName("escritorio")
                empresa = colaempresas.extraerid(idempresa)
                punto = empresa.puntosatencion.extraerid(idpunto)
                #objeto config
                nconfig = Config(id,idempresa,idpunto,empresa.nombre,punto.nombre)
                colaconfiguracion.insertar(nconfig)
                for escritorioa in escritoriosactivos:
                    idescritorio = escritorioa.getAttribute("idEscritorio")
                    nescri = punto.escritorios.extraerid(idescritorio)
                    configurar_escritorios(nescri,punto,None)
                    pass
                #GUARDAR CLIENTES
                clientes = config.getElementsByTagName("cliente")
                for cliente in clientes:
                    idcliente = cliente.getAttribute("dpi")
                    nombre = cliente.getElementsByTagName("nombre")[0].firstChild.data
                    ncliente = Cliente(idcliente,nombre)
                    punto.agregarCliente(ncliente)
                    #GUARDAR TRANSACCIONES
                    transacciones = cliente.getElementsByTagName("transaccion")
                    for transaccion in transacciones:
                        idtransaccion = transaccion.getAttribute("idTransaccion")
                        cantidad = transaccion.getAttribute("cantidad")
                        ncliente.agregarTransaccion(idtransaccion,cantidad,empresa)   
        if(ventana != None):
            ventana.destroy()
        mostrar_pruebas()
def mostrar_pruebas():
    global colaconfiguracion
    wconfig = Toplevel(root)
    wconfig.title("Configuraciones")
    wconfig.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    wconfig.grab_set()
    wconfig.resizable(False, False)
    label = tk.Label(wconfig, text='ELIJA UN PUNTO PARA LA PRUEBA',font=("Britannic Bold",18))
    label.pack()
    label.place(x=150, y=30)
    cont = 0
    posx = 0
    posy = 0
    nconfigs = colaconfiguracion.getlen()
    colaconftemp = Cola()
    for i in range(0,nconfigs,1):
        nconfig = colaconfiguracion.extraer()
        nconfig.siguiente = None
        colaconftemp.insertar(nconfig)
        boton = tk.Button(
            wconfig,
            bg="#8FA0AC",
            font=myFont,
            text=nconfig.nempresa + "-" + nconfig.npunto,
            command=partial(realizar_prueba,nconfig)
        )
        boton.pack(
            ipadx=10,
            ipady=10,
            expand=True
        )
        boton.place(x=50 + posx, y=100 + posy, width=250, height=50)                
        cont+=1
        posx += 260
        if(cont == 2 or cont == 4 or cont == 6):
            posy += 60
            posx = 0   
    boton = tk.Button(
        wconfig,
        bg="#8FA0AC",
        font=myFont,
        text="CARGAR PRUEBA",
        command=partial(prueba_inicial,wconfig)
    )
    boton.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    boton.place(x=230, y=300, width=150, height=50)   
    colaconfiguracion = colaconftemp
    pass
def realizar_prueba(prueba):
    #CONFIGURACION VENTANA
    wprueba = Toplevel(root)
    wprueba.title("Pruebas")
    wprueba.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    wprueba.grab_set()
    wprueba.resizable(False,False)    
    w = Canvas(wprueba,width=600,height=400)
    w.create_rectangle(10,30,400,330, outline="red")
    w.create_rectangle(10,30,400,60, outline="red")
    w.create_rectangle(410,30,590,330, outline="red")
    w.create_rectangle(410,30,590,60, outline="red")
    w.pack()
    label = tk.Label(wprueba, text=prueba.nempresa + " - " + prueba.npunto,font=("Britannic Bold",15))
    label.pack()
    label.place(x=135, y=0)
    label12 = tk.Label(wprueba, text="ESCRITORIOS ACTIVOS:",font=("Britannic Bold",11))
    label12.pack()
    label12.place(x=12, y=35)
    label1 = tk.Label(wprueba, text="ES TU TURNO:",font=("Britannic Bold",11))
    label1.pack()
    label1.place(x=12, y=62)
    label2 = tk.Label(wprueba, text="EN ESPERA:",font=("Britannic Bold",11))
    label2.pack()
    label2.place(x=412, y=35)
    #CREACION VARIABLES
    empresa = colaempresas.extraerid(prueba.idempresa)
    punto = empresa.puntosatencion.extraerid(prueba.idpunto)
    numescritoriosactivos = punto.escritoriosactivos.getlen()
    #ESCRITORIOS ACTIVOS VENTANA
    label3 = tk.Label(wprueba, text=numescritoriosactivos,font=("Britannic Bold",11))
    label3.pack()
    label3.place(x=175, y=35)
    #CLIENTES EN ESPERA VENTANA
    numclientes = punto.clientes.getlen()
    colaclientestemp = Cola()
    posy = 0
    for i in range(0,numclientes,1):
        ncliente = punto.clientes.extraer()
        ncliente.siguiente = None
        colaclientestemp.insertar(ncliente)
        labelc = tk.Label(wprueba, text="- "+ncliente.nombre,font=("Britannic Bold",11))
        labelc.pack()
        labelc.place(x=412, y=62 + posy)
        posy += 20
        pass
    punto.clientes = colaclientestemp
    pass
    #BOTONES
    boton0 = tk.Button(
        wprueba,
        bg="#8FA0AC",
        font=myFont,
        text="RECARGAR",
        command=partial(recargar,prueba,wprueba)
    )
    boton0.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    boton0.place(x=500, y=2, width=97, height=20)
    boton = tk.Button(
        wprueba,
        bg="#8FA0AC",
        font=myFont,
        text="ATENDER\nCLIENTE",
        command=partial(atender_cliente,punto,wprueba)
    )
    boton.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    boton.place(x=1, y=345, width=97, height=50)
    boton1 = tk.Button(
        wprueba,
        bg="#8FA0AC",
        font=myFont,
        text="SIMULAR\nATENCION",
        command=partial(simular,punto,wprueba)
    )
    boton1.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    boton1.place(x=101, y=345, width=97, height=50)
    boton2 = tk.Button(
        wprueba,
        bg="#8FA0AC",   
        font=myFont,     
        text="AGREGAR\nCLIENTE",
        command=partial(agregar_cliente,punto,wprueba)
    )
    boton2.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    boton2.place(x=201, y=345, width=97, height=50)
    boton3 = tk.Button(
        wprueba,
        bg="#8FA0AC",   
        font=myFont,     
        text="VER INFO.\nPUNTO",
        command=partial(ver_punto,punto)
    )
    boton3.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    boton3.place(x=301, y=345, width=97, height=50)
    boton4 = tk.Button(
        wprueba,
        bg="#8FA0AC",   
        font=myFont,     
        text="VER INFO.\nESCRITORIOS",
        command=partial(ver_escritorios,punto)
    )
    boton4.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    boton4.place(x=401, y=345, width=97, height=50)
    boton4 = tk.Button(
        wprueba,
        bg="#8FA0AC",   
        font=myFont,     
        text="MANEJAR\nESCRITORIOS",
        command=partial(configurar_puntos,punto)
    )
    boton4.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    boton4.place(x=501, y=345, width=97, height=50)
def recargar(prueba, ventana):
    ventana.destroy()
    realizar_prueba(prueba)
def atender_cliente(punto, ventana):
    pass
def simular(punto, ventana):
    pass
def agregar_cliente(punto,ventana):
    pass
def ver_punto(punto):
    pass
def ver_escritorios(punto):
    pass

def configurar_empresa(empresa):
    wpuntos = Toplevel(root)
    wpuntos.title("Puntos")
    wpuntos.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    wpuntos.grab_set()
    wpuntos.resizable(False, False)  
    label = tk.Label(wpuntos, text='SELECCIONE UN PUNTO',font=("Britannic Bold",18))
    label.pack()
    label.place(x=170, y=30)
    npuntos = empresa.puntosatencion.getlen()
    if(npuntos > 0):
        colapuntostemp = Cola()
        cont = 0
        posx = 0
        posy = 0
        for i in range(0,npuntos,1):
            npunto = empresa.puntosatencion.extraer()
            npunto.siguiente = None
            colapuntostemp.insertar(npunto)
            boton = tk.Button(
                wpuntos,
                bg="#8FA0AC",
                font=myFont,
                text=npunto.nombre,
                command=partial(configurar_puntos,npunto)
            )
            boton.pack(
                ipadx=10,
                ipady=10,
                expand=True
            )
            boton.place(x=50 + posx, y=100 + posy, width=150, height=50)                
            cont+=1
            posx += 160
            if(cont == 3 or cont == 6):
                posy += 60
                posx = 0            
        empresa.puntosatencion = colapuntostemp
    boton = tk.Button(
        wpuntos,
        bg="#8FA0AC",
        font=myFont,
        text="CREAR PUNTO",
        command=partial(crear_puntos,empresa,wpuntos)
    )
    boton.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    boton.place(x=50, y=300, width=150, height=50)
    boton1 = tk.Button(
        wpuntos,
        bg="#8FA0AC",
        font=myFont,
        text="CREAR TRANSACCIONES",
        command=partial(crear_transacciones,empresa,wpuntos)
    )
    boton1.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    boton1.place(x=210, y=300, width=150, height=50) 
    boton2 = tk.Button(
        wpuntos,
        bg="#8FA0AC",
        font=myFont,
        text="VER TRANSACCIONES",
        command=partial(ver_transacciones,empresa)
    )
    boton2.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    boton2.place(x=370, y=300, width=150, height=50) 
#VENTANA PARA MOSTRAR ESCRITORIOS
def configurar_puntos(punto):
    wescritorios = Toplevel(root)
    wescritorios.title("Escritorios")
    wescritorios.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    wescritorios.grab_set()
    wescritorios.resizable(False, False)  
    label = tk.Label(wescritorios, text='ACTIVE UN ESCRITORIO',font=("Britannic Bold",18))
    label.pack()
    label.place(x=170, y=30)  
    nescritorios = punto.escritorios.getlen()
    if (nescritorios > 0):
        colaescritoriotemp = Cola()
        cont = 0
        posx = 0
        posy = 0
        for i in range(0,nescritorios,1):
            nescritorio = punto.escritorios.extraer()
            nescritorio.siguiente = None
            colaescritoriotemp.insertar(nescritorio)
            boton = tk.Button(
                wescritorios,
                font=myFont,
                text=nescritorio.id + "-"+ nescritorio.nombreEncargado,
                command=partial(configurar_escritorios,nescritorio,punto,wescritorios)
            )
            boton.pack(
                ipadx=10,
                ipady=10,
                expand=True
            )
            boton.place(x=50 + posx, y=100 + posy, width=150, height=50)         
            if nescritorio.estado == False:
                boton.configure(bg="#E06D6D")
            else:
                boton.configure(bg="#97E06D")            
            cont+=1
            posx += 160
            if(cont == 3 or cont == 6):
                posy += 60
                posx = 0    
        punto.escritorios = colaescritoriotemp
    boton = tk.Button(
        wescritorios,
        bg="#8FA0AC",
        font=myFont,
        text="CREAR ESCRITORIO",
        command=partial(crear_escritorios,punto,wescritorios)
    )
    boton.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    boton.place(x=120, y=300, width=150, height=50) 
    boton1 = tk.Button(
        wescritorios,
        bg="#8FA0AC",
        font=myFont,
        text="DESACTIVAR ESCRITORIO",
        command=partial(desactivar_escritorios,punto,wescritorios)
    )
    boton1.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    boton1.place(x=330, y=300, width=150, height=50) 
    pass
def configurar_escritorios(escritorio,punto,ventana):    
    if escritorio.estado == False:
        escritorio.estado = True
        escritorion = copy.deepcopy(escritorio)
        escritorion.siguiente = None
        punto.activarEscritorio(escritorion)        
        if ventana != None:
            ventana.destroy()
            configurar_puntos(punto)

    pass
def desactivar_escritorios(punto,ventana):    
    oper = punto.desactivarEscritorio()
    if(oper == True):
        ventana.destroy()
        configurar_puntos(punto)    
    pass
def crear_empresas(ventana):
    wcreare = Toplevel(root)
    wcreare.title("Crear_Empresas")
    wcreare.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    wcreare.grab_set()
    wcreare.resizable(False, False)
    label = tk.Label(wcreare, text='CREAR UNA EMPRESA',font=("Britannic Bold",18))
    label.pack()
    label.place(x=170, y=30)
    #ID
    lid = tk.Label(wcreare, text="ID: ")
    lid.pack()
    lid.place(x=70, y=90, height=20)
    celda = Entry(wcreare, width=45, fg='black',font=('Arial', 10, 'normal'))
    celda.place(x=170, y=90, height=20)
    #Nombre
    lnombre = tk.Label(wcreare, text="Nombre: ")
    lnombre.pack()
    lnombre.place(x=70, y=120, height=20)
    celda1 = Entry(wcreare, width=45, fg='black',font=('Arial', 10, 'normal'))
    celda1.place(x=170, y=120, height=20)
    # Abre
    labre = tk.Label(wcreare, text="Abreviatura: ")
    labre.pack()
    labre.place(x=70, y=150, height=20)
    celda2 = Entry(wcreare, width=45, fg='black', font=('Arial', 10, 'normal'))
    celda2.place(x=170, y=150, height=20)
    #BOTON
    def nueva_empresa():
        if(celda.get() != "" and celda1.get() != "" and celda2.get() != ""):
            empresa = Empresa(celda.get(),celda1.get(),celda2.get())
            colaempresas.insertar(empresa)
            wcreare.destroy()
            ventana.destroy()
            mostrar_empresas()
            pass
        else:
            messagebox.showwarning("Advertencia", "Asegurese de llenar los espacios obligatorios para crear una empresa")
        pass
    crear = tk.Button(
        wcreare,
        bg="#8FA0AC",
        font=myFont,
        text="Crear",
        command=nueva_empresa
    )
    crear.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    crear.place(x=250, y=340, width=150, height=50)
    pass
def crear_puntos(empresa,ventana):
    wcrearp = Toplevel(root)
    wcrearp.title("Crear_Puntos")
    wcrearp.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    wcrearp.grab_set()
    wcrearp.resizable(False, False)
    label = tk.Label(wcrearp, text='CREAR UN PUNTO DE ATENCION',font=("Britannic Bold",18))
    label.pack()
    label.place(x=170, y=30)
    #ID
    lid = tk.Label(wcrearp, text="ID: ")
    lid.pack()
    lid.place(x=70, y=90, height=20)
    celda = Entry(wcrearp, width=45, fg='black',font=('Arial', 10, 'normal'))
    celda.place(x=170, y=90, height=20)
    #Nombre
    lnombre = tk.Label(wcrearp, text="Nombre: ")
    lnombre.pack()
    lnombre.place(x=70, y=120, height=20)
    celda1 = Entry(wcrearp, width=45, fg='black',font=('Arial', 10, 'normal'))
    celda1.place(x=170, y=120, height=20)
    # Abre
    labre = tk.Label(wcrearp, text="Direccion: ")
    labre.pack()
    labre.place(x=70, y=150, height=20)
    celda2 = Entry(wcrearp, width=45, fg='black', font=('Arial', 10, 'normal'))
    celda2.place(x=170, y=150, height=20)
    #BOTON
    def nuevo_punto():
        if(celda.get() != "" and celda1.get() != "" and celda2.get() != ""):
            punto = PuntoAtencion(celda.get(),celda1.get(),celda2.get())
            empresa.agregarPuntos(punto)
            wcrearp.destroy()
            ventana.destroy()
            configurar_empresa(empresa)
            pass
        else:
            messagebox.showwarning("Advertencia", "Asegurese de llenar los espacios obligatorios para crear un punto de atencion")
        pass
    crear = tk.Button(
        wcrearp,
        bg="#8FA0AC",
        font=myFont,
        text="Crear",
        command=nuevo_punto
    )
    crear.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    crear.place(x=250, y=340, width=150, height=50)
    pass
def crear_escritorios(punto,ventana):
    wcreares = Toplevel(root)
    wcreares.title("Crear_Escritorios")
    wcreares.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    wcreares.grab_set()
    wcreares.resizable(False, False)
    label = tk.Label(wcreares, text='CREAR UN ESCRITORIO',font=("Britannic Bold",18))
    label.pack()
    label.place(x=170, y=30)
    #ID
    lid = tk.Label(wcreares, text="ID: ")
    lid.pack()
    lid.place(x=70, y=90, height=20)
    celda = Entry(wcreares, width=45, fg='black',font=('Arial', 10, 'normal'))
    celda.place(x=170, y=90, height=20)
    #Nombre
    lnombre = tk.Label(wcreares, text="Tipo: ")
    lnombre.pack()
    lnombre.place(x=70, y=120, height=20)
    celda1 = Entry(wcreares, width=45, fg='black',font=('Arial', 10, 'normal'))
    celda1.place(x=170, y=120, height=20)
    # Abre
    labre = tk.Label(wcreares, text="Encargado: ")
    labre.pack()
    labre.place(x=70, y=150, height=20)
    celda2 = Entry(wcreares, width=45, fg='black', font=('Arial', 10, 'normal'))
    celda2.place(x=170, y=150, height=20)
    #BOTON
    def nuevo_escritorio():
        if(celda.get() != "" and celda1.get() != "" and celda2.get() != ""):
            escritorio = Escritorio(celda.get(),celda1.get(),celda2.get(),False)
            punto.agregarEscritorio(escritorio)
            wcreares.destroy()
            ventana.destroy()
            configurar_puntos(punto)
            pass
        else:
            messagebox.showwarning("Advertencia", "Asegurese de llenar los espacios obligatorios para crear un punto de atencion")
        pass
    crear = tk.Button(
        wcreares,
        bg="#8FA0AC",
        font=myFont,
        text="Crear",
        command=nuevo_escritorio
    )
    crear.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    crear.place(x=250, y=340, width=150, height=50)
    pass
def crear_transacciones(empresa,ventana):
    wcrearp = Toplevel(root)
    wcrearp.title("Crear_Transaccion")
    wcrearp.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    wcrearp.grab_set()
    wcrearp.resizable(False, False)
    label = tk.Label(wcrearp, text='CREAR TRANSACCION',font=("Britannic Bold",18))
    label.pack()
    label.place(x=170, y=30)
    #ID
    lid = tk.Label(wcrearp, text="ID: ")
    lid.pack()
    lid.place(x=70, y=90, height=20)
    celda = Entry(wcrearp, width=45, fg='black',font=('Arial', 10, 'normal'))
    celda.place(x=170, y=90, height=20)
    #Nombre
    lnombre = tk.Label(wcrearp, text="Nombre: ")
    lnombre.pack()
    lnombre.place(x=70, y=120, height=20)
    celda1 = Entry(wcrearp, width=45, fg='black',font=('Arial', 10, 'normal'))
    celda1.place(x=170, y=120, height=20)
    # Abre
    labre = tk.Label(wcrearp, text="Minutos: ")
    labre.pack()
    labre.place(x=70, y=150, height=20)
    celda2 = Entry(wcrearp, width=45, fg='black', font=('Arial', 10, 'normal'))
    celda2.place(x=170, y=150, height=20)
    #BOTON
    def nuevo_punto():
        if(celda.get() != "" and celda1.get() != "" and celda2.get() != ""):
            trans = Transaccion(celda.get(),celda1.get(),celda2.get(),0)
            empresa.agregarTransaccion(trans)
            wcrearp.destroy()
            ventana.destroy()
            configurar_empresa(empresa)
            pass
        else:
            messagebox.showwarning("Advertencia", "Asegurese de llenar los espacios obligatorios para crear un punto de atencion")
        pass
    crear = tk.Button(
        wcrearp,
        bg="#8FA0AC",
        font=myFont,
        text="Crear",
        command=nuevo_punto
    )
    crear.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    crear.place(x=250, y=340, width=150, height=50)
    pass
def ver_transacciones(empresa):
    wver = Toplevel(root)
    wver.title("Escritorios")
    wver.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    wver.grab_set()
    wver.resizable(False, False)  
    label = tk.Label(wver, text='VER TIPOS DE TRANSACCIONES',font=("Britannic Bold",18))
    label.pack()
    label.place(x=170, y=30)  
    ntrans = empresa.transacciones.getlen()
    if (ntrans > 0):
        colatranstemp = Cola()
        cont = 0
        posx = 0
        posy = 0
        for i in range(0,ntrans,1):
            ntransaccion = empresa.transacciones.extraer()
            ntransaccion.siguiente = None
            colatranstemp.insertar(ntransaccion)
            boton = tk.Button(
                wver,
                font=myFont,
                text=ntransaccion.nombre + ": " + ntransaccion.minutos + " min",
                state=DISABLED
            )
            boton.pack(
                ipadx=10,
                ipady=10,
                expand=True
            )
            boton.place(x=50 + posx, y=100 + posy, width=150, height=50)           
            cont+=1
            posx += 160
            if(cont == 3 or cont == 6):
                posy += 60
                posx = 0    
        empresa.transacciones = colatranstemp
    pass
def limpiar():
    global colaempresas
    global colaconfiguracion
    global cargar
    colaconfiguracion = Cola()
    colaempresas = Cola()
    cargar = True
    messagebox.showinfo("INFORMACION","Se limpió el sistema exitosamente")
    pass
# VENTANA PRINCIPAL
###
carga_button = tk.Button(
    root,
    bg="#8FA0AC",
    font=myFont,
    text="Manejar empresas",
    command=cargar_archivo
)
carga_button.pack(
    ipadx=10,
    ipady=10,
    expand=True
)
carga_button.place(x=240, y=160, width=150, height=80)
limpiar_button = tk.Button(
    root,
    bg="#8FA0AC",
    font=myFont,
    text="Limpiar sistema",
    command=limpiar,
)
limpiar_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
limpiar_button.place(x=430, y=330, width=150, height=50)
salir_button = tk.Button(
    root,
    bg="#8FA0AC",
    font=myFont,
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

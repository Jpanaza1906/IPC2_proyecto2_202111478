from math import sqrt
import math
from Cola import Cola
class PuntoAtencion:
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.siguiente = None
        self.escritorios = Cola()
        self.escritoriosactivos = Cola()
        self.historialclientes = Cola()
        self.clientes = Cola()
    def agregarEscritorio(self, escritorio):
        if(self.escritorios.extraerid(escritorio.id) == False):
            self.escritorios.insertar(escritorio)
        else:
            return False
    def desocuparEscritorios(self):
        cabezaescritorios = self.escritoriosactivos.cabeza()
        numescri = self.escritoriosactivos.getlen()
        for i in range(0,numescri,1):
            cabezaescritorios.ocupado = False
            cabezaescritorios = cabezaescritorios.siguiente
    def activarEscritorio(self, escritorio):
        self.escritoriosactivos.insertar(escritorio)
        self.escritoriosactivos.crearReporte()
    def desactivarEscritorio(self):
        escritorio = self.escritoriosactivos.extraer()
        if(escritorio != None):
            escritoriofdesactivar = self.escritorios.extraerid(escritorio.id)
            escritoriofdesactivar.estado = False
            self.escritoriosactivos.crearReporte()
            return True
        return False
            
    def agregarCliente(self,cliente):
        if(self.clientes.extraerid(cliente.id) == False):
            self.clientes.insertar(cliente)
            self.clientes.crearReportec()
        else:
            return False
    def atenderCliente(self):
        if(self.clientes.primero != None):
            clienteatendido = self.clientes.extraer()
            clienteatendido.siguiente = None
            self.historialclientes.insertar(clienteatendido)
            self.clientes.crearReportec()
            return clienteatendido
        return None
    def tiempoclientest(self):
        cabezaclientes = self.clientes.cabeza()
        total = 0
        if(cabezaclientes != None):
            numclientes = self.clientes.getlen()
            for i in range(0,numclientes,1):
                total += cabezaclientes.tiempoTrans()
                cabezaclientes = cabezaclientes.siguiente
        return total
    def tiempopromedio(self):
        cabezaescritorio = self.escritorios.cabeza()
        promedio = 0
        if(cabezaescritorio != None):
            numescritorios = self.escritorios.getlen()
            total = 0
            contador = 0
            for i in range(0,numescritorios,1):
                tiempoe = cabezaescritorio.tiempoPromedio()
                if(tiempoe != None):
                    total += tiempoe
                    contador += 1
                cabezaescritorio = cabezaescritorio.siguiente
            promedio = total/contador
        return round(promedio,2)
    def tiempoesperapromedio(self):
        cabezacliente = self.historialclientes.cabeza()
        promedio = 0
        if cabezacliente.siguiente != None:
            ncliente = self.historialclientes.getlen()
            total = 0
            for i in range(0,ncliente-1,1):
                tiempoe = cabezacliente.tiempoTrans() + cabezacliente.siguiente.tiempoTrans()
                total += tiempoe
                cabezacliente = cabezacliente.siguiente
            promedio = total/(ncliente-1)
        return round(promedio,2)
    def tiempoesperamax(self):
        cabezacliente = self.historialclientes.cabeza()
        tmax = 0
        if cabezacliente != None:
            if cabezacliente.siguiente != None:
                ncliente = self.historialclientes.getlen()
                for i in range(0,ncliente-1,1):
                    cabeza2cliente = self.historialclientes.cabeza()
                    tmax = tiempoe = cabezacliente.tiempoTrans() + cabezacliente.siguiente.tiempoTrans()
                    for j in range(0,i or cabeza2cliente.siguiente != None,1):
                        tiempo1e = cabeza2cliente.tiempoTrans() + cabeza2cliente.siguiente.tiempoTrans()
                        if(tiempoe > tiempo1e):
                            tmax = tiempoe
                        elif(tiempo1e > tiempoe):
                            tmax = tiempo1e
                        cabeza2cliente = cabeza2cliente.siguiente
                    cabezacliente = cabezacliente.siguiente
        return tmax
    def tiempoesperamin(self):
        cabezacliente = self.historialclientes.cabeza()
        tmin = 0
        if cabezacliente != None:
            if cabezacliente.siguiente != None:
                ncliente = self.historialclientes.getlen()
                for i in range(0,ncliente-1,1):
                    cabeza2cliente = self.historialclientes.cabeza()
                    tmin = tiempoe = cabezacliente.tiempoTrans() + cabezacliente.siguiente.tiempoTrans()
                    for j in range(0,i or cabeza2cliente.siguiente != None,1):
                        tiempo1e = cabeza2cliente.tiempoTrans() + cabeza2cliente.siguiente.tiempoTrans()
                        if(tiempoe < tiempo1e):
                            tmin = tiempoe
                        elif(tiempo1e < tiempoe):
                            tmin = tiempo1e
                        cabeza2cliente = cabeza2cliente.siguiente
                    cabezacliente = cabezacliente.siguiente
        return tmin
    def tiempoatencionmax(self):
        cabezacliente = self.historialclientes.cabeza()
        tmax = 0
        if cabezacliente != None:
            ncliente = self.historialclientes.getlen()
            for i in range(0,ncliente,1):
                cabeza2cliente = self.historialclientes.cabeza()
                tmax = tiempoe = cabezacliente.tiempoTrans() 
                for j in range(0,i,1):
                    tiempo1e = cabeza2cliente.tiempoTrans() 
                    if(tiempoe > tiempo1e):
                        tmax = tiempoe
                    elif(tiempo1e > tiempoe):
                        tmax = tiempo1e
                    cabeza2cliente = cabeza2cliente.siguiente
                cabezacliente = cabezacliente.siguiente
        return tmax
    def tiempoatencionmin(self):
        cabezacliente = self.historialclientes.cabeza()
        tmin = 0
        if cabezacliente != None:
            ncliente = self.historialclientes.getlen()
            for i in range(0,ncliente,1):
                cabeza2cliente = self.historialclientes.cabeza()
                tmin = tiempoe = cabezacliente.tiempoTrans() 
                for j in range(0,i,1):
                    tiempo1e = cabeza2cliente.tiempoTrans() 
                    if(tiempoe < tiempo1e):
                        tmin = tiempoe
                    elif(tiempo1e < tiempoe):
                        tmin = tiempo1e
                    cabeza2cliente = cabeza2cliente.siguiente
                cabezacliente = cabezacliente.siguiente
        return tmin
        
from Cola import Cola


class Escritorio:
    def __init__(self, id, identificacionEscritorio, nombreEncargado, estado):
        self.id = id
        self.identificacionEscritorio = identificacionEscritorio
        self.nombreEncargado = nombreEncargado
        self.estado = estado
        self.clientesatendidos = Cola()
        self.ocupado = False
        self.siguiente = None

    def asignarCliente(self, cliente):
        if(self.clientesatendidos.extraerid(cliente.id) == False):
            self.clientesatendidos.insertar(cliente)

    def tiempoPromedio(self):
        cabezaclientes = self.clientesatendidos.cabeza()
        if(cabezaclientes != None):
            clientetotal = self.clientesatendidos.getlen()
            ttotal = 0
            for i in range(0, clientetotal, 1):
                ttotal += cabezaclientes.tiempoTrans()
                cabezaclientes = cabezaclientes.siguiente
            promedio = ttotal/clientetotal
            return round(promedio,2)
        else:
            return 0

    def tiempomax(self):
        cabezacliente = self.clientesatendidos.cabeza()
        tmax = 0
        if cabezacliente != None:
            ncliente = self.clientesatendidos.getlen()
            for i in range(0, ncliente, 1):
                cabeza2cliente = self.clientesatendidos.cabeza()
                tmax = tiempoe = cabezacliente.tiempoTrans()
                for j in range(0, i, 1):
                    tiempo1e = cabeza2cliente.tiempoTrans()
                    if(tiempoe > tiempo1e):
                        tmax = tiempoe
                    elif(tiempo1e > tiempoe):
                        tmax = tiempo1e
                    cabeza2cliente = cabeza2cliente.siguiente
                cabezacliente = cabezacliente.siguiente
        return tmax
    def tiempomin(self):
        cabezacliente = self.clientesatendidos.cabeza()
        tmin = 0
        if cabezacliente != None:
            ncliente = self.clientesatendidos.getlen()
            for i in range(0, ncliente, 1):
                cabeza2cliente = self.clientesatendidos.cabeza()
                tmin = tiempoe = cabezacliente.tiempoTrans()
                for j in range(0, i, 1):
                    tiempo1e = cabeza2cliente.tiempoTrans()
                    if(tiempoe < tiempo1e):
                        tmin = tiempoe
                    elif(tiempo1e < tiempoe):
                        tmin = tiempo1e
                    cabeza2cliente = cabeza2cliente.siguiente
                cabezacliente = cabezacliente.siguiente
        return tmin

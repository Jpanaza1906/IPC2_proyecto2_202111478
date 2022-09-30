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
            for i in range(0,clientetotal,1):
                ttotal += cabezaclientes.tiempoTrans()
                cabezaclientes = cabezaclientes.siguiente
            promedio = ttotal/clientetotal
            return promedio
        else:
            return None
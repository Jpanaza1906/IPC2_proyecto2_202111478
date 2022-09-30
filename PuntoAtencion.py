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
    def activarEscritorio(self, escritorio):
        self.escritoriosactivos.insertar(escritorio)
    def desactivarEscritorio(self):
        escritorio = self.escritoriosactivos.extraer()
        if(escritorio != None):
            escritoriofdesactivar = self.escritorios.extraerid(escritorio.id)
            escritoriofdesactivar.estado = False
            return True
        return False
            
    def agregarCliente(self,cliente):
        if(self.clientes.extraerid(cliente.id) == False):
            self.clientes.insertar(cliente)
        else:
            return False
    def atenderCliente(self):
        if(self.clientes.primero != None):
            clienteatendido = self.clientes.extraer()
            clienteatendido.siguiente = None
            self.historialclientes.insertar(clienteatendido)
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
            promedio = total/contador
        return promedio
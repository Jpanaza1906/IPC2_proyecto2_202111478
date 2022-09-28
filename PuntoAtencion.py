from Cola import Cola
class PuntoAtencion:
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.siguiente = None
        self.escritorios = Cola()
        self.escritoriosactivos = Cola()
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
            
    def agregarCliente(self,cliente):
        if(self.clientes.extraerid(cliente.id) == False):
            self.clientes.insertar(cliente)
        else:
            return False
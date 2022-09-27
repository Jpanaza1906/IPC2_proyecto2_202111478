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
        self.escritorios.insertar(escritorio)
    def activarEscritorio(self, id):
        escritoriofactivar = self.escritorios.extraerid(id)
        if(escritoriofactivar != None):
            self.escritoriosactivos.insertar(escritoriofactivar)
        else:
            return False
    def agregarCliente(self,cliente):
        self.clientes.insertar(cliente)
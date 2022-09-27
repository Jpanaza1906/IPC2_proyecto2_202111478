from Cola import Cola
escritorios = Cola()
escritoriosactivos = Cola()
clientes = Cola()
class PuntoAtencion:
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.siguiente = None
    def agregarEscritorio(escritorio):
        escritorios.insertar(escritorio)
    def activarEscritorio(id):
        escritoriofactivar = escritorios.extraerid(id)
        if(escritoriofactivar != None):
            escritoriosactivos.insertar(escritoriofactivar)
        else:
            return False
    def agregarCliente(cliente):
        clientes.insertar(cliente)
from Cola import Cola
class Empresa:
    def __init__(self, id, nombre, abreviatura):
        self.id = id
        self.nombre = nombre
        self.abreviatura = abreviatura
        self.siguiente = None
        self.puntosatencion = Cola()
        self.transacciones = Cola()
    def agregarPuntos(self, puntoatencion):
        if (self.puntosatencion.extraerid(puntoatencion.id) == False):
            self.puntosatencion.insertar(puntoatencion)
        else:
            return False
    def agregarTransaccion(self, transaccion):
        if (self.transacciones.extraerid(transaccion.id) == False):
            self.transacciones.insertar(transaccion)
        else:
            return False
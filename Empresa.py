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
        self.puntosatencion.insertar(puntoatencion)
    def agregarTransaccion(self, transaccion):
        self.transacciones.insertar(transaccion)
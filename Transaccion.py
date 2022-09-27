class Transaccion:
    def __init__(self, id, nombre, minutos, cantidad):
        self.id = id
        self.nombre = nombre
        self.minutos = minutos
        self.cantidad = cantidad
        self.siguiente = None        
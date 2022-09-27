from Cola import Cola
from Empresa import transacciones
transaccionespendientes = Cola()
class Cliente:
    def __init__(self, dpi, nombre):
        self.dpi = dpi
        self.nombre = nombre
        self.siguiente = None
    def agregarTransaccion(id, cantidad):
        temptrans = transacciones.extraerid(id)
        if(temptrans != None):
            temptrans.cantidad = cantidad
            transaccionespendientes.insertar(temptrans)
        else:
            return False
            
        
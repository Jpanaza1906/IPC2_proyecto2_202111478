import copy
from Cola import Cola
from Transaccion import Transaccion
class Cliente:
    def __init__(self, dpi, nombre):
        self.id = dpi
        self.nombre = nombre
        self.transaccionespendiente = Cola()
        self.siguiente = None
    def agregarTransaccion(self, id, cantidad,empresa):
        temptrans = copy.deepcopy(empresa.transacciones.extraerid(id))
        if(temptrans != False):
            temptrans.cantidad = cantidad
            temptrans.siguiente = None
            self.transaccionespendiente.insertar(temptrans)
        else:
            return False
            
        
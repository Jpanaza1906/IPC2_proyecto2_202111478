import copy
from Cola import Cola
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
    def tiempoTrans(self):
        cabezatrans = self.transaccionespendiente.cabeza()
        if(cabezatrans != None):
            numtrans = self.transaccionespendiente.getlen()
            total = 0
            for i in range(0,numtrans,1):
                total += (int(cabezatrans.minutos)*int(cabezatrans.cantidad))
                cabezatrans = cabezatrans.siguiente
            return total
        else:
            return None
        
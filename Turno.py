class Turno:
    def __init__(self, id,idpunto, cliente, escritorio):
        self.id = id
        self.idpunto = idpunto
        self.cliente = cliente
        self.escritorio = escritorio
        self.siguiente = None
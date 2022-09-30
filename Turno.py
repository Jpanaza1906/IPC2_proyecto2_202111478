class Turno:
    def __init__(self, id, cliente, escritorio):
        self.id = id
        self.cliente = cliente
        self.escritorio = escritorio
        self.siguiente = None
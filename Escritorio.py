class Escritorio:
    def __init__(self, id, identificacionEscritorio, nombreEncargado, estado):
        self.id = id
        self.identificacionEscritorio = identificacionEscritorio
        self.nombreEncargado = nombreEncargado
        self.estado = estado
        self.siguiente = None
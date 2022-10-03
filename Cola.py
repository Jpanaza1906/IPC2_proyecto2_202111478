from rich.console import Console
import os
class Cola:
    def __init__(self):
        self.primero = None
        self.contador = 0
    def estaVacia(self):
        if self.primero == None:
            return True
        else:
            return False
    def insertar(self,item):
        if self.estaVacia():
            self.primero = item
        else:
            temp = self.primero
            while(temp.siguiente != None):
                temp = temp.siguiente
            temp.siguiente = item
    def cabeza(self):
        return self.primero
    def extraerid(self, id):
        if self.primero != None:
            temp = self.primero
            if temp.id == id:
                return temp
            while temp.siguiente != None:                
                temp = temp.siguiente
                if temp.id == id:
                    return temp
        return False
    def extraer(self):
        temp = self.primero
        if self.primero != None:
            self.primero = self.primero.siguiente            
            return temp
            del temp
        else:
            print("No hay items pendientes.")
    def getlen(self):
        cont = 1
        if self.primero != None:
            temp = self.primero
            while temp.siguiente != None:
                cont += 1
                temp = temp.siguiente
            return cont
        else:
            return 0 
    
    def reporte(self):
        aux = self.primero
        text = ""
        text += "rankdir=LB; \n node[shape=egg, style = filled, color=khaki, fontname=\"Century Gothic\"];"
        text += "labelloc = \"t;\" label = \" Escritorios activos\" ; \n"
        while aux:
            text += "x" + str(aux.id) + "[dir=both label=\"id = " + str(aux.id) + "\\n nombre = " + aux.nombreEncargado + "\\n tipo = " + str(aux.identificacionEscritorio) + "\"]"
            if(aux.siguiente != None):
                text += "x" + str(aux.id) + "-> x" + str(aux.siguiente.id) + "\n"
                aux = aux.siguiente
            if(aux != self.primero):
                text += "x" + str(aux.id) + "[dir=both label=\"id = " + str(aux.id) + "\\n nombre = " + aux.nombreEncargado + "\\n tipo = " + str(aux.identificacionEscritorio) + "\"]"                
            else:
                break
            if(aux.siguiente == None):                
                break
        return text
    def reportec(self):
        aux = self.primero
        text = ""
        text += "rankdir=LB; \n node[shape=egg, style = filled, color=khaki, fontname=\"Century Gothic\"];"
        text += "labelloc = \"t;\" label = \" Clientes en cola\" ; \n"
        while aux:
            text += "x" + str(aux.id) + "[dir=both label=\"id = " + str(aux.id) + "\\n nombre = " + aux.nombre + "\\n tiempo = " + str(aux.tiempoTrans()) +" min" + "\"]"
            if(aux.siguiente != None):
                text += "x" + str(aux.id) + "-> x" + str(aux.siguiente.id) + "\n"
                aux = aux.siguiente
            if(aux != self.primero):
                text += "x" + str(aux.id) + "[dir=both label=\"id = " + str(aux.id) + "\\n nombre = " + aux.nombre + "\\n tiempo = " + str(aux.tiempoTrans()) +" min"  + "\"]"                
            else:
                break
            if(aux.siguiente == None):                
                break
        return text
    def crearReporte(self, npunto):
        self.contador += 1
        contenido = "digraph G{\n\n"
        r = open("reporte"+ npunto +".txt", "w")
        contenido += str(self.reporte())
        contenido += "\n}"
        r.write(contenido)
        r.close()
        os.system("dot -Tpng reporte"+ npunto +".txt -o reporte"+ npunto + str(self.contador) +".png")
        os.system("dot -Tpdf reporte"+ npunto +".txt -o reporte"+ npunto + str(self.contador) +".pdf")
    def crearReportec(self,npunto):
        self.contador += 1
        contenido = "digraph G{\n\n"
        r = open("reporte"+ npunto +".txt", "w")
        contenido += str(self.reportec())
        contenido += "\n}"
        r.write(contenido)
        r.close()
        os.system("dot -Tpng reporte"+ npunto +".txt -o reporte"+ npunto + str(self.contador) +".png")
        os.system("dot -Tpdf reporte"+ npunto +".txt -o reporte"+ npunto + str(self.contador) +".pdf")
   
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
    def extraerid(self, id):
        if self.primero != None:
            temp = self.primero
            while temp.siguiente != None:
                if temp.id == id:
                    return temp
                temp = temp.siguiente
        pass
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
        pass
    """def get_tiempoespera(self):
        temp = self.primero
        tiempot = temp.tiempo
        while(temp.siguiente != None):            
            temp = temp.siguiente
            tiempot += temp.tiempo
        return str(tiempot)
    def get_ordenespendientes(self):
        c = Console()
        temp = self.primero
        if self.primero != None:
            c.print("[bold]|[cyan]Nombre[/]|[green]Descripcion[/]|[white]Tiempo|[/][/]")
            c.print("[cyan]" + temp.nombre + " [/]" + "[green]" + temp.descripcion + " [/]" + "[white]" + str(temp.tiempo) + " min[/]")
            while temp.siguiente != None:
                temp = temp.siguiente
                c.print("[cyan]" + temp.nombre + " [/]" + "[green]" + temp.descripcion + " [/]" + "[white]" + str(temp.tiempo) + " min[/]")
        else:
            c.print("No hay ordenes pendientes", style="red on white")
    def report(self):
        aux = self.primero
        text = ""
        text += "rankdir=LB; \n node[shape=egg, style = filled, color=khaki, fontname=\"Century Gothic\"];"
        text += "labelloc = \"t;\" label = \" Compras\" ; \n"
        while aux:
            text += "x" + str(aux.nombre) + "[dir=both label=\"Nombre = " + str(aux.nombre) + "\\n Descripcion = " + aux.descripcion + "\\n Tiempo = " + str(aux.tiempo) + "\"]"
            if(aux.siguiente != None):
                text += "x" + str(aux.nombre) + "-> x" + str(aux.siguiente.nombre) + "\n"
                aux = aux.siguiente
            if(aux != self.primero):
                text += "x" + str(aux.nombre) + "[dir=both label=\"Nombre = " + str(aux.nombre) + "\\n Descripcion = " + aux.descripcion + "\\n Tiempo = " + str(aux.tiempo) + "\"]"                
            else:
                break
            if(aux.siguiente == None):                
                break
        return text
    def crearReporte(self):
        self.contador += 1
        contenido = "digraph G{\n\n"
        r = open("reporte.txt", "w")
        contenido += str(self.report())
        contenido += "\n}"
        r.write(contenido)
        r.close()
        os.system("dot -Tpng reporte.txt -o reporte"+ str(self.contador) +".png")
        os.system("dot -Tpdf reporte.txt -o reporte"+ str(self.contador) +".pdf")
    """
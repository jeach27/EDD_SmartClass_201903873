class nodo:
    def __init__(self,data):
        self.data = data
        self.siguiente = None
        self.anterior = None

class listaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacia(self):
        return self.primero == None

    def insertar(self,dato):
        if self.vacia():
            self.primero = self.ultimo = nodo(dato)
            self.size += 1
            return
        temp = self.ultimo
        self.ultimo = temp.siguiente = nodo(dato)
        self.ultimo.anterior = temp
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero
        self.size += 1
    
    def eliminar(self, nodo):
        anterior = nodo.anterior
        anterior.siguiente = nodo.siguiente
        nodo.siguiente.anterior = anterior
        
    def imprimir(self):
        aux = self.primero
        while aux != self.ultimo:
            print(aux.data)
            aux = aux.siguiente
        print(self.ultimo.data)
        

#lista = listaDoble()
#lista.insertar(1)
#lista.imprimir()


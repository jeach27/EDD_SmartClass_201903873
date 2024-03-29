class Nodo:
    def __init__(self,id,dato):
        self.id = id
        self.dato = dato
        self.data = None
        self.izq = None
        self.der = None

class AVL:
    def __init__(self):
        self.raiz = None
        self.altura = -1
        self.equilibrio = 0

    def insertar(self,_id,_nombre):
        nuevo = Nodo(_id,_nombre)
        if self.raiz == None:
            self.raiz = nuevo
            self.raiz.izq = AVL()
            self.raiz.der = AVL()
        elif _id > self.raiz.id:
            self.raiz.der.insertar(_id,_nombre)
        elif _id < self.raiz.id:
            self.raiz.izq.insertar(_id,_nombre)
        else: #YA EXISTE
            print("el valor ya existe")
        self.balancear()

    def balancear(self):
        self.actualizarAlturas(recursivo = False)
        self.actualizarEquilibrio(False)
        while self.equilibrio < -1 or self.equilibrio > 1:
            if self.equilibrio > 1:
                if self.raiz.izq.equilibrio < 0:
                    self.raiz.izq.rotacionziquierda()
                    self.actualizarAlturas()
                    self.actualizarEquilibrio()
                self.rotacionDerecha()
                self.actualizarAlturas()
                self.actualizarEquilibrio()
            if self.equilibrio < -1:
                if self.raiz.der.equilibrio > 0:
                    self.raiz.der.rotacionDerecha()
                    self.actualizarAlturas()
                    self.actualizarEquilibrio()
                self.rotacionziquierda()
                self.actualizarAlturas()
                self.actualizarEquilibrio()


    def actualizarAlturas(self, recursivo =  True):
        if self.raiz == None:
            self.altura = -1
        else:
            if recursivo:
                if self.raiz.izq != None:
                    self.raiz.izq.actualizarAlturas()
                if self.raiz.der != None:
                    self.raiz.der.actualizarAlturas()
            self.altura = max(self.raiz.izq.altura, self.raiz.der.altura) + 1

    def actualizarEquilibrio(self, recursivo = True):
        if self.raiz == None:
            self.equilibrio = 0
        else:
            if recursivo:
                if self.raiz.izq != None:
                    self.raiz.izq.actualizarEquilibrio()
                if self.raiz.der != None:
                    self.raiz.der.actualizarEquilibrio()
            self.equilibrio = self.raiz.izq.altura - self.raiz.der.altura

    def rotacionDerecha(self):
        raiz = self.raiz
        self.raiz = raiz.izq.raiz
        raiz.izq.raiz = self.raiz.der.raiz
        self.raiz.der.raiz = raiz

    def rotacionziquierda(self):
        raiz = self.raiz
        self.raiz = raiz.der.raiz
        raiz.der.raiz = self.raiz.izq.raiz
        self.raiz.izq.raiz = raiz

    def enOrden(self):
        arr = []
        self.enOrden2(self.raiz,arr)
        return arr

    def enOrden2(self, raizActual,arr):
        if raizActual:
            self.enOrden2(raizActual.izq.raiz , arr )
            # print(raizActual.id)
            arr.append(
                {
                    "id":raizActual.id,
                    "DPI":raizActual.dato.DPI
                }
            )
            self.enOrden2(raizActual.der.raiz , arr )
    
    def Orden(self,buscado):
        return self.Orden2(self.raiz,buscado)

    def Orden2(self,raizActual,buscado):
        if raizActual:
            self.Orden2(raizActual.izq.raiz , buscado)
            if raizActual.id == buscado:
                return raizActual
            self.Orden2(raizActual.der.raiz,buscado)
        return None 
        
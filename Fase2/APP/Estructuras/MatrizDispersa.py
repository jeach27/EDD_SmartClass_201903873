class Nodo:
    def __init__(self, x, y, codigo):
        self.x = x
        self.y = y
        self.codigo = codigo
        self.arriba = None
        self.abajo = None
        self.derecha = None
        self.izquierda = None

class Matriz:
    def __init__(self, nombre):
        self.raiz = Nodo(-1,-1,nombre)
        self.columnas = 0
        self.filas = 0

    def insertar(self,x,y,codigo):
        nuevo = Nodo(x,y,codigo)

        columna = self.buscarColumna(x)
        fila = self.buscarFila(y)

        if columna == None and fila == None:
            columna = self.crearColumna(x)
            fila = self.crearFila(y)    

            nuevo = self.insertarOrdenColumna(fila, nuevo)
            nuevo = self.insertarOrdenFila(columna,nuevo)

        elif columna == None and fila != None:
            columna = self.crearColumna(x)

            nuevo = self.insertarOrdenColumna(fila, nuevo)
            nuevo = self.insertarOrdenFila(columna,nuevo)

        elif columna != None and fila == None:
            fila = self.crearFila(y)

            nuevo = self.insertarOrdenColumna(fila, nuevo)
            nuevo = self.insertarOrdenFila(columna,nuevo)

        elif columna != None and fila != None:
            nuevo = self.insertarOrdenColumna(fila, nuevo)
            nuevo = self.insertarOrdenFila(columna,nuevo)

    def verificarNodo(self,x,y):
        pass

    def verificarNodo2(self,x,y):
        pass

    def buscarColumna(self,x):
        aux = self.raiz
        while aux != None:
            if aux.x == x:
                return aux
            aux = aux.derecha
        return None

    def buscarFila(self,y):
        aux = self.raiz
        while aux != None:
            if aux.y == y:
                return aux
            aux = aux.abajo
        return None

    def crearColumna(self,x):
        cabeceraC = self.raiz
        nuevo = Nodo(x,-1,str(x))
        columna = self.insertarOrdenColumna(cabeceraC,nuevo)
        self.columnas += 1
        return columna

    def crearFila(self,y):
        cabeceraF = self.raiz
        nuevo = Nodo(-1,y, str(y))
        fila = self.insertarOrdenFila(cabeceraF,nuevo)
        self.filas += 1
        return fila

    def insertarOrdenColumna(self,cabecera,nuevo):
        aux = cabecera
        flag = False

        while True:
            if aux.x > nuevo.x:
                flag = True
                break
            if aux.derecha != None:
                aux = aux.derecha
            else:
                break

        if flag:
            nuevo.derecha = aux
            aux.izquierda.derecha = nuevo
            nuevo.izquierda = aux.izquierda
            aux.izquierda = nuevo
        else:
            aux.derecha = nuevo
            nuevo.izquierda = aux

        return nuevo

    def insertarOrdenFila(self,cabecera,nuevo):
        aux = cabecera
        flag = False

        while True:
            if aux.y > nuevo.y:
                flag = True
                break
            if aux.abajo != None:
                aux = aux.abajo
            else:
                break

        if flag:
            nuevo.abajo = aux
            aux.arriba.abajo = nuevo
            nuevo.arriba = aux.arriba
            aux.arriba = nuevo
        else:
            aux.abajo = nuevo
            nuevo.arriba = aux

        return nuevo

    def nodoH(self,nuevo):
        pass

    def nodoV(self,nuevo):
        pass


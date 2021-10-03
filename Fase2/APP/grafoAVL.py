import os

class Grafo:
    def __init__(self):
        pass

    def graficarArbol(self, raiz):
        acumuladores = ["digraph G{\nnode [shape=Mrecord];\n", ""]

        if raiz != None:
            self.recorrerArbol(raiz,acumuladores)

        acumuladores[0] += acumuladores[1] + "\n}"

        f = open('grafo.dot', 'w')
        try:
            f.write(acumuladores[0])
        finally:
            f.close()

        prog = "dot -Tpng  grafo.dot -o grafo.png"
        os.system(prog)


    def recorrerArbol(self, raiz,acum):

        if raiz:
            label = '{'+str(raiz.id)+' | '+str(raiz.dato.nombre)+' | '+str(raiz.dato.carrera)+'}'
            acum[1] += '"{}"[label="{}"];\n'.format(str(hash(raiz)),label)

            if raiz.izq.raiz != None:
                acum[1] += '"{}" -> "{}";\n'.format(str(hash(raiz)),str(hash(raiz.izq.raiz)))
            if raiz.der.raiz != None:
                acum[1] += '"{}" -> "{}";\n'.format(str(hash(raiz)), str(hash(raiz.der.raiz)))

            self.recorrerArbol(raiz.izq.raiz, acum)
            self.recorrerArbol(raiz.der.raiz, acum)
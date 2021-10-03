import os
from Estructuras import ListaDoble as LD
from Estructuras import Tareas as ta

def grafoArbolB(ArbolB):
    pass

def grafoMatriz(Matriz):
    file = open('grafoR.dot','w')
    file.write('digraph G{\n')

    file.write('graph [pad="0.5", nodesep="0.5", ranksep="2"];\n  node [shape=plain]\n  rankdir=LR; \nFoo [label=< \n<table border="0" cellborder="1" cellspacing="0">\n')
    filas = []
    columnas = []  
    aux = Matriz.raiz  
    while aux:
        filas.append(aux.y)
        aux = aux.abajo 
    aux = Matriz.raiz
    while aux:
        columnas.append(aux.x)
        aux = aux.derecha

    for i in filas:
        aux = Matriz.buscarFila(i)
        if aux != None:
            file.write('<tr>\n')    
            for j in columnas:
                if aux.x == j and aux.y == i:
                    file.write('<td>'+aux.codigo+'</td>\n')
                    if aux.derecha != None:
                        aux = aux.derecha
                else:
                    file.write('<td>'+' '+'</td>\n')
            file.write('</tr>\n')

    file.write('</table>>];\n')
        
    file.write('}')
    file.close() 
    os.system('dot -Tpng grafoR.dot -o grafoR.png')
    os.startfile('grafoR.png')

def grafoLista(Lista):
    file = open('Agenda.dot','w')
    file.write('digraph G{\n')
    file.write('rankdir="LR";\n')
    #file.write('Label[label="LISTA"]\n')
    aux = Lista.primero
    while aux != Lista.ultimo:
        file.write(str(aux)+'[label="{{ Carne: '+str(aux.data.carne)+' | Nombre: '+str(aux.data.nombre)+' | Descripcion: '+str(aux.data.descripcion)+' | Materia: '+str(aux.data.materia)+' | Fecha: '+str(aux.data.fecha)+' | Hora: '+str(aux.data.hora)+' | Estado: '+str(aux.data.estado)+' }}",shape=Mrecord]\n')
        aux = aux.siguiente
    file.write(str(aux)+'[label="{{ Carne: '+str(aux.data.carne)+' | Nombre: '+str(aux.data.nombre)+' | Descripcion: '+str(aux.data.descripcion)+' | Materia: '+str(aux.data.materia)+' | Fecha: '+str(aux.data.fecha)+' | Hora: '+str(aux.data.hora)+' | Estado: '+str(aux.data.estado)+' }}",shape=Mrecord]\n')

    aux = Lista.primero
    while aux != Lista.ultimo:
        if aux.siguiente != Lista.primero:
            file.write(str(aux)+'->'+str(aux.siguiente)+'\n')
            file.write(str(aux.siguiente)+'->'+str(aux)+'\n')
        aux = aux.siguiente
    #file.write(str(aux)+'->'+str(aux.siguiente)+'\n')
    #file.write(str(aux.siguiente)+'->'+str(aux)+'\n')
        
        
    file.write('}')
    file.close()
    os.system('dot -Tpng Agenda.dot -o Agenda.png')
    os.startfile('Agenda.png')    

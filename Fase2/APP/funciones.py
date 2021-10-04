from sys import _debugmallocstats
from flask.app import setupmethod
import Estructuras.MatrizDispersa as MAT
import Estructuras.ArbolAVL as AVL
import Estructuras.Estudiantes as est
import Estructuras.ListaDoble as LD
import Estructuras.Años as YR
import Estructuras.Meses as MS
import Estructuras.Tareas as TR
from gramatica import parser, user_list , task_list
import grafoAVL as graf
import grafos as gr

aEstudiantes = AVL.AVL()
grafo = graf.Grafo()

def buscarLDY(lista, buscado):
    aux = lista.primero
    while aux != lista.ultimo:
        if aux.data.año == buscado:
            return aux.data
        else:
            aux = aux.siguiente
    if lista.ultimo.data.año == buscado:
        return lista.ultimo.data
    else:
        return False

def buscarLDM(lista, buscado):
    aux = lista.primero
    while aux != lista.ultimo:
        if aux.data.mes == buscado:
            return aux.data
        else:
            aux = aux.siguiente
    if lista.ultimo.data.mes == buscado:
        return lista.ultimo.data    
    else:
        return False

def buscarLDR(lista, buscado):
    aux = lista.primero
    while aux != lista.ultimo:
        if aux.data.posicion == buscado:
            return aux.data
        else:
            aux = aux.siguiente
    if lista.ultimo.data.posicion == buscado:
        return lista.ultimo.data    
    else:
        return False

def cargaMasivaEstudiantes(ruta):
    f = open(ruta, "r", encoding="utf-8")
    input = f.read()
    #print(input)
    parser.parse(input)
    aux = user_list.First
    while aux is not None:
        carne = aux.Carnet
        #print(aux.Nombre)
        listaA = LD.listaDoble()
        estudiante = est.estudiante(aux.Carnet,aux.DPI,aux.Nombre,aux.Carrera,aux.Correo,aux.Password,aux.Creditos,aux.Edad,listaA)
        aEstudiantes.insertar(carne,estudiante)
        aux = aux.Next
    #grafo.graficarArbol(aEstudiantes.raiz)
    return "Carga Masiva Estudiantes Exitosa"

def cargaMasivaRecordatorio(ruta):
    f = open(ruta, "r", encoding="utf-8")
    input = f.read()
    #print(input)
    parser.parse(input)   
    aux = task_list.First
    while aux is not None:
        carne = aux.Carnet
        fecha = aux.Fecha
        dia = fecha[0]+fecha[1]
        mes = fecha[3]+fecha[4]
        year = fecha[6]+fecha[7]+fecha[8]+fecha[9]
        hora = aux.Hora
        if hora[1] == ":":
            hora = hora[0]
        else:
            hora = hora[0] + hora[1]
        encontrado = aEstudiantes.Orden(carne)
        if encontrado != None:
            yearBuscado = buscarLDY(encontrado.dato.year,year)
            if yearBuscado != False:
                mesBuscado = buscarLDM(yearBuscado.meses,mes)
                if mesBuscado != False:
                    verificarMM = mesBuscado.tareas.verificarNodo(int(dia),int(hora))
                    if verificarMM != False:
                        verificarMM.insertar(TR.tarea(aux.Carnet,aux.Nombre,aux.Descripcion,aux.Materia,aux.Fecha,aux.Hora,aux.Estado))
                    else:
                        tr = LD.listaDoble
                        tr.insertar(TR.tarea(aux.Carnet,aux.Nombre,aux.Descripcion,aux.Materia,aux.Fecha,aux.Hora,aux.Estado))
                        mesBuscado.tareas.insertar(int(dia),int(hora),tr)
                else:
                    tareas = MAT.Matriz(str(mes))
                    verificarM = tareas.verificarNodo(int(dia),int(hora))
                    if verificarM != False:
                        verificarM.insertar(TR.tarea(aux.Carnet,aux.Nombre,aux.Descripcion,aux.Materia,aux.Fecha,aux.Hora,aux.Estado))
                    else:
                        tr = LD.listaDoble()
                        tr.insertar(TR.tarea(aux.Carnet,aux.Nombre,aux.Descripcion,aux.Materia,aux.Fecha,aux.Hora,aux.Estado))
                        tareas.insertar(int(dia),int(hora),tr)
                    yearBuscado.meses.insertar(MS.meses(mes,tareas))
            else:
                sem = LD.listaDoble()
                mese = LD.listaDoble()
                tareas = MAT.Matriz(str(mes))
                verificarM = tareas.verificarNodo(int(dia),int(hora))
                if verificarM != False:
                    verificarM.insertar(TR.tarea(aux.Carnet,aux.Nombre,aux.Descripcion,aux.Materia,aux.Fecha,aux.Hora,aux.Estado))
                else:
                    tr = LD.listaDoble()
                    tr.insertar(TR.tarea(aux.Carnet,aux.Nombre,aux.Descripcion,aux.Materia,aux.Fecha,aux.Hora,aux.Estado))
                    tareas.insertar(int(dia),int(hora),tr)
                mese.insertar(MS.meses(mes,tareas))
                years = YR.año(year,sem,mese)
                encontrado.dato.year.insertar(years)
        aux = aux.Next
    return "Carga Masiva Recordatorio"

def reporteAVL():
    grafo.graficarArbol(aEstudiantes.raiz)
    return "Grafo de AVL de estudiantes generado"

def reporteLD(carne,year,mes,dia,hora):
    hor = hora
    if hor[1] == ":":
        hor = hor[0]
    else:
        hor = hor[0] + hor[1]
    encontrado = aEstudiantes.Orden(carne)
    if encontrado != None:
        yearBuscado = buscarLDY(encontrado.dato.year,year)
        if yearBuscado != False:
            mesBuscado = buscarLDM(yearBuscado.meses,mes)
            if mesBuscado != False:
                verificarMM = mesBuscado.tareas.verificarNodo(int(dia),int(hor))
                if verificarMM != False:
                    gr.grafoLista(verificarMM)
                    return "Grafo de Lista de Tareas generado"
                return "No se encontro la lista de Recordatorio"
            return "No se encontro el mes"
        return "No se encontro ese año"
    return "No se encontro el estudiante"

def reporteM(carne,year,mes):
    encontrado = aEstudiantes.Orden(carne)
    if encontrado != None:
        yearBuscado = buscarLDY(encontrado.dato.year,year)
        if yearBuscado != False:
            mesBuscado = buscarLDM(yearBuscado.meses,mes)
            if mesBuscado != False:
                gr.grafoMatriz(mesBuscado.tareas)
                return "Grado de Matriz generado"
            return "No se encontro el mes"
        return "No se encontro ese año"
    return "No se encontro el estudiante"

def crearEstudiante(carne,dpi,Nombre,carrera,correo,password,creditos,edad):
    listaA = LD.listaDoble()
    estudiante = est.estudiante(carne,dpi,Nombre,carrera,correo,password,creditos,edad,listaA)
    aEstudiantes.insertar(carne,estudiante)
    return "El estudiante ha sido ingresado exitosamente"
 
def modificarEstudiante(carne,dpi,nombre,carrera,correo,contra,creditos,edad):
    encontrado = aEstudiantes.Orden(carne)
    if encontrado != None:
        encontrado.dato.carne = carne
        encontrado.dato.DPI = dpi
        encontrado.dato.nombre = nombre
        encontrado.dato.carrera = carrera
        encontrado.dato.correo = correo
        encontrado.dato.contra = contra
        encontrado.dato.creditos = creditos
        encontrado.dato.edad = edad
        return "El estudiante ha sido modificado exitosamente"
    return "No se encontro el estudiante"
    
def eliminarEstudiante():
    pass
    
def obtenerEstudiante(carne):
    datos = []
    encontrado = aEstudiantes.Orden(carne)
    if encontrado != None:
        datos.append(
            {
                "carnet": encontrado.dato.carne,
                "DPI": encontrado.dato.DPI,
                "nombre": encontrado.dato.nombre,
                "carrera": encontrado.dato.carrera,
                "correo": encontrado.dato.correo,
                "password": encontrado.dato.contra,
                "creditos": encontrado.dato.creditos,
                "edad": encontrado.dato.edad

            }
        )
        return datos
    datos.append(
        {
            "mensaje": "Estudiante no encontrado"
        }
    )
    return datos
    
def crearRecordatorio(carne,nombre,descripcion,materia,fecha,hora,estado):
    dia = fecha[0]+fecha[1]
    mes = fecha[3]+fecha[4]
    year = fecha[6]+fecha[7]+fecha[8]+fecha[9]
    hor = hora
    if hor[1] == ":":
        hor = hor[0]
    else:
        hor = hor[0] + hor[1]
    encontrado = aEstudiantes.Orden(carne)
    if encontrado != None:
        yearBuscado = buscarLDY(encontrado.dato.year,year)
        if yearBuscado != False:
            mesBuscado = buscarLDM(yearBuscado.meses,mes)
            if mesBuscado != False:
                verificarMM = mesBuscado.tareas.verificarNodo(int(dia),int(hor))
                if verificarMM != False:
                    verificarMM.insertar(TR.tarea(carne,nombre,descripcion,materia,fecha,hora,estado))
                else:
                    tr = LD.listaDoble
                    tr.insertar(TR.tarea(carne,nombre,descripcion,materia,fecha,hora,estado))
                    mesBuscado.tareas.insertar(int(dia),int(hor),tr)
            else:
                tareas = MAT.Matriz(str(mes))
                verificarM = tareas.verificarNodo(int(dia),int(hor))
                if verificarM != False:
                    verificarM.insertar(TR.tarea(carne,nombre,descripcion,materia,fecha,hora,estado))
                else:
                    tr = LD.listaDoble()
                    tr.insertar(TR.tarea(carne,nombre,descripcion,materia,fecha,hora,estado))
                    tareas.insertar(int(dia),int(hor),tr)
                yearBuscado.meses.insertar(MS.meses(mes,tareas))
            return "Recordatorio creado"
        else:
            sem = LD.listaDoble()
            mese = LD.listaDoble()
            tareas = MAT.Matriz(str(mes))
            verificarM = tareas.verificarNodo(int(dia),int(hor))
            if verificarM != False:
                verificarM.insertar(TR.tarea(carne,nombre,descripcion,materia,fecha,hora,estado))
            else:
                tr = LD.listaDoble()
                tr.insertar(TR.tarea(carne,nombre,descripcion,materia,fecha,hora,estado))
                tareas.insertar(int(dia),int(hor),tr)
            mese.insertar(MS.meses(mes,tareas))
            years = YR.año(year,sem,mese)
            encontrado.dato.year.insertar(years)
        return "Recordatorio creado"
    return "No se encontro el estudiante"
    
def modificarRecordatorio(carne,nombre,descripcion,materia,fecha,hora,estado,posicion):
    dia = fecha[0]+fecha[1]
    mes = fecha[3]+fecha[4]
    year = fecha[6]+fecha[7]+fecha[8]+fecha[9]
    hor = hora
    if hor[1] == ":":
        hor = hor[0]
    else:
        hor = hor[0] + hor[1]
    encontrado = aEstudiantes.Orden(carne)
    if encontrado != None:
        yearBuscado = buscarLDY(encontrado.dato.year,year)
        if yearBuscado != False:
            mesBuscado = buscarLDM(yearBuscado.meses,mes)
            if mesBuscado != False:
                verificarMM = mesBuscado.tareas.verificarNodo(int(dia),int(hor))
                if verificarMM != False:
                    tar = TR.tarea(carne,nombre,descripcion,materia,fecha,hora,estado)
                    tar.posicion = posicion
                    verificarMM.insertar(tar)
                    return "Recordatorio Modificado"
                else:
                    tr = LD.listaDoble
                    tar = TR.tarea(carne,nombre,descripcion,materia,fecha,hora,estado)
                    tar.posicion = posicion
                    tr.insertar(tar)
                    mesBuscado.tareas.insertar(int(dia),int(hor),tr)
                    return "Recordatorio modificado"
            return "No se encontro el mes"
        return "No se encontro ese año"
    return "No se encontro el estudiante"
    
def eliminarRecordatorio(carne,fecha,hora,posicion):
    dia = fecha[0]+fecha[1]
    mes = fecha[3]+fecha[4]
    year = fecha[6]+fecha[7]+fecha[8]+fecha[9]
    hor = hora
    if hor[1] == ":":
        hor = hor[0]
    else:
        hor = hor[0] + hor[1]
    encontrado = aEstudiantes.Orden(carne)
    if encontrado != None:
        yearBuscado = buscarLDY(encontrado.dato.year,year)
        if yearBuscado != False:
            mesBuscado = buscarLDM(yearBuscado.meses,mes)
            if mesBuscado != False:
                verificarMM = mesBuscado.tareas.verificarNodo(int(dia),int(hor))
                if verificarMM != False:
                    verificarR = buscarLDR(verificarMM,posicion)
                    if verificarR != False:
                        verificarMM.eliminar(verificarR)
                        return "El recordatorio ha sido eliminado"
                    return "No se encontro el recordatorio"
                return "No se encontro la lista de recordatorios"
            return "No se encontro el mes"
        return "No se encontro ese año"
    return "No se encontro el estudiante"
    
def obtenerRecordatorio(carne,fecha,hora,posicion):
    dia = fecha[0]+fecha[1]
    mes = fecha[3]+fecha[4]
    year = fecha[6]+fecha[7]+fecha[8]+fecha[9]
    hor = hora
    if hor[1] == ":":
        hor = hor[0]
    else:
        hor = hor[0] + hor[1]
    encontrado = aEstudiantes.Orden(carne)
    if encontrado != None:
        yearBuscado = buscarLDY(encontrado.dato.year,year)
        if yearBuscado != False:
            mesBuscado = buscarLDM(yearBuscado.meses,mes)
            if mesBuscado != False:
                verificarMM = mesBuscado.tareas.verificarNodo(int(dia),int(hor))
                if verificarMM != False:
                    verificarR = buscarLDR(verificarMM,posicion)
                    if verificarR != False:
                        datos = []
                        datos.append({

                            "carne":verificarR.carne,
                            "nombre":verificarR.nombre,
                            "descripcion":verificarR.descripcion,
                            "materia":verificarR.materia,
                            "fecha":verificarR.fecha,
                            "hora":verificarR.hora,
                            "estado":verificarR.estado,
                            "posicion":verificarR.posicion
                        })
                        return datos
                    return "No se encontro el recordatorio"
                return "No se encontro la lista de Recordatorio"
            return "No se encontro el mes"
        return "No se encontro ese año"
    return "No se encontro el estudiante"
    
def crearCurso():
    pass

def cursosPensum():
    pass

#cargaMasivaEstudiantes("D:\Quincho\VI Semestre\EDD\LabEDD\Estudiantes.txt")
#cargaMasivaEstudiantes("D:\Quincho\VI Semestre\EDD\LabEDD\Estudiantes_Tareas.txt")
#cargaMasivaRecordatorio("D:\Quincho\VI Semestre\EDD\LabEDD\Estudiantes.txt")
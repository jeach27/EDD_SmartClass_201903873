import Estructuras.MatrizDispersa as MAT
import Estructuras.ArbolAVL as AVL
import Estructuras.Estudiantes as est
import Estructuras.ListaDoble as LD
from gramatica import parser, user_list , task_list
import grafoAVL as graf

aEstudiantes = AVL.AVL()
grafo = graf.Grafo()

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
            
def reportes():
    pass

def crearEstudiante(carne,dpi,Nombre,carrera,correo,password,creditos,edad):
    listaA = LD.listaDoble()
    estudiante = est.estudiante(carne,dpi,Nombre,carrera,correo,password,creditos,edad,listaA)
    aEstudiantes.insertar(carne,estudiante)
    return "El estudiante ha sido ingresado exitosamente"
 
def modificarEstudiante():
    pass
    
def eliminarEstudiante():
    pass
    
def obtenerEstudiante():
    pass
    
def crearRecordatorio():
    pass
    
def modificarRecordatorio():
    pass
    
def eliminarRecordatorio():
    pass
    
def obtenerRecordatorio():
    pass
    
def crearCurso():
    pass

def cursosPensum():
    pass

#cargaMasivaEstudiantes("D:\Quincho\VI Semestre\EDD\LabEDD\Estudiantes.txt")
cargaMasivaEstudiantes("D:\Quincho\VI Semestre\EDD\LabEDD\Estudiantes_Tareas.txt")
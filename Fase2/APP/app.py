from APP.funciones import cargaMasivaEstudiantes
from flask import Flask, jsonify, request
from werkzeug.wrappers import CommonRequestDescriptorsMixin
import funciones as fn

app = Flask(__name__) 

@app.route('/carga', methods=['POST'])
def carga():
    detalles = request.get_json()
    tipo = detalles["tipo"]
    ruta = detalles["path"]
    if tipo == "estudiante":
        fn.cargaMasiva(ruta)
        return "Carga Masiva Estudiante"
    elif tipo == "recordatorio":
        pass
    elif tipo == "curso":
        pass

@app.route('/reporte', methods=['GET'])
def reporte():
    detalles = request.get_json()
    tipo = int(detalles["tipo"])
    if tipo == 0:
        pass
    elif tipo == 1:
        carne = detalles["carnet"]
        año = ["año"]
        mes = detalles["mes"]
    elif tipo == 2:
        carne = detalles["carnet"]
        año = ["año"]
        mes = detalles["mes"]
        dia = detalles["dia"]
        hora = detalles["hora"]
    elif tipo == 3:
        pass          
    elif tipo == 4:
        carne = detalles["carnet"]
        año = ["año"]
        semetre = detalles["semestre"]

@app.route('/estudiante', methods=['POST'])
def crear():
    detalles = request.get_json()
    carne = detalles["carnet"]
    dpi = detalles["DPI"]
    Nombre = detalles["nombre"]
    carrera = detalles["carrera"]
    correo = detalles["correo"]
    password = detalles["password"]
    creditos = detalles["creditos"]
    edad = detalles["edad"]
    return fn.crearEstudiante(carne,dpi,Nombre,carrera,correo,password,creditos,edad)
    
@app.route('/estudiante', methods=['PUT'])
def modificar():
    detalles = request.get_json()
    carne = detalles["carnet"]
    dpi = detalles["DPI"]
    Nombre = detalles["nombre"]
    carrera = detalles["carrera"]
    correo = detalles["correo"]
    password = detalles["password"]
    creditos = detalles["creditos"]
    edad = detalles["edad"]

@app.route('/estudiante', methods=['DELETE'])
def eliminar():
    detalles = request.get_json()
    carne = detalles["carnet"]

@app.route('/estudiante', methods=['GET'])
def obtener():
    detalles = request.get_json()
    carne = detalles["carnet"]
    return jsonify({"mensaje":"ya esta"})

@app.route('/recordatorio', methods=['POST'])
def crearR():
    detalles = request.get_json()
    carne = detalles["Carnet"]
    nombre = detalles["Nombre"]
    descripcion = detalles["Descripcion"]
    materia = detalles["Materia"]
    fecha = detalles["Fecha"]
    hora = detalles["Hora"]
    estado = detalles["Estado"]

@app.route('/recordatorio', methods=['PUT'])
def modificarR():
    detalles = request.get_json()
    carne = detalles["Carnet"]
    nombre = detalles["Nombre"]
    descripcion = detalles["Descripcion"]
    materia = detalles["Materia"]
    fecha = detalles["Fecha"]
    hora = detalles["Hora"]
    estado = detalles["Estado"]
    posicion = detalles["Posicion"]

@app.route('/recordatorio', methods=['DELETE'])
def eliminarR():
    detalles = request.get_json()
    fecha = detalles["Fecha"]
    hora = detalles["Hora"]
    posicion = detalles["Posicion"]

@app.route('/recordatorio', methods=['GET'])
def obtenerR():
    detalles = request.get_json()
    fecha = detalles["Fecha"]
    hora = detalles["Hora"]
    posicion = detalles["Posicion"]

@app.route('/cursosEstudiantes', methods=['POST'])
def crearCurso():
    pass

@app.route('/cursosPensum', methods=['POST'])
def cursosPensum():
    pass

if __name__ == '__main__':
    app.run(debug=True,port=3000)

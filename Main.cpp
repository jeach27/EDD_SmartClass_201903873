#include <iostream>
#include <stdlib.h>
#include <sstream>
#include <fstream>
#include "./Estructuras/ListaDoble.cpp"
#include "./Estructuras/Cola.cpp"
#include "./Objetos/Estudiante.cpp"
#include "./Objetos/Tareas.cpp"
#include "./Objetos/Errores.cpp"


using namespace std;
ListaDoble<Estudiante> *list = new ListaDoble<Estudiante>();

void menuManual();
void menuMUsuarios();
void menuMTareas();
void menuReportes();
void cargaUsuarios();
void cargaTareas();

int main(){
    int opcion;
    bool repetir = true;

    do
    {
        system("cls");

        // Texto del menú que se verá cada vez
        cout << "\n\n\t\t\tMENU" << endl;
        cout << "\t\t\t----------------" << endl;
        cout << "\n\t1. Carga de Usuarios" << endl;
        cout << "\t2. Carga de Tareas" << endl;
        cout << "\t3. Ingreso Manual" << endl;
        cout << "\t4. Reportes" << endl;
        cout << "\t5. SALIR" << endl;

        cout << "\n\tIngrese una opcion: ";
        cin >> opcion;

        switch (opcion)
        {
        case 1:
            cargaUsuarios();
            break;

        case 2:
            cargaTareas();
            break;

        case 3:
            menuManual();
            break;

        case 4:
            menuReportes();
            break;

        case 5:
            repetir = false;
            break;
        }
    } while (repetir);
    
    return 0;
}

void menuManual(){
    int opcion;
    bool repetir = true;

    do
    {
        system("cls");

        cout << "\n\n\t\t\tMENU" << endl;
        cout << "\t\t\t------------------------" << endl;
        cout << "\n\t1. Usuarios" << endl;
        cout << "\t2. Tareas" << endl;
        cout << "\t3. Regresar" << endl;

        cout << "\n\tIngrese una opcion: ";
        cin >> opcion;

        switch (opcion)
        {
        case 1:
            menuMUsuarios();
            break;

        case 2:
            menuMTareas();
            break;

        case 3:
            repetir = false;
            break;
        }
    } while (repetir);

}

void menuMUsuarios(){
    int opcion;
    bool repetir = true;

    do
    {
        system("cls");

        cout << "\n\n\t\t\tMENU USUARIOS" << endl;
        cout << "\t\t\t------------------------" << endl;
        cout << "\n\t1. Ingresar" << endl;
        cout << "\t2. Modificar" << endl;
        cout << "\t3. Eliminar" << endl;
        cout << "\t4. Regresar" << endl;

        cout << "\n\tIngrese una opcion: ";
        cin >> opcion;

        switch (opcion)
        {
        case 1:
            
            break;

        case 2:
            
            break;
        case 3:

            break;
        case 4:
            repetir = false;
            break;
        }
    } while (repetir);

}

void menuMTareas(){
    int opcion;
    bool repetir = true;

    do
    {
        system("cls");

        cout << "\n\n\t\t\tMENU TAREAS" << endl;
        cout << "\t\t\t------------------------" << endl;
        cout << "\n\t1. Ingresar" << endl;
        cout << "\t2. Modificar" << endl;
        cout << "\t3. Eliminar" << endl;
        cout << "\t4. Regresar" << endl;

        cout << "\n\tIngrese una opcion: ";
        cin >> opcion;

        switch (opcion)
        {
        case 1:
            
            break;

        case 2:
            
            break;
        case 3:

            break;
        case 4:
            repetir = false;
            break;
        }
    } while (repetir);

}

void menuReportes(){
    int opcion;
    bool repetir = true;

    do
    {
        system("cls");

        cout << "\n\n\t\t\tMENU REPORTES" << endl;
        cout << "\t\t\t------------------------" << endl;
        cout << "\n\t1. Lista Usuarios" << endl;
        cout << "\t2. Linealizacion Tarea" << endl;
        cout << "\t3. Regresar" << endl;

        cout << "\n\tIngrese una opcion: ";
        cin >> opcion;

        switch (opcion)
        {
        case 1:
            
            break;

        case 2:
            
            break;

        case 3:
            repetir = false;
            break;
        }
    } while (repetir);

}

void cargaUsuarios(){
    string nombre;
    cout << "\nIngrese ruta de Archivo\n" <<endl;
    cin >> nombre;
    ifstream archivo(nombre);
    string linea;
    char delimitador = ',';
   
    getline(archivo, linea);
    
    while (getline(archivo, linea)){
        stringstream stream(linea); // Convertir la cadena a un stream
        string Carnet, DPI,Nombre,Carrera,Password,Creditos,Edad,Correo;
        // Extraer todos los valores de esa fila
        getline(stream, Carnet, delimitador);
        getline(stream, DPI, delimitador);
        getline(stream, Nombre, delimitador);
        getline(stream, Carrera, delimitador);
        getline(stream, Password, delimitador);
        getline(stream, Creditos, delimitador);
        getline(stream, Edad, delimitador);
        getline(stream, Correo, delimitador);

        Estudiante *nuevo = new Estudiante(Carnet,DPI,Nombre,Carrera,Correo,Password,Creditos,Edad);
        list->insertar(*nuevo);
        /* Imprimir
        cout << "==================" << endl;
        cout << "Carne: " << Carnet << endl;
        cout << "DPI: " << DPI << endl;
        cout << "Nombre: " << Nombre << endl;
        cout << "Carrera: " << Carrera << endl;
        cout << "Password: " << Password << endl;
        cout << "Edad: " << Edad << endl;
        cout << "Correo: " << Correo << endl;
        */
    }
    archivo.close();
    system("pause");
    

}

void cargaTareas(){
    string nombre;
    cout << "\nIngrese ruta de Archivo\n" <<endl;
    cin >> nombre;
    ifstream archivo(nombre);
    string linea;
    char delimitador = ',';
   
    getline(archivo, linea);
    
    while (getline(archivo, linea)){
        stringstream stream(linea); // Convertir la cadena a un stream
        string Mes,Dia,Hora,Carnet,Nombre,Descripcion,Materia,Fecha,Estado;
        // Extraer todos los valores de esa fila
        getline(stream, Mes, delimitador);
        getline(stream, Dia, delimitador);
        getline(stream, Hora, delimitador);
        getline(stream, Carnet, delimitador);
        getline(stream, Nombre, delimitador);
        getline(stream, Descripcion, delimitador);
        getline(stream, Materia, delimitador);
        getline(stream, Fecha, delimitador);
        getline(stream, Estado, delimitador);
        /* Imprimir
        cout << "==================" << endl;
        cout << "Mes: " << Mes << endl;
        cout << "Dia: " << Dia << endl;
        cout << "Hora: " << Hora << endl;
        cout << "Carne: " << Carnet << endl;
        cout << "Nombre: " << Nombre << endl;
        cout << "Descripcion: " << Descripcion << endl;
        cout << "Materia: " << Materia << endl;
        cout << "Fecha: " << Fecha << endl;
        cout << "Estado: " << Estado << endl;
        */
    }
    archivo.close();
    system("pause");

}

/*
-------------JEACH-------------
*/
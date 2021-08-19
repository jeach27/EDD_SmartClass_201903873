#include<iostream>
#include<stdlib.h>
#include"./Estructuras/ListaDoble.cpp"

using namespace std;

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

}

void cargaTareas(){

}

/*
-------------JEACH-------------
*/
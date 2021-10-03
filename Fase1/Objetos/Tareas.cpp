#ifndef TAREAS_H
#define TAREAS_H

#include<iostream>

using namespace std;

class Tareas
{
private:
    /* data */
public:
    int Id;
    string Carne;
    string Nombre;
    string Descripcion;
    string Materia;
    string Fecha;
    string Hora;
    string Estado;
    Tareas(int,string,string,string,string,string,string,string);
    ~Tareas();
};

Tareas::Tareas(int id,string carne,string nombre,string descripcion,string materia,string fecha,string hora,string estado)
{
    this->Id = id;
    this->Carne = carne;
    this->Nombre = nombre;
    this->Descripcion = descripcion;
    this->Materia = materia;
    this->Fecha = fecha;
    this->Hora = hora;
    this->Estado = estado;
}

Tareas::~Tareas()
{
}


#endif
#ifndef ESTUDIANTE_H
#define ESTUDIANTE_H

#include<iostream>

using namespace std;

class Estudiante
{
private:
    /* data */
public:
    string Carne;
    string DPI;
    string Nombre;
    string Carrera;
    string Correo;
    string Password;
    string Creditos;
    string Edad;
    Estudiante(string,string,string,string,string,string,string,string);
    ~Estudiante();
};

Estudiante::Estudiante(string carne,string dpi,string nombre,string carrera,string correo,string password,string creditos,string edad)
{
    this->Carne = carne;
    this->DPI = dpi;
    this->Nombre = nombre;
    this->Carrera = carrera;
    this->Correo = correo;
    this->Password = password;
    this->Creditos = creditos;
    this->Edad = edad;
}

Estudiante::~Estudiante()
{
}


#endif 
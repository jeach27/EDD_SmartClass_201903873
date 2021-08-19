#ifndef ERRORES_H
#define ERRORES_H

#include<iostream>

using namespace std;

class Errores
{
private:
    /* data */
public:
    int Id;
    string Tipo;
    string Campo;
    Errores(int,string,string);
    ~Errores();
};

Errores::Errores(int id,string tipo,string campo)
{
    this->Id = id;
    this->Tipo = tipo;
    this->Campo = campo;
}

Errores::~Errores()
{
}


#endif
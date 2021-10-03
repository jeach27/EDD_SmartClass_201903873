#ifndef NODOLISTA_H
#define NODOLISTA_H

#include<stdlib.h>

template <typename T>
class NodoLista
{
private:
    /* data */
public:
    T valor;
    NodoLista * siguiente;
    NodoLista * anterior;
    NodoLista(T);
    ~NodoLista();
};

template <typename T>
NodoLista<T>::NodoLista(T Valor){
    this->valor = Valor;
    this->siguiente = NULL;
    this->anterior = NULL;
}

template <typename T>
NodoLista<T>::~NodoLista()
{
}


#endif
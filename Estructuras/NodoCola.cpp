#ifndef NODOCOLA_H
#define NODOCOLA_H

#include<stdlib.h>

template <typename T>
class NodoCola
{
private:
    /* data */
public:
    T valor;
    NodoCola * next;
    NodoCola(T Valor);
    ~NodoCola();
};

template <typename T>
NodoCola<T>::NodoCola(T Valor)
{
    this->valor = Valor;
    this->next = NULL;
}

template <typename T>
NodoCola<T>::~NodoCola()
{
}

#endif
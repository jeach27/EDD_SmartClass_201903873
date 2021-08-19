#ifndef COLA_H
#define COLA_H

#include<iostream>
#include<stdlib.h>
#include"NodoCola.cpp"

template <typename T>
class Cola
{
private:
    /* data */
public:
    NodoCola<T> *frente;
    NodoCola<T> *fin;
    int size;
    Cola(/* args */);
    void insertar(NodoCola<T> *&, NodoCola<T>*&, T Valor);
    bool colaVacia(NodoCola<T>*);
    ~Cola();
};

template <typename T>
Cola<T>::Cola(/* args */)
{
    this->frente = NULL;
    this->fin = NULL;
    this->size = 0;
}

template <typename T>
void Cola<T>::insertar(NodoCola<T> *&frente, NodoCola<T> *&fin, T Valor){
    NodoCola<T> *nuevo = new NodoCola<T>(Valor);

    nuevo->valor = Valor;
    nuevo->next = NULL;

    if(colaVacia(frente)){
        frente = nuevo;
    }else{
        fin->next = nuevo;
    }
    fin = nuevo;
    
}

template <typename T>
bool Cola<T>::colaVacia(NodoCola<T> *frente){
    return (frente == NULL)? true : false;
}

template <typename T>
Cola<T>::~Cola()
{
}


#endif

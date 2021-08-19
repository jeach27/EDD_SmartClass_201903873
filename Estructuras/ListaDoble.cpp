#ifndef LISTADOBLE_H
#define LISTADOBLE_H

#include<iostream>
#include<stdlib.h>
#include"NodoLista.cpp"

template <typename T>
class ListaDoble
{
private:
    /* data */
public:
    NodoLista<T> *primero;
    NodoLista<T> *ultimo;
    int size;
    ListaDoble(/* args */);
    void insertar(T Valor);
    ~ListaDoble();
};

template <typename T>
ListaDoble<T>::ListaDoble(/* args */)
{
    this->primero = NULL;
    this->ultimo = NULL;
    this->size = 0;
}

template <typename T>
void ListaDoble<T>::insertar(T Valor){
    NodoLista<T> *nuevo = new NodoLista<T>(Valor);
    if (this->primero == NULL){
        this->primero = nuevo;
        this->ultimo = nuevo;   
        this->size++;     
    }else{
        nuevo->siguiente = this->primero;
        primero->anterior = nuevo;
        
        nuevo->anterior = this->ultimo;
        this->ultimo->siguiente = nuevo;

        this->ultimo = nuevo;
        this->size++;
    }
}

template <typename T>
ListaDoble<T>::~ListaDoble()
{
}


#endif 
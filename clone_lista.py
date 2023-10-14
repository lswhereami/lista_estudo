#!/usr/bin/python3

from doctest import OutputChecker


lista = [4,7,5,8]

def copia(lista):
    clone =[]
    for itens in lista:
        clone.append(itens)
    return itens

#ou
lista[:]
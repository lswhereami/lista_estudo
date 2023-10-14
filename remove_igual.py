#!/usr/bin/python3

def remove_repetidos(lista):
    lista = list(set(sorted(lista)))
    return lista

lista=[int(num) for num in input('digite numeros:').split(',')]

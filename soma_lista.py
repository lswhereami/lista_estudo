#!/usr/bin/python3

def soma_elementos(lista):
    sum = 0
    for num in lista:
        sum += int (num)
    return sum

lista=[int(num) for num in input('digite numeros:').split(',')]

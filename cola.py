#!/usr/bin/python3

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
 "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print(len(alfabeto))
print(alfabeto[:13])
print(alfabeto[13:27])
print(alfabeto[13:])
letras = alfabeto[:]
print(letras)
letras = alfabeto[1:10]
print(letras)
print(letras + alfabeto)
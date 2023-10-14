gerador = (a ** 2 for a in range(15) if a % 2 == 0)

for numero in gerador:
    print(numero)

gerador = (a ** 2 for a in range(15) if a % 2 == 0)
print(next(gerador))  # 0
print(next(gerador))  # 4
print(next(gerador))  # 16
print(next(gerador))  # 36
print(next(gerador))  # 64
print(next(gerador))  # 100
print(next(gerador))  # 144
print(next(gerador))  # 196
#print(next(gerador))   erro

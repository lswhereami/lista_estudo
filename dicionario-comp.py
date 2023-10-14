dic = {f'index {a}': a * 2 for a in range(10) if a % 2 == 0}
print(dic)

for numero, dobro in dic.items():
    print(f'{numero} x 2 = {dobro}')

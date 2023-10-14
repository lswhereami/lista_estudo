# normal
dobro_par = []
for i in range(20):
    if i % 2 == 0:
        dobro_par.append(1 * 2)
print(dobro_par)

# comprehension
# variavel0 = [variavel1 X 2 for varivael1 in range (x) /2 ]
dobropar = [b * 2 for b in range(50) if b % 2 == 0]
print(dobropar)

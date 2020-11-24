from math import sqrt

for i in range(1000, 10000):
    dez = i % 100 #extraindo dezena e unidade
    mil = i // 100 #extraindo milhar e centena
    raiz = sqrt(i)
    if raiz == dez + mil:
        print(i)

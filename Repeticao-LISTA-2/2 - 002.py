n = int(input('Informe um número inteiro: '))
perf = 0

for i in range(1, n+1):
    if n % i == 0:
        perf = perf + i

perf1 = perf - n
print('----------')
if perf1 == n:
    print(f'O número {n} é PERFEITO.')
else:
    print(f'O número {n} NÃO é perfeito.')

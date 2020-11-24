maior = 0

for i in range(1, 6):
    n = float(input(f'Informe o {i}º número: '))
    if n > maior:
        maior = n

print('--------------')
print(f'O maior número informado foi: {maior}')

soma = 0

for i in range(1, 6):
    n = float(input(f'Insira o {i}º valor: '))
    soma = soma + n

media = soma / 5
print('---------------')
print(f'A média dos valores inseridos é: {media:.2f}')

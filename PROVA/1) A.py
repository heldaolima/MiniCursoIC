print('''Questão1- Fazer um programa que peça uma quantidade de números e em seguida separar os números
que forem pares e colocar em um vetor e os que forem impares e colocar em outro vetor. Ao final printar
os vetores.''')

print('----------------')
pares = []
ímpares = []
quant = int(input('Quantos números deseja inserir? '))

for i in range(1, quant+1):
    num = int(input(f'Insira o {i}º número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        ímpares.append(num)

print('----------------')
print(f'PARES: {pares}')
print(f'ÍMPARES: {ímpares}')

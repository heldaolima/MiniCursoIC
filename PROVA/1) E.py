print('''Questão 5- Faça um programa que peça a quantidade de números dentro do intervalo de -329 e 987,
coloque os pares dentro de um vetor e os ímpares dentro de outro vetor, os positivos dentro de um vetor 
e os negativos dentro de outro ao término, print os 4 vetores.''')

print('----------------')
pares = []
ímpares = []
positivos = []
negativos = []
interv = int(input('A análise será até que número do intervalo [-329 e 987]? '))

for i in range(-329, interv+1):
    if i % 2 == 0:
        pares.append(i)
    if i % 2 != 0:
        ímpares.append(i)
    if i < 0:
        negativos.append(i)
    if i > 0:
        positivos.append(i)

print('----------------')
print(f'Pares: {pares}')
print(f'Ímpares: {ímpares}')
print(f'Negativos: {negativos}')
print(f'Positivos: {positivos}')

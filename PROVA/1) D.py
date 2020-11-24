print('''Questão 4-Faça um programa que peça uma quantidade de números ao usuário e identifique qual o menor 
número digitado e print.''')

print('----------------')
quant = int(input('Quantos números deseja informar? '))
n = float(input('Informe o 1º número: '))
menor = n

for i in range(2, quant+1):
    n = float(input(f'Informe o {i}º número: '))
    if n < menor:
        menor = n

print('----------------')
print(f'Entre os {quant} números informados, o menor foi {menor}')

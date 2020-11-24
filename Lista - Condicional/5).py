"""Faça um programa que lê um valor em reais e calcule qual o menor número possível de notas de 100, 50,
10, 5 e 1 em que o valor lido pode ser decomposto. Escrever o valor lido e a relação de notas necessárias."""

n = float(input('Insira uma quantia: R$'))
print(f'O valor R${n} pode ser decomposto em: ')
print(f'{n//100} notas de R$100.00')
print(f'{n//50} notas de R$50.00')
print(f'{n//10} notas de R$10.00')
print(f'{n//5} notas de R$5.00')
print(f'{n//1} notas de R$1.00')

"""Faça um programa que leia um número e some 7 caso seja par ou some 4 caso seja ímpar, imprimir o
resultado desta operação."""
num = int(input('Insira um número: '))
if num % 2 == 0:
    print('PAR')
    print(num + 7)
else:
    print('ÍMPAR')
    print(num + 4)

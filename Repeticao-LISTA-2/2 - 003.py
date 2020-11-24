soma = 0
cont = 1
nome = input('Nome: ')
salario = float(input('Salário: R$'))
maior = salario
menor = salario
soma = salario
opcao = input('Continuar? [S/N]: ').upper()[0]

while opcao not in 'Nn':
    nome = input('Nome: ')
    salario = float(input('Salário: R$'))
    soma = soma + salario
    if salario > maior:
        maior = salario
    elif salario < menor:
        menor = salario
    cont = cont + 1
    opcao = input('Continuar? [S/N]: ').upper()[0]

media = soma / cont
print('------------------')
print(f'A média entre os salários foi R${media:.2f}')
print(f'O maior salário informado foi: R${maior:.2f}')
print(f'O menor salário informado foi: R${menor:.2f}')

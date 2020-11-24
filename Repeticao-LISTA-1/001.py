nome = input('Nome: ')
while len(nome) < 3:
    nome = input('Opção inválida. Inserir nome de mais de 3 caracteres.\nNome: ')

idade = int(input('Idade: '))
while not 0 <= idade <= 150:
    idade = int(input('Opção inválida. Inserir idade entre 0 e 150.\nIdade: '))

salario = float(input('Salário: R$'))
while salario <= 0:
    salario = float(input('Opção inválida. Inserir valor maior que 0.\nSalário: R$'))

sexo = input('Sexo [ M/F ]: ').upper()[0]
while sexo not in 'MF':
    sexo = input('Opção inválida. Inserir sexo [ M/F ]: ').upper()[0]

estcivil = input('Estado civil [ S/C/V/D ]: ').upper()[0]
while estcivil not in 'SCVD':
    estcivil = input('Opção inválida. Inserir estado civil [ S/C/V/D ]: ').upper()[0]

print('----------------')
print(f'''Nome: {nome}
Idade: {idade}
Salário: R${salario}
Sexo: {sexo}
Estado Civil: {estcivil}''')

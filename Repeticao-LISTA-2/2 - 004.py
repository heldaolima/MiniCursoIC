n = int(input('Número de alunos que prestaram o vestibular de engenharia:  '))
print('Insira os dados dos alunos APROVADOS ("X" encerra o programa).')
sexo = input('Sexo [M/F/X]: ').upper()[0]
if sexo not in 'Xx':
    if sexo in 'Mm':
        contm = 1
    cont = 1
contvez = 0

while sexo not in 'X':
    vezes = int(input('Quantas vezes prestou o vestibular: '))
    if vezes > 3:
        contvez = contvez + 1
    sexo = input('Sexo [M/F/X]: ').upper()[0]
    if sexo not in 'X':
        if sexo in 'M':
            contm = contm + 1
        cont = cont + 1
    else:
        print('-------------')

porcm = float(contm * 100 / cont)
porcvez = float(contvez * 100 / cont)
print(f'{cont} alunos foram aprovados no vestibular.')
print(f'{porcm:.1f}% dos aprovados são homens.')
print(f'{porcvez:.1f}% dos aprovados prestaram o vestibular mais de 3 vezes.')

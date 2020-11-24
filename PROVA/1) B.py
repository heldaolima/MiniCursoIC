print('''Questão2- Fazer um programa com uma série de perguntas ao usuário para saber se ele é suspeito 
de um crime. Ao final print o resultado.
Pergunta 1- Conhece a vítima?
Pergunta 2- Mora no bairro da vítima?
Pergunta 3- Esteve com a vítima?
Pergunta 4- Esteve na casa da vítima no dia do crime?
Entre 0 e 1 resposta sim= Inocente
Entre 2 e 3 respostas sim= Suspeito
4 perguntas sim= Assassino.''')

print('----------------')
contsim = 0
print('Precisamos fazer algumas perguntas relacionadas ao crime ocorrido...')
p1 = input('Você conhece a vítima? [S/N]: ').upper()[0]
while p1 not in 'SN':
    p1 = input('Você conhece a vítima? [S/N]: ').upper()[0]
if p1 in 'S':
    contsim = contsim + 1

p2 = input('Você mora no mesmo bairro da vítima? [S/N]: ').upper()[0]
while p2 not in 'SN':
    p2 = input('Você mora no mesmo bairro da vítima? [S/N]: ').upper()[0]
if p2 in 'S':
    contsim = contsim + 1

p3 = input('Você esteve com a vítima? [S/N]: ').upper()[0]
while p3 not in 'SN':
    p3 = input('Você esteve com a vítima? [S/N]: ').upper()[0]
if p3 in 'S':
    contsim = contsim + 1

p4 = input('Você esteve na casa da vítima no dia do crime? [S/N]: ').upper()[0]
while p4 not in 'SN':
    p4 = input('Você esteve na casa da vítima no dia do crime? [S/N]: ').upper()[0]
if p4 in 'S':
    contsim = contsim + 1

print('----------------')
if contsim <= 1:
    print('Inocente. Pode ir para casa.')
elif 2 <= contsim <= 3:
    print('Suspeito. Nós o contataremos para mais informações.')
else:
    print('Culpado! Acompanhe-nos à delegacia!')

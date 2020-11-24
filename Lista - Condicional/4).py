"""Faça um programa que peça 4 notas de um aluno e calcule sua média, além disso o programa deve pedir
o sexo do aluno (M ou F). Se o sexo for masculino, o resultado deverá ser precedido de “Caro aluno, seu
resultado é: “. Se for feminino, o resultado deverá ser precedido de “Cara aluna, seu resultado é: “."""
n1 = float(input('Insira a sua primeira nota: '))
n2 = float(input('Insira a sua segunda nota: '))
n3 = float(input('Insira a sua terceira nota: '))
n4 = float(input('Insira a sua quarta nota: '))
media = (n1 + n2 + n3 + n4) / 4
sexo = input('Qual o seu sexo [M ou F]? ').upper()
print('--------------')
if 'M' in sexo:
    print(f'Caro aluno, seu resultado é: {media:.1f}')
elif 'F' in sexo:
    print(f'Cara aluna, seu resultado é: {media:.1f}')

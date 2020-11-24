"""6) Faça um programa que pergunte o usuário é homem ou mulher. E calcule o seu IMC com a fórmula:
Para homens : IMC = 𝑷𝒆𝒔𝒐/𝑨𝒍𝒕𝒖𝒕𝒓𝒂𝟐
Para mulheres : IMC = 𝑷𝒆𝒔𝒐/𝟓− 𝑨𝒍𝒕𝒖𝒕𝒓𝒂𝟐"""
peso = float(input('Insira o seu peso [Kg]: '))
altura = float(input('Insira a sua altura [m]: '))
sexo = input('Insira o seu sexo [M ou F]: ').upper()
if sexo in 'M':
    imc = peso / (altura**2)
    print(f'Sendo homem, o seu IMC vale {imc:.1f}')
elif sexo in 'F':
    imc = peso / (5 - altura**2)
    print(f'Sendo mulher, seu IMC vale {imc:.2f}')
print('Você se encontra em: ', end='')
if imc < 16:
    print('SUBPESO SEVERO')
elif imc == 16 or imc <= 19.9:
    print('SUBPESO')
elif imc == 20 or imc <= 24.9:
    print('SITUAÇÃO NORMAL')
elif imc == 25 or imc <= 29.9:
    print('SOBREPESO')
elif imc == 30 or imc <= 39.9:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')

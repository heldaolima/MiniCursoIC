print('--- DENSIDADE ---')
massa1 = float(input('Insira a massa do primeiro objeto (g): '))
vol1 = float(input('Insira o volume do segundo objeto (cm^3): '))
den1 = massa1 / vol1
print(f'Este objeto tem densidade = {den1:.2f}g/cm^3.')
print('----------')
massa2 = float(input('Insira a massa do segundo objeto (g): '))
vol2 = float(input('Insira o volume do segundo objeto (cm^3):'))
den2 = massa2 / vol2
print(f'Este objeto tem densidade = {den2:.2f}g/cm^3')
print('----------')
if den1 > den2:
    print('O PRIMEIRO objeto é o de maior densidade. ')
elif den2 > den1:
    print('O SEGUNDO objeto é o de maior densidade.')
else:
    print('Os dois objetos têm a mesma densidade')

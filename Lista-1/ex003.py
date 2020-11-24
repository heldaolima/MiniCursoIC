"""Faça um programa que leia o raio de uma circunferência e
através dessa informação calcule o diâmetro, o comprimento da
circunferência e a área Em seguida mostre os resultados na
tela"""

print('--- CIRCUNFERÊNCIA ---')
raio = float(input('Insira o raio da circunferência: '))
diametro = 2 * raio
comprimento = 2 * 3.14 * raio
area = 3.14 * (raio ** 2)
print(f'O diâmetro da circunferência é {diametro}')
print(f'O comprimento da circunferência é {comprimento:.2f}')
print(f'A área da circunferência é {area:.2f}')

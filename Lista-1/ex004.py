"""Faça um programa que leia um ângulo em graus, transforme
esse mesmo ângulo para radianos e em seguida mostre o
resultado na tela"""
grau = float(input('Insira um ângulo em graus: '))
rad = grau * 3.14 / 180
print(f'O ângulo {grau}° em radianos vale aproximadamente {rad}rad')

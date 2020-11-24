"""Faça um programa que peça o capital inicial de uma aplicação financeira e o montante final.
Em seguida, calcule os juros sobre esse investimento. Se os juros forem menor ou igual à 10% retorne
(“ Não faça o investimento “), se forem maior do que 10% retorne (“Faça o investimento”)."""

capital = float(input('Qual o capital inicial da aplicação? R$'))
montante = float(input('Qual o montante final? R$'))
tempo = int(input('Em quantos anos será divido? '))
juros = montante - capital
taxa = juros / (capital*tempo)
print(f'A taxa da aplicação foi de {taxa*100:.2f}%.')
if taxa <= 0.1:
    print('Não faça o investimento')
else:
    print('Faça o investimento')

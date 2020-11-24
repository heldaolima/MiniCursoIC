print('''Questão3- Faça um programa que seja uma calculadora que contém as seguintes operações soma, 
subtração, multiplicação, divisão e potência. Então peça ao usuário a operação que ele pretende fazer 
a operação deve ser identificada através do seu símbolo (+)( - )... e peça dois números, assim faça a 
operação e print.''')

print('-------------------')
print('--- CALCULADORA ---')
operacao = input('Escolha a operação que deseja realizar [ +  -  *  /  ]: ')[0]
while operacao not in '+-*/':
    operacao = input('Escolha a operação que deseja realizar [ +  -  *  /  ]: ')[0]

num1 = float(input('Informe o primeiro valor: '))
num2 = float(input('Informe o segundo valor: '))

if operacao in '+':
    result = num1 + num2
elif operacao in '-':
    result = num1 - num2
elif operacao in '*':
    result = num1 * num2
elif operacao in '/':
    result = num1 / num2

print('-------------------')
print(f'{num1} {operacao} {num2} = {result:.2f}')

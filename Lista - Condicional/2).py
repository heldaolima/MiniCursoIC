"""2) Elabore um programa que calcule o que deve ser pago por um produto, considerando o preço normal
de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir para ler qual
a condição de pagamento escolhida e efetuar o cálculo adequado. Código Condição de pagamento:
1. À vista em dinheiro ou cheque, recebe 10% de desconto
2. À vista no cartão de crédito, recebe 17% de desconto
3. Em duas vezes, preço normal de etiqueta sem juros
4. Em duas vezes, preço normal de etiqueta mais juros de 5%"""

preco = float(input('Qual o valor da compra? R$'))
print('''Opções de pagamento: 
[1] À VISTA EM DINHEIRO OU CHEQUE — 10% de desconto,
[2] À VISTA NO CARTÃO DE CRÉDITO — 17% de desconto.
[3] EM 2x NO CARTÃO — Preço normal
[4] EM 3x OU MAIS — Preço normal + Juros de 5%''')
escolha = int(input('Faça a sua escolha (número diferente cancela a compra): '))
print('------------')
if escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4:
    print('Você escolheu a opção: ', end='')
    if escolha == 1:
        print('À VISTA EM DINHEIRO OU CHEQUE')
        final = preco - (preco * 10/100)
        print(f'Com 10% de desconto, o novo valor da compra é: R${final:.2f}')
    elif escolha == 2:
        print('À VISTA NO CARTÃO DE CRÉDITO')
        final = preco - (preco * 17/100)
        print(f'Com 17% de desconto, o novo valor da compra é: R${final:.2f}')
    elif escolha == 3:
        print('EM 2x NO CARTÃO')
        parcelas = preco / 2
        print(f'O valor da compra será inalterado e divido em duas vezes de R${parcelas:.2f}')
    elif escolha == 4:
        print('EM 3x OU MAIS')
        parcelas = int(input('Em quantas parcelas deseja dividir a compra? '))
        juros = preco * 5/100 * parcelas
        final = juros + preco
        print(f'Com 5% de juros aplicados ao período de {parcelas} meses, o novo valor da compra é: R${final:.2f}.')
        print(f'O valor será pago em {parcelas} parcelas de R${final/parcelas:.2f}')
else:
    print('Compra cancelada.')
print('Volte sempre!')

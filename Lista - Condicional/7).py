print('--- SISTEMA DO SHOPPING DO HELDÃO ---')
print('Bem vindo ao Shopping do Heldão! Através desse sistema, você pode fazer compras sem adentrar o estabelecimento')
print('''Temos as seguintes lojas:
[1] Farmárcia
[2] Mercado
[3] Soverteria
[4] Lanchonete''')
escolha = int(input('Em qual loja você pretende comprar (uma opção diferente encerra o sistema)? '))
print('--------------')
if escolha in [1, 2, 3, 4]:
    print('A loja escolhida foi: ', end='')
    if escolha == 1:
        print('FARMÁCIA')
        loja = 'FARMÁCIA'
        print('''Na FARMÁCIA, as opções disponíveis são:
        [1] Xarope
        [2] Estomazil
        [3] Benegripe
        [4] Engov
        [outro] ENCERRA A COMPRA''')
        opcao = int(input('Faça a sua compra: '))
        print('--------------')
        if opcao in [1, 2, 3, 4]:
            if opcao == 1:
                produto = 'XAROPE'
                preco = 5.99
            elif opcao == 2:
                produto = 'ESTOMAZIL'
                preco = 2.67
            elif opcao == 3:
                produto = 'BENEGRIPE'
                preco = 7.59
            elif opcao == 4:
                produto = 'ENGOVE'
                preco = 0.50
            print(f'Na loja {loja}, o produto {produto} custa R${preco}')
        else:
            print('Compra encerrada.')
    elif escolha == 2:
        print('MERCADO')
        loja = 'MERCADO'
        print('''No MERCADO, as opções disponíveis são:
        [1] Chocolate
        [2] Cheetos
        [3] Guaraná
        [4] Brigadeiro
        [outra opção] ENCERRA A COMPRA''')
        opcao = int(input('Faça a sua compra: '))
        print('--------------')
        if opcao in [1, 2, 3, 4]:
            if opcao == 1:
                produto = 'CHOCOLATE'
                preco = 5.99
            elif opcao == 2:
                produto = 'CHEETOS'
                preco = 6.76
            elif opcao == 3:
                produto = 'GUARANÁ'
                preco = 6.25
            elif opcao == 4:
                produto = 'BRIGADEIRO'
                preco = 4.99
            print(f'Na loja {loja}, o produto {produto} custa R${preco}')
        else:
            print('Compra encerrada.')
    elif escolha == 3:
        print('SORVETERIA')
        loja = 'SORVETERIA'
        print('''Na SORVETERIA, as opções disponíveis são:
        [1] Shake
        [2] Sorvete
        [3] Açaí
        [4] Água
        [outra opção] ENCERRA A COMPRA''')
        opcao = int(input('Faça a sua compra: '))
        print('--------------')
        if opcao in [1, 2, 3, 4]:
            if opcao == 1:
                produto = 'SHAKE'
                preco = 7.45
            elif opcao == 2:
                produto = 'SORVETE'
                preco = 3.50
            elif opcao == 3:
                produto = 'AÇAÍ'
                preco = 12.00
            elif opcao == 4:
                produto = 'ÁGUA'
                preco = 1.99
            print(f'Na loja {loja}, o produto {produto} custa R${preco}')
        else:
            print('Compra encerrada')
    elif escolha == 4:
        print('LANCHONETE')
        loja = 'LANCHONETE'
        print('''Na LANCHONETE, as opções disponíveis são:
        [1] Hambúrguer
        [2] Misto
        [3] Suco
        [4] Brigadeiro
        [outra opção] ENCERRA A COMPRA''')
        opcao = int(input('Faça a sua compra: '))
        print('--------------')
        if opcao in [1, 2, 3, 4]:
            if opcao == 1:
                produto = 'HAMBÚRGUER'
                preco = 15.50
            elif opcao == 2:
                produto = 'MISTO'
                preco = 4.00
            elif opcao == 3:
                produto = 'SUCO'
                preco = 3.99
            elif opcao == 4:
                produto = 'BRIGADEIRO'
                preco = 1.00
            print(f'Na loja {loja}, o produto {produto} custa R${preco}')
        else:
            print('Compra encerrada.')
else:
    print('SISTEMA ENCERRADO')
print('Volte sempre!')

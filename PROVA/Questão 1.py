continuar = 'S'
print('As questões são [1, 2, 3, 4, 5]')
while continuar in 'S':
    quest = int(input('Qual questão deseja ver? '))
    while quest not in [1, 2, 3, 4, 5]:
        quest = int(input('Qual questão deseja ver? '))
    print('----------------')
    if quest == 1:
        print('''Questão1- Fazer um programa que peça uma quantidade de números e em seguida separar os números
        que forem pares e colocar em um vetor e os que forem impares e colocar em outro vetor. Ao final printar
        os vetores.''')

        print('----------------')
        pares = []
        impares = []
        quant = int(input('Quantos números deseja inserir? '))

        for i in range(1, quant + 1):
            num = int(input(f'Insira o {i}º número: '))
            if num % 2 == 0:
                pares.append(num)
            else:
                impares.append(num)

        print('----------------')
        print(f'PARES: {pares}')
        print(f'ÍMPARES: {impares}')

    elif quest == 2:
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

    elif quest == 3:
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

    elif quest == 4:
        print('''Questão 4- Faça um programa que peça uma quantidade de números ao usuário e identifique qual o menor 
        número digitado e print.''')

        print('----------------')
        quant = int(input('Quantos números deseja informar? '))
        n = float(input('Informe o 1º número: '))
        menor = n

        for i in range(2, quant + 1):
            n = float(input(f'Informe o {i}º número: '))
            if n < menor:
                menor = n

        print('----------------')
        print(f'Entre os {quant} números informados, o menor foi {menor}')
        
    elif quest == 5:
        print('''Questão 5- Faça um programa que peça a quantidade de números dentro do intervalo de -329 e 987,
        coloque os pares dentro de um vetor e os ímpares dentro de outro vetor, os positivos dentro de um vetor 
        e os negativos dentro de outro ao término, print os 4 vetores.''')

        print('----------------')
        pares = []
        ímpares = []
        positivos = []
        negativos = []
        print('Análise do intervalo [-329 e 987]:')

        for i in range(-329, 988):
            if i % 2 == 0:
                pares.append(i)
            if i % 2 != 0:
                ímpares.append(i)
            if i < 0:
                negativos.append(i)
            if i > 0:
                positivos.append(i)

        print('----------------')
        print(f'Pares: {pares}')
        print(f'Ímpares: {ímpares}')
        print(f'Negativos: {negativos}')
        print(f'Positivos: {positivos}')

    print()
    print('-----------------------------')
    continuar = input('Deseja continuar [S/N]? ').upper()[0]
    while continuar not in 'SN':
        continuar = input('Deseja continuar [S/N]? ').upper()[0]
print('----------------')
print('Programa encerrado.')

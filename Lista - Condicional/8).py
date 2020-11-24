print('--- SISTEMA DE CONDOMÍNIO ---')
print('Através desse sistema, pode-se checar o registro dos moradores.')
print('O condomínio é dividido em blocos e estes em andares, onde ficam os apartamentos.')
print('''Os blocos são os seguintes:
[1] Poxim
[2] São Francisco''')
escolhabloco = int(input('Em qual bloco deseja checar (outra opção encerra o sistema)? '))
print('------------')
if escolhabloco == 1 or escolhabloco == 2:
    print('O bloco escolhido foi ', end='')
    if escolhabloco == 1:
        print('POXIM')
        bloco = 'POXIM'
        print('''O bloco POXIM divide-se da seguinte forma:
        [1] 1º ANDAR -> Aparts. 101, 102, 103, 104.
        [2] 2º ANDAR -> Aparts. 201, 202, 203, 204.
        [3] 3º ANDAR -> Aparts. 301, 302, 303, 304.
        [4] 4º ANDAR -> Aparts. 401, 402, 403, 404'.''')
        escolhaandar = int(input('Escolha o andar (outro número encerra a checagem): '))
        print('------------')
        if escolhaandar == 1 or escolhaandar == 2 or escolhaandar == 3 or escolhaandar == 4:
            if escolhaandar == 1:
                andar = '1º'
                print('''No primeiro andar há os seguintes apartamentos:
                [1] Apart. 101 
                [2] Apart. 102 
                [3] Apart. 103 
                [4] Apart. 104 ''')
                escolhacasa = int(input('Escolha o apartamento (outro número encerra a checagem): '))
                print('------------')
                if escolhacasa == 1 or escolhacasa == 2 or escolhacasa == 3 or escolhacasa == 4:
                    if escolhacasa == 1:
                        apto = 101
                        morador = 'José'
                    elif escolhacasa == 2:
                        apto = 102
                        morador = 'Paulo'
                    elif escolhacasa == 3:
                        apto = 103
                        morador = 'Alex'
                    elif escolhacasa == 4:
                        apto = 104
                        morador = 'David'
                    print(f'O bloco escolhido foi: {bloco}')
                    print(f'O andar escolhido foi: {andar}')
                    print(f'O apartamento escolhido foi o {apto}, no qual mora {morador}')
                else:
                    print('Checagem encerrada')
            elif escolhaandar == 2:
                andar = '2º'
                print('''No segundo andar há os seguintes apartamentos:
                                [1] Apart. 201 
                                [2] Apart. 202 
                                [3] Apart. 203 
                                [4] Apart. 204 ''')
                escolhacasa = int(input('Escolha o apartamento (outro número encerra a checagem): '))
                print('------------')
                if escolhacasa == 1 or escolhacasa == 2 or escolhacasa == 3 or escolhacasa == 4:
                    if escolhacasa == 1:
                        apto = 201
                        morador = 'Laura'
                    elif escolhacasa == 2:
                        apto = 202
                        morador = 'Paula'
                    elif escolhacasa == 3:
                        apto = 203
                        morador = 'Maria'
                    elif escolhacasa == 4:
                        apto = 204
                        morador = 'Larissa'
                    print(f'O bloco escolhido foi: {bloco}')
                    print(f'O andar escolhido foi: {andar}')
                    print(f'O apartamento escolhido foi o {apto}, no qual mora {morador}')
                else:
                    print('Checagem encerrada')
            elif escolhaandar == 3:
                andar = '3º'
                print('''No terceiro andar há os seguintes apartamentos:
                                [1] Apart. 301 
                                [2] Apart. 302 
                                [3] Apart. 303 
                                [4] Apart. 304 ''')
                escolhacasa = int(input('Escolha o apartamento (outro número encerra a checagem): '))
                print('------------')
                if escolhacasa == 1 or escolhacasa == 2 or escolhacasa == 3 or escolhacasa == 4:
                    if escolhacasa == 1:
                        apto = 301
                        morador = 'Chico'
                    elif escolhacasa == 2:
                        apto = 302
                        morador = 'Neymar'
                    elif escolhacasa == 3:
                        apto = 303
                        morador = 'Lebron'
                    elif escolhacasa == 4:
                        apto = 304
                        morador = 'Wilson'
                    print(f'O bloco escolhido foi: {bloco}')
                    print(f'O andar escolhido foi: {andar}')
                    print(f'O apartamento escolhido foi o {apto}, no qual mora {morador}')
                else:
                    print('Checagem encerrada')
            elif escolhaandar == 4:
                andar = '4º'
                print('''No quanto andar há os seguintes apartamentos:
                                [1] Apart. 401 
                                [2] Apart. 402 
                                [3] Apart. 403 
                                [4] Apart. 404 ''')
                escolhacasa = int(input('Escolha o apartamento (outro número encerra a checagem): '))
                print('------------')
                escolhacasa = int(input('Escolha o apartamento: '))
                if escolhacasa == 1 or escolhacasa == 2 or escolhacasa == 3 or escolhacasa == 4:
                    if escolhacasa == 1:
                        apto = 401
                        morador = 'Vanessa'
                    elif escolhacasa == 2:
                        apto = 402
                        morador = 'Lady'
                    elif escolhacasa == 3:
                        apto = 403
                        morador = 'Lorena'
                    elif escolhacasa == 4:
                        apto = 404
                        morador = 'Maria'
                    print(f'O bloco escolhido foi: {bloco}')
                    print(f'O andar escolhido foi: {andar}')
                    print(f'O apartamento escolhido foi o {apto}, no qual mora {morador}')
                else:
                    print('Checagem cancelada')
            else:
                print('Checagem cancelada')
        else:
            print('Checagem cancelada')
    elif escolhabloco == 2:
        print('SÃO FRANCISCO')
        bloco = 'SÃO FRANCISCO'
        print('''O bloco SÃO FRANCISCO divide-se da seguinte forma:
               [1] 1º ANDAR -> Aparts. 101, 102, 103, 104.
               [2] 2º ANDAR -> Aparts. 201, 202, 203, 204.
               [3] 3º ANDAR -> Aparts. 301, 302, 303, 304.
               [4] 4º ANDAR -> Aparts. 401, 402, 403, 404'.''')
        escolhaandar = int(input('Escolha o andar (outro número encerra a checagem): '))
        print('------------')
        if escolhaandar == 1 or escolhaandar == 2 or escolhaandar == 3 or escolhaandar == 4:
            if escolhaandar == 1:
                andar = '1º'
                print('''No primeiro andar há os seguintes apartamentos:
                                [1] Apart. 101 
                                [2] Apart. 102 
                                [3] Apart. 103 
                                [4] Apart. 104 ''')
                escolhacasa = int(input('Escolha o apartamento (outro número encerra a checagem): '))
                print('------------')
                if escolhacasa == 1 or escolhacasa == 2 or escolhacasa == 3 or escolhacasa == 4:
                    if escolhacasa == 1:
                        apto = 101
                        morador = 'Flávio'
                    elif escolhacasa == 2:
                        apto = 102
                        morador = 'Gabriel'
                    elif escolhacasa == 3:
                        apto = 103
                        morador = 'Monique'
                    elif escolhacasa == 4:
                        apto = 104
                        morador = 'Noberto'
                    print(f'O bloco escolhido foi: {bloco}')
                    print(f'O andar escolhido foi: {andar}')
                    print(f'O apartamento escolhido foi o {apto}, no qual mora {morador}')
                else:
                    print('Checagem encerrada')
            elif escolhaandar == 2:
                andar = '2º'
                print('''No segundo andar há os seguintes apartamentos:
                                [1] Apart. 201 
                                [2] Apart. 202 
                                [3] Apart. 203 
                                [4] Apart. 204 ''')
                escolhacasa = int(input('Escolha o apartamento (outro número encerra a checagem): '))
                print('------------')
                if escolhacasa == 1 or escolhacasa == 2 or escolhacasa == 3 or escolhacasa == 4:
                    if escolhacasa ==1:
                        apto = 201
                        morador = 'Kaike'
                    elif escolhacasa == 2:
                        apto = 202
                        morador = 'Matheus'
                    elif escolhacasa == 3:
                        apto = 203
                        morador = 'Danilo'
                    elif escolhacasa == 4:
                        apto = 204
                        morador = 'Ricardo'
                    print(f'O bloco escolhido foi: {bloco}')
                    print(f'O andar escolhido foi: {andar}')
                    print(f'O apartamento escolhido foi o {apto}, no qual mora {morador}')
                else:
                    print('Checagem encerrada')
            elif escolhaandar == 3:
                andar = '3º'
                print('''No terceiro andar há os seguintes apartamentos:
                                [1] Apart. 301 
                                [2] Apart. 302 
                                [3] Apart. 303 
                                [4] Apart. 304 ''')
                escolhacasa = int(input('Escolha o apartamento (outro número encerra a checagem): '))
                print('------------')
                if escolhacasa == 1 or escolhacasa == 2 or escolhacasa == 3 or escolhacasa == 4:
                    if escolhacasa == 1:
                        apto = 301
                        morador = 'Leandro'
                    elif escolhacasa == 2:
                        apto = 302
                        morador = 'Lukinhas'
                    elif escolhacasa == 3:
                        apto = 303
                        morador = 'Arthur'
                    elif escolhacasa == 4:
                        apto = 304
                        morador = 'Ana'
                    print(f'O bloco escolhido foi: {bloco}')
                    print(f'O andar escolhido foi: {andar}')
                    print(f'O apartamento escolhido foi o {apto}, no qual vive {morador}')
                else:
                    print('Checagem encerrada')
            elif escolhaandar == 4:
                andar = '4º'
                print('''No quarto andar há os seguintes apartamentos:
                                [1] Apart. 401 
                                [2] Apart. 402 
                                [3] Apart. 403 
                                [4] Apart. 404 ''')
                escolhacasa = int(input('Escolha o apartamento (outro número encerra a checagem): '))
                print('------------')
                if escolhacasa == 1 or escolhacasa == 2 or escolhacasa == 3 or escolhacasa == 4:
                    if escolhacasa == 1:
                        apto = 401
                        morador = 'Alberto'
                    elif escolhacasa == 2:
                        apto = 402
                        morador = 'Gisele'
                    elif escolhacasa == 3:
                        apto = 403
                        morador = 'Daniele'
                    elif escolhacasa == 4:
                        apto = 404
                        morador = 'Marta'
                    print(f'O bloco escolhido foi: {bloco}')
                    print(f'O andar escolhido foi: {andar}')
                    print(f'O apartamento escolhido foi o {apto}, no qual mora {morador}')
                else:
                    print('Checagem cancelada')
            else:
                print('Checagem cancelada')
        else:
            print('Checagem cancelada')
else:
    print('SISTEMA ENCERRADO')
print('------------')
print('Volte semrpre.')

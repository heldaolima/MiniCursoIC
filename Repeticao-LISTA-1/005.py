n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
print('--------------')
if n2 - n1 == 1:
    print(f'{n2} segue-se a {n1}.')
elif n1 - n2 == 1:
    print(f'{n1} segue-se a {n2}.')
elif n1 == n2:
    print(f'{n1} = {n2}')
else:
    print(f'Os números entre {n1} e {n2} são: ')
    if n2 > n1:
        for i in range(n1+1, n2):
            print(i, end=' ')
    elif n1 > n2:
        for i in range(n1-1, n2, -1):
            print(i, end=' ')

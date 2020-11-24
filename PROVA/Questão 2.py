lista1 = []
lista2 = []

num = int(input('Informe um número entre 0 e 10: '))
while num < 0 or num > 10:
    print('Número inválido. ', end='')
    num = int(input('Informe um número entre 0 e 10: '))

if 0 <= num <= 5:
    for i in range(0, num+1):
        lista1.append(str(i))
        print(lista1)
elif 6 <= num <= 10:
    for i in range(6, num+1):
        lista2.append(str(i))
        print(lista2)

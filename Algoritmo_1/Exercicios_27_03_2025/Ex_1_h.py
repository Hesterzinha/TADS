n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outro número: '))

if (n1 > n2) and (n1 > n3):
    print(f'O maior número é {n1}')
elif (n2 > n1) and (n2 > n3):
    print(f'O maior número é {n2}')
elif (n3 > n1) and (n3 > n2):
    print(f'O maior número é {n3}')
else:
    print('Os números são iguais')

n1 = float(input('Digite um número: '))

if (n1 >= 0) and (n1 <= 20):
    print('O número pertence ao intervalo A')

if (n1 >= -5) and (n1 <= -1):
    print('O número pertence ao intervalo B')

if (n1 >= 21) and (n1 <= 60):
    print('O número pertence ao intervalo C')

if (n1 >= -100) and (n1 <= 15):
    print('O número pertence ao intervalo D')

if (n1 < -100) or (n1 > 60):
    print('O número não pertence a nenhum intervalo')

import math

n1 = float(input('Digite a circunferência do círculo: '))

print(' Calculadora de área de círculo ')
print()

if n1 <= 0:
    print('Entrada inválida')

area = math.pi * (n1 ** 2)

if n1 > 0:
    print(f'A área do círculo é {area:.2f}')

import math

print('Calculadora de raízes de uma equação de segundo grau')
print()

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
baskara = (b ** 2) - (4 * a * c)

if baskara < 0:
    print('A equação não possui raízes reais.')

else:
    x1 = (-b + math.sqrt(baskara)) / (2 * a)
    x2 = (-b - math.sqrt(baskara)) / (2 * a)
    print(f'O valor de x1 é {x1:.2f} e o valor de x2 é {x2:.2f}')

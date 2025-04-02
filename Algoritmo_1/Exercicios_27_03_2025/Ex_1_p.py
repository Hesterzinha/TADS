import math

l1 = float(input('Digite um lado do triângulo: '))
l2 = float(input('Digite outro lado do triângulo: '))
l3 = float(input('Digite outro lado do triângulo: '))

lados = sorted([l1, l2, l3])
a, b, c = lados[0], lados[1], lados[2]

if math.isclose(c**2, a**2 + b**2):
    print('O triângulo é retângulo')
elif c**2 > a**2 + b**2:
    print('O triângulo é obtusângulo')
else:
    print('O triângulo é acutângulo')

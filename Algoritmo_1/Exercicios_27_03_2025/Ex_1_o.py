l1 = float(input('Digite um lado do triângulo:'))
l2 = float(input('Digite outro lado do triângulo:'))
l3 = float(input('Digite outro lado do triângulo:'))

if (l1 == l2) and  (l2 == l3):
    print('O triângulo é equilátero')
elif (l1 == l2) or (l2 == l3) or (l1 == l3):
    print('O triângulo é isósceles')
else:
    print('O triângulo é escaleno')
z = float(input('Digite um número: '))
w = float(input('Digite outro número: '))

if (w > 0) or (z < 7):
    x = (5*w + 1)/3
    t = 5*z + 2

else:
    x = 5*z + 2
    t = (5*w + 1)/3

y = (7 * x * 2 - 3 * 3 - 8 * t)/5 * (x + 2)

print(f'O valor de y é {y:.2f}')

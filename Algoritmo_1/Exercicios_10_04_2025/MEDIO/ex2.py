n = int(input('digite un numero para saber se ele é perfeito: '))
soma = 0

for i in range(1, n):
    if n % i == 0:
        soma += i

if soma == n:
    print(f'{n} é um número perfeito')
else:
    print(f'{n} não é um número perfeito')

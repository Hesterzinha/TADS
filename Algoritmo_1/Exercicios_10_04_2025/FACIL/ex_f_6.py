n = input('Digite um numero para calcular seu fatorial: ')
fatorial = 1

for i in range(1, int(n)+1):
    fatorial *= i
print(f'O fatorial de {n} é: {fatorial}')

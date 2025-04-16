n = int(input('Digite um numero para saber quantos divisores eles possui: '))
divisores = 0

for i in range(1, n+1):
    if n % i == 0:
        divisores += 1

print(f'O numero {n} possui {divisores} divisores')

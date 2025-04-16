soma = 0
while True:
    n = float(input('Informe um número: '))
    if n < 0:
        continue
    if n == 0:
        break
    soma += n
print(f'Soma dos numeros: {soma}')

equilibrado = 0
instavel = 0

for numero in range(8):
    numeros = int(input(f'Digite {numero}º numero inteiro: '))

    if numeros % 2 == 0 and numeros % 5 == 0 or numeros % 2 != 0 and numeros % 3 == 0:
        print
        equilibrado += 1 

    else:
        instavel += 1 

print(f'Equilibrados: {equilibrado}')
print(f'Instável: {instavel}')

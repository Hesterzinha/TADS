par_divisivel_5 = 0
impar_divisivel_3 = 0
equilibrado = 0
instavel = 0

for numero in range(8, 0, -1):
    numeros = int(input(f'Digite {numero}º numero inteiro: '))

    if numeros % 2 == 0 and numeros % 5 == 0:
        par_divisivel_5 += 1
        equilibrado += 1 

    elif numeros % 2 != 0 and numeros % 3 == 0:
        impar_divisivel_3 += 1
        equilibrado += 1

    else:
        instavel += 1 

print(f'Equilibrados: {equilibrado}')
print(f'Instável: {instavel}')

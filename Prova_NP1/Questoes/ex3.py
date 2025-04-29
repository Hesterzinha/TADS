positivos = 0
energia_total = 0
numeros_necessarios = 0

while energia_total <100:
    numeros_digitados = int(input('Digite um numero: '))

    if numeros_digitados > 0:
        positivos += 1
        energia_total += numeros_digitados
        numeros_necessarios += 1 

    if numeros_digitados < 0:
        energia_total += numeros_digitados
        numeros_necessarios -= 1

    while energia_total >= 100:
        print(f'Você chegou ao limite com {energia_total} de energia. Zerou o game.')
        exit()

print(f'Foram necessarios {numeros_necessarios} numeros para chegar a {energia_total} de energia.')
soma = 0

for cont in range(10):# for cont in range(2, 6) -> Mostrara o intervalo dos numeros dentro do parenteses.
    # for cont in range(3, 19, 4) -> A sequencia começa em 3, e o restante e obtido somando 4 ao numero atual(3).
    # for cont in range(5,0,-1) -> Vamos obter um intervalo decrescente.
    n = float(input('Informe um número: '))
    soma += n
    print(soma)

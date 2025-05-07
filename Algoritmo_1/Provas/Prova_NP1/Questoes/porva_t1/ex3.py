# A
senha = 'Open123'
tentativas = 5
acesso_concedido = False

for i in range(1, 6, +1):
    tentativa_senha = input('Digite a senha: ')

    if tentativa_senha != senha:
        tentativas -= 1
        print(f'Senha incorreta. Tentativas restantantes: {tentativas}')

    if tentativa_senha == senha:
        print('Acesso concedido')
        acesso_concedido = True
        break

if tentativas == 0:
    print('Acesso negado. Terminal bloqueado.')
    exit()

# B
pares = 0
soma_pares = 0
impares = 0
soma_impares = 0

if acesso_concedido:
    print('digite 10 números secretos para continuar. Eu informarei quantos são pares, quantos são ímpares e somarei os valores de cada grupo. Mas cuidado: você não verá os números novamente! ')
    for numeros in range(10, 0, -1):
        numeros_digitados = int(input(f'informe {numeros}º numeros: '))

        if numeros_digitados % 2 == 0:
            pares += 1
            soma_pares += numeros_digitados

        if numeros_digitados % 2 != 0:
            impares += 1
            soma_impares += numeros_digitados

        print(f'Quantidade de Pares {pares} e quantidade de impares {impares}')
        print()
        print()

    print(f'Pares: {pares}      |   Soma dos pares: {soma_pares}')
    print(f'Impares: {impares}      |   Soma dos impares: {soma_impares}')

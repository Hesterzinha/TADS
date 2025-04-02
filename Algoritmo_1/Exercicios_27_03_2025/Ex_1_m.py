print('Média entre 5 números ímpares')
print()

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
n4 = float(input('Digite o quarto número: '))
n5 = float(input('Digite o quinto número: '))
numeros = [n1, n2, n3, n4, n5]  # Lista com os números fornecidos
impares = [num for num in numeros if num % 2 != 0]  # Filtra os números ímpares

if impares:
    media = sum(impares) / len(impares)  # Calcula a média dos números ímpares
    # sum(impares) soma os números ímpares
    # len(impares) conta quantos números ímpares foram fornecidos

    print(f'A média dos números ímpares é: {media:.2f}')
else:
    print('Nenhum número ímpar foi fornecido.')

print('Soma dos números pares')
print()

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outro número: '))
n4 = float(input('Digite outro número: '))

numeros = [n1, n2, n3, n4]  # Lista com os números fornecidos
pares = [num for num in numeros if num % 2 == 0]  # Lista de números pares

if pares:
    soma = sum(pares)  # Calcula a soma dos números pares
    print(f'A soma dos números pares é: {soma:.2f}')
else:
    print('Nenhum número par foi fornecido.')

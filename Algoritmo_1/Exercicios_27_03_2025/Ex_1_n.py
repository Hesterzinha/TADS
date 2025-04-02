n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outro número: '))

numeros = [n1, n2, n3]  # Lista com os números fornecidos
# sorted() ordena a lista em ordem crescente
numeros_ordenados = sorted(numeros)

print(f'Os números em ordem crescente são: {numeros_ordenados}')

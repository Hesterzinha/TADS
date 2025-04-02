a = float(input('Digite um número maior que zero(0): '))
b = float(input('Digite outro número maior que zero(0): '))


if a > 0 and b > 0:
    aux = a
    a = b
    b = aux

    print(f'Após a troca, o valor de a é: {a}')
    print(f'Após a troca, o valor de b é: {b}')
else:
    print('Ambos os números devem ser maiores que zero!')

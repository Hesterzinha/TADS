# Calculadora simples

print('Calculadora simples')
print()

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print()

print('Escolha a operação desejada:')
print()

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print()

print('Digite o número correspondente a operação desejada:')

op = int(input())
print()

if op == 1:
    print('Resultado:', n1+n2)
elif op == 2:
    print('Resultado:', n1-n2)
elif op == 3:
    print('Resultado:', n1*n2)
elif op == 4:
    print('Resultado:', n1/n2)
else:
    print('Operação inválida!')

#  ler duas notas e efetuar as 4 operações matematicas
# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))

# soma = n1 + n2
# subtracao = n1 - n2
# multiplicacao = n1 * n2
# divisao = n1 / n2

# print(f'A soma é: {soma}')
# print(f'A subtração é: {subtracao}')
# print(f'A multiplicação é: {multiplicacao}')
# print(f'A divisão é: {divisao}')


# mostrar a nota final
# calcular a média ponderada tb, onde os pesos sao: 0.2, 0.1, 0.4, 0.3

''' 
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
mediap = (n1 * 0.2 + n2 * 0.1 + n3 * 0.4 + n4 * 0.3)


media =  (n1 + n2 + n3 + n4)/4
print(f'A média é: {media}')
print()
print(f'A média ponderada é: {media:.2f}') '''

'''
1 - ler o valor de  2 lados de um treângulo retangulo, calcular h 

2 - calcular a raiz cúbica de x da exp. abaixo.
x = ((raiz(y)) + a/3)/raiz(b/2a)

'''


import math
n1 = float(input("Digite o primeiro lado do triângulo: "))
n2 = float(input("Digite o segundo lado do triângulo: "))

h = math.sqrt(n1 ** 2 + n2 ** 2)    # hipotenusa

print(f"A hipotenusa é: {h}")

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
y = float(input("Digite o valor de y: "))

x = ((y ** 0.5) + a / 3) / ((b / (2*a)**0.5))

raiz_cubica_x = x ** 1/3


print(f"A raiz cúbica de {x:.2f} é {raiz_cubica_x:.2f}")

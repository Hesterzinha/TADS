import math

n = float(input('Digite um número: '))
x = n * math.pi

print()
# Exemplo de uso da função format() com a constante matemática pi
print('x = n * π = {x:.2f}')

print()

print('Teto de x:', math.ceil(x))
print()
print('Piso de x:', math.floor(x))
print()
print('Valor absoluto de x:', format(math.fabs(x), '.2f'))
print()
print('Fatorial de x:', math.factorial(int(x)))
print()
print('Exponencial de x:', format(math.exp(x), '.2f'))
print()
print('Logaritmo natural de x:', math.log(x))
print()
print('Logaritmo de x na base 10:', math.log10(x))
print()
print('Raiz quadrada de x:', math.sqrt(x))
print()
print('Seno de x:', math.sin(x))
print()
print('Cosseno de x:', math.cos(x))
print()
print('Tangente de x:', math.tan(x))

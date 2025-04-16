# receber um numero e somar de 1 ate o numero digitado
n = float(input("Digite um número: "))
soma = 0

for i in range(int(n)+1):
    soma += i
print(f"A somaé: {soma}")   

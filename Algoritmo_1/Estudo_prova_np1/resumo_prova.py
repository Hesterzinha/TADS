'''

✅ 1. Estruturas de Controle
Condicional

python

if condicao:
    # bloco
elif outra_condicao:
    # outro bloco
else:
    # bloco final
Laço for

python

for i in range(5):  # 0 a 4
    print(i)

for item in lista:
    print(item)
Laço while

python

while condicao:
    # repete enquanto for verdadeira

✅ 2. Tipos de Dados Comuns
Listas

python

lista = [1, 2, 3]
lista.append(4)
lista.remove(2)
lista.sort()
len(lista)
Strings

python

s = "Python"
s.upper()      # "PYTHON"
s.lower()      # "python"
s[0]           # 'P'
s[1:4]         # 'yth'
Dicionários

python

d = {"nome": "Yasmin", "idade": 20}
d["nome"]
d["cidade"] = "Campo Grande"
Conjuntos (set)

python

s = {1, 2, 3}
s.add(4)
s.remove(2)
✅ 3. Funções

python

def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Yasmin"))
✅ 4. Algoritmos Clássicos
Busca Linear

python

def busca_linear(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1
Busca Binária (lista ordenada)

python

def busca_binaria(lista, valor):
    ini, fim = 0, len(lista) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            ini = meio + 1
        else:
            fim = meio - 1
    return -1
Bubble Sort

python

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
Recursão: Fatorial

python

def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n - 1)
✅ 5. Extras Úteis
range(início, fim, passo)

enumerate(lista) → retorna índice + valor

input() → lê string do usuário

int(input()) → lê número inteiro

'''
import random

# Listas

'''
Lista/ Tuplas/ dicionarios 

Listas -> coleçoes heterogeneas de obj, podem ser de qualquer tipo, inclusive outras listas.

[0, 1, 10, "beto', [0.2,0.3]]

listas sao mutaveis 
n1, n2, n3, n4 = 1,2,3,4

lista01 = [1,2,3,4,5,6]

lista02 = [3,14, 'beto', True, []]

-> o zero é o primeiro elemento da lista

-> nunca acessar um index que esteja fora da coleçao

len() -> é uma funçao que retorna o tamanho de uma coleçao

vetor -> array -> coleçao vector



# PESQUISA:
# pop -> Remove e retorna o elemento em uma posição específica (ou o último, se o índice não for especificado).
# remove -> Remove a primeira ocorrência de um elemento.
# zip -> Combina duas ou mais listas em uma lista de tuplas, onde cada tupla contém um elemento de cada lista na mesma posição.
        # tupla -> coleçao imutavel de obj, podem ser de qualquer tipo, inclusive outras tuplas.
# set -> Converte uma lista em um conjunto, removendo duplicatas e ordenando os elementos.
# frozenset -> Converte uma lista em um conjunto imutável, removendo duplicatas e ordenando os elementos.

'''

lista = [1,2,3,4,5]

print(lista)

nome = "beto"

print(nome[0])

# len() -> é uma funçao que retorna o tamanho de uma coleçao

print(len(nome))

progs = ['yes', 'genises', 'pink floyd', 'elp']
# como imprimir letra por letra da lista?

print(progs[0])
print(progs[1])
print(progs[2])
# print(progs[3]) -> so para posicao especifica 

progs[3] = 'Metalica'
# progs[5] = 10

# forma 1
for i in range(len(4)): 
    print(progs[i])
    
# forma 2
for i in progs: 
    print(i)
    
# incluir novo elemento na lista
progs.append('guns')

# trocar o ultimo elemento da lista
progs[-1] = 'novo elemento na ultima posiçao '

# ordernar
progs.sort()
print(progs)

# inverter a lista
progs.reverse()
print(progs)

# remover o ultimo elemento da lista
progs.pop() # Remove e retorna o elemento em uma posição específica (ou o último, se o índice não for especificado).
print(progs)

# remover o primeiro elemento da lista
progs.remove() # Remove a primeira ocorrência de um elemento.
print(progs)

for p in progs:
    print('posicao ?? e elemento ??')
    
for i, p in enumerate(progs): # enumerate() -> retorna o index e o elemento da lista
    # i -> index
    # p -> elemento
    print(f'posicao {i} e elemento {p}')

#  dada as seguintes listas [a, b, c] e [d, e, f] como poderiamos jungar?
lista1 = ['a', 'b', 'c']
lista2 = ['d', 'e', 'f']

lista1 += lista2
'''
Exercicio:
pensando em listas de 50 alunos, onde serao lidas(random) 4 notas 
mostre:

a % de alunos aprovados
a % de alunos reprovados

imprima os 5 primeiros alunos com a media mais alta
imprima os 5 piores alunos 
imrima a nota mais alta, a posicao e qual aluno pertence

'''

notas = []
for i in range(50):
    aluno = []
    for j in range(4):
        aluno.append(random.randint(0, 10))
    notas.append(aluno)
    




'''
Funções Básicas
len(lista): Retorna o tamanho da lista (número de elementos).
ex:
lista = [1, 2, 3]
print(len(lista))  # Saída: 3


print(lista): Exibe a lista no console.
ex:
lista = [1, 2, 3]
print(lista)  # Saída: [1, 2, 3]


Indexação: Acessa elementos pelo índice.
ex:
lista = [10, 20, 30]
print(lista[0])  # Saída: 10


Fatiamento (Slicing): Retorna uma sublista.
ex:
lista = [1, 2, 3, 4, 5]
print(lista[1:4])  # Saída: [2, 3, 4]


Métodos de Manipulação

append(item): Adiciona um elemento ao final da lista.
ex:
lista = [1, 2]
lista.append(3)
print(lista)  # Saída: [1, 2, 3]


insert(index, item): Insere um elemento em uma posição específica.
ex:
lista = [1, 3]
lista.insert(1, 2)
print(lista)  # Saída: [1, 2, 3]


remove(item): Remove a primeira ocorrência de um elemento.
ex:
lista = [1, 2, 3, 2]
lista.remove(2)
print(lista)  # Saída: [1, 3, 2]

pop(index): Remove e retorna o elemento em uma posição específica (ou o último, se o índice não for especificado).
ex:
lista = [1, 2, 3]
item = lista.pop(1)
print(item)  # Saída: 2
print(lista)  # Saída: [1, 3]


clear(): Remove todos os elementos da lista.
ex:
lista = [1, 2, 3]
lista.clear()
print(lista)  # Saída: []


Métodos de Ordenação e Pesquisa

sort(): Ordena a lista em ordem crescente (ou decrescente com reverse=True).
ex:
lista = [3, 1, 2]
lista.sort()
print(lista)  # Saída: [1, 2, 3]


sorted(lista): Retorna uma nova lista ordenada sem modificar a original.
ex:
lista = [3, 1, 2]
nova_lista = sorted(lista)
print(nova_lista)  # Saída: [1, 2, 3]


reverse(): Inverte a ordem dos elementos na lista.
ex:
lista = [1, 2, 3]
lista.reverse()
print(lista)  # Saída: [3, 2, 1]

index(item): Retorna o índice da primeira ocorrência de um elemento.
ex:
lista = [1, 2, 3]
print(lista.index(2))  # Saída: 1

count(item): Conta o número de ocorrências de um elemento.
ex:
lista = [1, 2, 2, 3]
print(lista.count(2))  # Saída: 2


Operações Avançadas

extend(iterável): Adiciona os elementos de outro iterável (como outra lista) ao final da lista.
ex:
lista = [1, 2]
lista.extend([3, 4])
print(lista)  # Saída: [1, 2, 3, 4]


Compreensão de Listas (List Comprehension): Cria listas de forma concisa.
ex:
lista = [x**2 for x in range(5)]
print(lista)  # Saída: [0, 1, 4, 9, 16]


copy(): Retorna uma cópia rasa da lista.
ex:
lista = [1, 2, 3]
copia = lista.copy()
print(copia)  # Saída: [1, 2, 3]


del: Remove um elemento ou fatia da lista.
ex:
lista = [1, 2, 3]
del lista[1]
print(lista)  # Saída: [1, 3]


zip(): Combina elementos de várias listas em pares.
ex:
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
combinada = list(zip(lista1, lista2))
print(combinada)  # Saída: [(1, 'a'), (2, 'b'), (3, 'c')]


enumerate(): Retorna índices e elementos ao iterar.
ex: 
lista = ['a', 'b', 'c']
for i, item in enumerate(lista):
    print(i, item)
# Saída:
# 0 a
# 1 b
# 2 c
'''



# TUPLAS -> semelhante a lista, mas imutavel: nao acrescenta, nao remove, fazer atribuicoes
tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) #as virgulas que definem a tupla

tupla1 = (1,)
print(tupla[0]) # Saída: (1,)

for t in tupla:
    print(t)
    
# para tranformar uma tupla em lista, basta fazer o seguinte:
tupla = list(tupla)
print(tupla) # Saída: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# para tranformar uma lista em tupla, basta fazer o seguinte:
lista = tuple(tupla)
print(lista) # Saída: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    
    
# uniao,intersecao, diferenca entre tuplas
tupla1 = (1, 2, 3)
tupla2 = (3, 4, 5)

tupla_uniao = tupla1 + tupla2 # uniao
print(tupla_uniao) # Saída: (1, 2, 3, 3, 4, 5)

tupla_intersecao = tuple(set(tupla1) & set(tupla2)) # intersecao
print(tupla_intersecao) # Saída: (3,)

tupla_diferenca = tuple(set(tupla1) - set(tupla2)) # diferenca
print(tupla_diferenca) # Saída: (1, 2)

# o q range? -> gera uma lista de numeros inteiros, onde o primeiro numero é o inicio e o segundo o fim
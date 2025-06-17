'''
As listas são uma das estruturas de dados mais versáteis em Python, permitindo armazenar e manipular conjuntos de informações de forma eficiente. Para ajudar você a aprimorar suas habilidades de programação, apresentamos uma série de exercícios práticos que exploram os conceitos de listas em Python. Vamos começar!

1. Criar uma Lista
Começamos com o básico. Crie uma lista de números inteiros e a imprima.

2. Acessar Elementos da Lista
Vamos explorar os elementos da lista. Acesse e imprima o primeiro, o último e um elemento do meio da lista que você criou no exercício anterior.

3. Modificar Elementos da Lista
Faça uma pequena modificação. Modifique um elemento da lista que você criou anteriormente e, em seguida, imprima a lista atualizada.

4. Adicionar Elementos à Lista
Envolve o usuário. Peça ao usuário para inserir um número e adicione-o à lista. Em seguida, imprima a lista atualizada.

5. Remover Elementos da Lista
Hora de remover. Remova um elemento da lista que você criou anteriormente e, em seguida, imprima a lista atualizada.

6. Encontrar o Comprimento da Lista
Meça a lista. Calcule e imprima o comprimento da lista.

7. Somar Elementos da Lista
Some todos os elementos da lista e imprima o resultado.

8. Ordenar uma Lista
Bagunça organizada. Crie uma lista de números desordenados e ordene-a em ordem crescente. Em seguida, imprima a lista ordenada.

9. Inverter uma Lista
Olhando de trás para frente. Inverta a ordem dos elementos em uma lista e a imprima.

10. Contar Elementos
Conte quantas vezes um número específico aparece na lista e imprima o resultado.

11. Fatiar uma Lista
Vamos pegar uma fatia. Crie uma lista com pelo menos 5 elementos e, em seguida, crie uma fatia da lista que inclua os elementos do meio. Imprima a fatia.

12. Mesclar Listas
Misture e combine. Crie duas listas e, em seguida, crie uma terceira lista que seja a mescla das duas. Imprima a lista mesclada.

13. Verificar a Existência de um Elemento
Peça ao usuário para inserir um número e verifique se ele existe na lista. Imprima uma mensagem informando se o número está ou não na lista.

14. Remover Duplicatas
Livre-se das duplicatas. Crie uma lista com elementos duplicados e remova todas as duplicatas, deixando apenas uma ocorrência de cada elemento na lista. Imprima a lista resultante.

15. Substituir Elementos
Substitua e renove. Crie uma lista de palavras e substitua todas as ocorrências de uma palavra específica por outra. Imprima a lista resultante.
'''

# 1
lista_numeros = [1, 2, 3, 4, 5]
print(lista_numeros)

# 2
primeiro_elemento = lista_numeros[0]
ultimo_elemento = lista_numeros[-1]
elemento_meio = lista_numeros[len(lista_numeros) // 2]
print("Primeiro elemento:", primeiro_elemento)
print("Último elemento:", ultimo_elemento)
print("Elemento do meio:", elemento_meio)

# 3
lista_numeros[2] = 10
print("Lista atualizada:", lista_numeros)

# 4
numero_inserido = int(input("Digite um número para adicionar à lista: "))
lista_numeros.append(numero_inserido)
print("Lista atualizada:", lista_numeros)

# 5
elemento_removido = lista_numeros.pop(3)
print(f"Elemento removido: {elemento_removido}")
print("Lista atualizada:", lista_numeros)

# 6
comprimento_lista = len(lista_numeros)
print("Comprimento da lista:", comprimento_lista)

# 7
soma_elementos = sum(lista_numeros)
print("Soma dos elementos da lista:", soma_elementos)

# 8
lista_desordenada = [5, 1, 3, 4, 2]
lista_ordenada = sorted(lista_desordenada)
print("Lista ordenada:", lista_ordenada)

# 9
lista_reversa = lista_numeros[::-1]
print("Lista invertida:", lista_reversa)

# 10
numero_contagem = 2
quantidade = lista_numeros.count(numero_contagem)
print(f"O número {numero_contagem} aparece {quantidade} vezes na lista.")

# 11
lista_elementos = [10, 20, 30, 40, 50, 60]
fatia = lista_elementos[2:4]
print("Fatia da lista:", fatia)

# 12
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_mesclada = lista1 + lista2
print("Lista mesclada:", lista_mesclada)

# 13
numero_verificar = int(
    input("Digite um número para verificar se está na lista: "))
if numero_verificar in lista_numeros:
    print(f"O número {numero_verificar} está na lista.")
else:
    print(f"O número {numero_verificar} não está na lista.")

# 14
lista_duplicatas = [1, 2, 2, 3, 4, 4, 4, 5]
lista_sem_duplicatas = list(set(lista_duplicatas))
print("Lista sem duplicatas:", lista_sem_duplicatas)

# 15
lista_palavras = ["casa", "carro", "casa", "trabalho", "casa"]
palavra_antiga = "casa"
palavra_nova = "apartamento"
lista_atualizada = [palavra_nova if palavra ==
                    palavra_antiga else palavra for palavra in lista_palavras]
print("Lista atualizada:", lista_atualizada)

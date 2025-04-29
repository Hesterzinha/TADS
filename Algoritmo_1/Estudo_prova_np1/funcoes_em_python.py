'''
==========================
GUIA RÁPIDO - FUNÇÕES EM PYTHON 
==========================

🔹 LISTAS (list)
--------------------------
append(x)        -> Adiciona x no final da lista
extend(iterável) -> Adiciona todos os elementos do iterável
insert(i, x)     -> Insere x na posição i
remove(x)        -> Remove a primeira ocorrência de x
pop([i])         -> Remove e retorna o item no índice i (ou o último)
sort()           -> Ordena a lista (altera original)
sorted(lista)    -> Retorna nova lista ordenada
reverse()        -> Inverte a lista
len(lista)       -> Tamanho da lista
x in lista       -> Verifica se x está na lista

🔹 STRINGS (str)
--------------------------
upper()          -> Maiúsculas
lower()          -> Minúsculas
strip()          -> Remove espaços extras nas pontas
replace(a, b)    -> Substitui a por b
split()          -> Divide em lista (por espaço padrão)
join(lista)      -> Junta lista em string com separador
find(x)          -> Retorna índice de x (ou -1)
x in s           -> Verifica se x está na string

🔹 DICIONÁRIOS (dict)
--------------------------
d[key]           -> Acessa valor da chave
get(key)         -> Acessa valor ou None
keys()           -> Retorna todas as chaves
values()         -> Retorna todos os valores
items()          -> Lista de (chave, valor)
update({})       -> Atualiza com outro dicionário
pop(key)         -> Remove chave e retorna valor
key in d         -> Verifica se a chave está no dicionário

🔹 CONJUNTOS (set)
--------------------------
add(x)           -> Adiciona x ao conjunto
remove(x)        -> Remove x (erro se não existe)
discard(x)       -> Remove x (sem erro se não existe)
union(s2)        -> União com outro conjunto
intersection(s2) -> Interseção com s2
difference(s2)   -> Diferença com s2
clear()          -> Esvazia o conjunto
x in s           -> Verifica se x está no conjunto


sep=''             -> Define o separador entre os itens do print()
end=''             -> Define o que será colocado ao final da linha (por padrão, uma nova linha)
'''
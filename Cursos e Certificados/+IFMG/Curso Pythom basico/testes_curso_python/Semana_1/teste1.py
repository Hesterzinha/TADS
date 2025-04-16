# print('funcionouu!')
# Para testar direto no terminal: 'python teste1.py'

# Teste de variáveis e operações matemáticas
import math
n1 = 10  # inteiro (int)
n2 = 2.5  # Fracionário (float)
nome = 'Yasmin'  # Textuais (str)
teste = True  # Valores lógicos (bool)
# nome = str(input('Digite teu nome: ')) -> Para receber dados do usuário.

# depurar = testa linha a linha para encontrar possiveis erros no funcionamento. -> F5

print(n1, n2, nome, teste)  # Imprime todas as variáveis;

print()  # Pula uma linha;

print((n1 + n2)/2)  # Média aritmética;

print(n1**2)  # Elevado ao quadrado;

print(n1//n2)  # Divisão inteira;

print(n1 % n2)  # Resto da divisão;

print(n1/n2)  # Divisão fracionária;

print(n1*n2)  # Multiplicação;

print(n1-n2)  # Subtração;

print(n1+n2)  # Soma;
# Podem ser usados () para definir a ordem de execução das operações matemáticas.


# O parâmetro sep (abreviação de "separator") define o separador que será usado entre os argumentos passados para a função print(). Por padrão, o separador é um espaço (' ').
print(1, 2, 3, sep='-')  # Saída: 1-2-3
# O parâmetro end define o que será adicionado ao final da saída da função print(). Por padrão, o valor de end é uma nova linha ('\n').
print("Hello", end=' ')
print("World!")  # Saída: Hello World!


# Exemplo de uso da função abs()
numero_positivo = 10
numero_negativo = -10

print(abs(numero_positivo))  # Saída: 10
print(abs(numero_negativo))  # Saída: 10

# Exemplo de uso da função chr()
codigo_unicode = 65
caractere = chr(codigo_unicode)
print(caractere)  # Saída: 'A'

print(chr(65))  # Saída: 'A'
print(chr(97))  # Saída: 'a'
print(chr(8364))  # Saída: '€'

# Exemplo de uso da função ord()
caractere = 'A'
codigo_unicode = ord(caractere)
print(codigo_unicode)  # Saída: 65

print(ord('A'))  # Saída: 65
print(ord('a'))  # Saída: 97
print(ord('€'))  # Saída: 8364

# Exemplo de uso da função round()
numero = 3.14159

# Arredonda para 2 casas decimais
print(round(numero, 2))  # Saída: 3.14

# Arredonda para o inteiro mais próximo
print(round(numero))  # Saída: 3

# Exemplo de uso da função type()
# Imprime os tipos de cada variável.
print(type(n1), type(n2), type(nome), type(teste))

# Exemplo de uso da função lower()
texto = "Hello World!"
texto_minusculo = texto.lower()
print(texto_minusculo)  # Saída: hello world!

# Exemplo de uso da função find()
texto = "Hello World!"
subtexto = "World"
indice = texto.find(subtexto)
print(indice)  # Saída: 6

# Busca com índice inicial
indice = texto.find("o", 5)
print(indice)  # Saída: 7

# Busca com índices de início e fim
indice = texto.find("o", 5, 8)
print(indice)  # Saída: 7

# Exemplo de uso da função format()
nome = "Yasmin"
idade = 25
texto = "Olá, {}. Você tem {} anos."
resultado = texto.format(nome, idade)
print(resultado)  # Saída: Olá, Yasmin. Você tem 25 anos.

# Exemplo de substituição por nome
texto = "Olá, {nome}. Você tem {idade} anos."
resultado = texto.format(nome="Yasmin", idade=25)
print(resultado)  # Saída: Olá, Yasmin. Você tem 25 anos.

# Exemplo de formatação de números
numero = 3.14159
texto = "O valor de pi é aproximadamente {0:.2f}."
resultado = texto.format(numero)
print(resultado)  # Saída: O valor de pi é aproximadamente 3.14.

# Exemplo de acesso a elementos de listas e dicionários
lista = [1, 2, 3]
dicionario = {"nome": "Yasmin", "idade": 25}
texto = "Primeiro elemento da lista: {0[0]}, Nome: {1[nome]}"
resultado = texto.format(lista, dicionario)
print(resultado)  # Saída: Primeiro elemento da lista: 1, Nome: Yasmin

# Exemplo de uso da função replace()
texto = "Hello World! World is beautiful."
novo_texto = texto.replace("World", "Earth")
print(novo_texto)  # Saída: Hello Earth! Earth is beautiful.

# Substituir apenas a primeira ocorrência
novo_texto = texto.replace("World", "Earth", 1)
print(novo_texto)  # Saída: Hello Earth! World is beautiful.

# Funções matemáticas

# Funções Aritméticas Básicas

# abs(x): Retorna o valor absoluto de x.

# round(x[, n]): Arredonda x para n dígitos após a vírgula decimal.

# Funções Trigonométricas
# math.sin(x): Retorna o seno de x (em radianos).
# math.cos(x): Retorna o cosseno de x (em radianos).
# math.tan(x): Retorna a tangente de x (em radianos).
# math.asin(x): Retorna o arco-seno de x.
# math.acos(x): Retorna o arco-cosseno de x.
# math.atan(x): Retorna o arco-tangente de x.

# Funções Exponenciais e Logarítmicas
# math.exp(x): Retorna e elevado à potência x.
# math.log(x[, base]): Retorna o logaritmo de x na base especificada. Se a base não for especificada, retorna o logaritmo natural (base e).
# math.log10(x): Retorna o logaritmo de base 10 de x.
# math.log2(x): Retorna o logaritmo de base 2 de x.

# Funções de Potência e Raiz
# math.sqrt(x): Retorna a raiz quadrada de x.
# math.pow(x, y): Retorna x elevado à potência y.

# Funções de Arredondamento e Modulação
# math.ceil(x): Retorna o menor inteiro maior ou igual a x.
# math.floor(x): Retorna o maior inteiro menor ou igual a x.
# math.fmod(x, y): Retorna o resto da divisão de x por y.

# Funções de Constantes
# math.pi: O valor de π (pi).
# math.e: O valor de e (base dos logaritmos naturais).

# Exemplos de uso de funções matemáticas
# Valor absoluto
print(abs(-7))  # Saída: 7

# Arredondamento
print(round(3.14159, 2))  # Saída: 3.14

# Funções trigonométricas
print(math.sin(math.pi / 2))  # Saída: 1.0

# Funções exponenciais e logarítmicas
print(math.exp(1))  # Saída: 2.718281828459045
print(math.log(10))  # Saída: 2.302585092994046

# Funções de potência e raiz
print(math.sqrt(16))  # Saída: 4.0
print(math.pow(2, 3))  # Saída: 8.0

# Funções de arredondamento e modulação
print(math.ceil(4.2))  # Saída: 5
print(math.floor(4.8))  # Saída: 4
print(math.fmod(7, 3))  # Saída: 1.0

# Constantes
print(math.pi)  # Saída: 3.141592653589793
print(math.e)  # Saída: 2.718281828459045

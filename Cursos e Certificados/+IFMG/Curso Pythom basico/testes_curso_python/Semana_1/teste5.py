# Exemplo de concatenização

print('insira os dados')
print()

nome = str(input('Digite teu nome: '))
sobrenome = str(input('Digite teu sobrenome: '))
idade = int(input('Digite tua idade: '))
print()

mensagem = 'Olá, ' + nome + ' ' + sobrenome + \
    ', sua idade é: ' + str(idade) + '.'
print(mensagem)  # str está convertendo a variavel idade para string.

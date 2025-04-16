import math

nome_completo = input('Digite seu nome completo: ')
sobrenome = input('Digite seu sobrenome: ')

pos = nome_completo.find(sobrenome)

if pos != -1:
    print('O sobrenome', sobrenome, 'foi encontrado na posição', pos)

else:
    print('Sobrenome não encontrado!')

n = float(input('Digite um número: '))
print('{n:.8f}'.format(n=n))
# (n=n) -> está formatando o número n com 8 casas decimais e imprimindo o resultado. O n=n dentro do método format() é necessário para associar o valor da variável n ao marcador de posição {n} na string de formato.



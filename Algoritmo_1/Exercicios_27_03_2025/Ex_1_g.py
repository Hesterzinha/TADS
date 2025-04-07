n1 = float(input('Digite a primeira nota: ')) #alt + shift + seta para baixo -> duplica a linha
n2 = float(input('Digite a segunda nota: ')) #alt + seta para baixo -> move a linha para baixo
n3 = float(input('Digite a terceira nota: ')) 
n4 = float(input('Digite a quarta nota: '))

media = (n1 + n2 + n3 + n4) / 4

print(f'A média é {media}')
print()

if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')

#ler um numero de 1 ate 7 e mostrar o dia da semana correspondente
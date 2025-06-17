# Calcular média de duas notas e verificar se o aluno foi aprovado ou reprovado.

# float para aceitar números fracionários e input para receber dados do usuário.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

print('Média:', m)

if m >= 6:
    print('Aprovado')
else:
    print('Reprovado')

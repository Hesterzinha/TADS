nome = input('Digite o nome do funcionário: ')
valor_funcao = float(input('Digite o valor da função: '))
numero_funcoes = int(input('Digite o número de funções: '))

salario_bruto = valor_funcao * numero_funcoes

inss = salario_bruto * 0.08

salario_liquido = salario_bruto - inss

print(f'Nome do funcionário: {nome}')
print()
print(f'Salário bruto: {salario_bruto}')
print()
print(f'Salário líquido: {salario_liquido}')

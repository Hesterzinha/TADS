# operadores lógicos
# not -> NÃO -> Inverte o valor lógico (not true -> False, not false -> True)
# and -> E -> Só é verdadeiro se todas as condições forem verdadeiras (true and true -> True, true and false -> False)
# or -> OU -> Só é falso se todas as condições forem falsas (true or true -> True, true or false -> True, false or false -> False)

n4 = float(input('Digite um número: '))
n5 = float(input('Digite outro número: '))

a = (n4 > n5)
b = (n4 != n5)
c = not (a or b) and (not a)

print()

print('a =', a)
print()

print('b =', b)
print()

print('c =', c)

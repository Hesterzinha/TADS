'''
1 Receber 7 numeros 
2 verificar se algum e negativo e sair da execuçao
verificr se se  tem n minimo 4 multiplos de 3 
'''
multiplos_3 = 0

print('Para tentar abrir o cofre digite 7 algarismos')
print()

for numeros in range(1, 8):
    algarismos = int(
        input(f'Digite o algarismo {numeros} para abrir o cofre: '))

    if algarismos < 0:
        print('Alarme ATIVADO!! Saia imediatamente.')
        exit()

    if algarismos % 3 == 0:
        multiplos_3 += 1

if multiplos_3 >= 4:
    print('Cofre aberto com sucesso!!')
else:
    print('Tentativa falhou! o cofre continua fechado.')

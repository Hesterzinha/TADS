#ler um numero de 1 ate 7 e mostrar o dia da semana correspondente
#verificar a range
# mostrar dia da semana, 1 - domingo

# dia_da_semana = int(input('Digite um número de 1 a 7, para ver o dia da semana: '))

# if dia_da_semana == 1:
#     print('Domingo')
    
# elif dia_da_semana == 2:
#     print('Segunda-feira')
    
# elif dia_da_semana == 3:
#     print('Terça-feira')
    
# elif dia_da_semana == 4:
#     print('Quarta-feira')
    
# elif dia_da_semana == 5:
#     print('Quinta-feira')
    
# elif dia_da_semana == 6:    
#     print('Sexta-feira')
    
# elif dia_da_semana == 7:
#     print('Sábado')
    
# else:
#     print('Número que digitou é inválido!')
    
    
# outra forma de fazer:

# dia_da_semana = int(input('Digite um número de 1 a 7, para ver o dia da semana: '))
# match dia_da_semana:
#     case 1:
#         print('Domingo')
#     case 2:
#         print('Segunda-feira')
#     case 3:
#         print('Terça-feira')
#     case 4:
#         print('Quarta-feira')
#     case 5:
#         print('Quinta-feira')
#     case 6:
#         print('Sexta-feira')
#     case 7:
#         print('Sábado')
#     case _:
#         print('Número que digitou é inválido!')
        

# forma que o professor fez:
dia_da_semana = int(input('Digite um número de 1 a 7, para ver o dia da semana: '))

if dia_da_semana >= 1 and dia_da_semana <= 7:
    if dia_da_semana == 1:
        print('Domingo')
    elif dia_da_semana == 2:
        print('Segunda-feira')
    elif dia_da_semana == 3:
        print('Terça-feira')
    elif dia_da_semana == 4:
        print('Quarta-feira')
    elif dia_da_semana == 5:
        print('Quinta-feira')
    elif dia_da_semana == 6:    
        print('Sexta-feira')
    else:
        print('Sábado')
else:
    print('Número que digitou é inválido!')

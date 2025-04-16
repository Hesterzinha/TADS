'''
1- var de controle
2- condição de parada
3- att da var de controle
'''
#  1 - var de controle
# i = 20

#  2 - condição de parada
# while i < 10:
#     if i % 2 == 0:
#         print(f"i = {i}")

#  3 - att da var de controle
# i = i + 2  # incremento

# criar um laço de repetiçao que dependa da resposta do usuario para continuar o laço
resp = 's'

while resp == 's':  # or resp == 'S'
    print("Ainda estou repetindo...")
    
    while True:
        resp = input(' Deseja continuar? s = sim/ n = nao: ')
        resp = resp.lower()
        if resp == 's' or resp == 'n':
            break  # tremina um laço de repetiçao
        else:
            print('Resposta inválida!')

print('terminei!!')

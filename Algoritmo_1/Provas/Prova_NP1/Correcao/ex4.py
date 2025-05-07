tentativas = 0
numeros_aceitos = 0
nao_primo = 0
se_for_primo = False

while numeros_aceitos < 5:
    numeros = int(input('Digite os numeros: '))

    for primos in range(numeros-1, 1, -1):
        if numeros % primos == 0:
            print('Numero não aceito!')
            nao_primo +=1
            tentativas += 1
            se_for_primo = True
            break
            
    if se_for_primo: 
        print('Numero aceito!')
        numeros_aceitos += 1 
        tentativas += 1

if numeros_aceitos == 5:
    print(f'Portal liberado após {tentativas} tentativas.')

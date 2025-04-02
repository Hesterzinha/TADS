saldo_medio = float(input("Digite o saldo médio: "))
credito20 = saldo_medio * 0.20
credito30 = saldo_medio * 0.30
credito40 = saldo_medio * 0.40

if (saldo_medio >= 0) and (saldo_medio <= 200):
    print(
        f'Seu Saldo Médio é de R$ {saldo_medio:.2f} e você não tem direito a nenhum crédito')

elif (saldo_medio >= 201) and (saldo_medio <= 400):
    print(
        f'Seu Saldo Médio é de R$ {saldo_medio:.2f} e você tem direito a um crédito de 20%')
    print()
    print('Aguarde um momento, estamos processando seu crédito...')
    print()
    print(f' Seu crédito é de: {credito20:.2f}')

elif (saldo_medio >= 401) and (saldo_medio <= 600):
    print(
        f'Seu Saldo Médio é de R$ {saldo_medio:.2f} você tem direito a um crédito de 30%')
    print()
    print('Aguarde um momento, estamos processando seu crédito...')
    print()
    print(f'Seu crédito é de: {credito30:.2f}')

elif saldo_medio > 600:
    print(
        f'Seu Saldo Médio é de R$ {saldo_medio:.2f} e você tem direito a um crédito de 40%')
    print()
    print('Aguarde um momento, estamos processando seu crédito...')
    print()
    print(f'Seu crédito é de: {credito40:.2f}')

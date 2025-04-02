print('Calculadora do peso ideal')
print()

sexo = str(input('Digite seu sexo (Feminino ou Masculino): '))
altura = float(input('Digite sua altura (Em Metros. Ex: 1.60): '))
peso_ideal_m = (62.1 * altura) - 44.7
peso_ideal_h = (72.7 * altura) - 58

if (sexo == 'Feminino') or (sexo == 'feminino'):
    print(f'O peso ideal para você é {peso_ideal_m:.2f} kg')

elif sexo == 'Masculino' or sexo == 'masculino':
    print(f'O peso ideal para você é {peso_ideal_h:.2f} kg')

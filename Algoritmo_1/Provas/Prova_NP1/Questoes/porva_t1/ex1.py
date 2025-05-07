n_passos = int(input('Digite o numero de passos: '))

n_pedras = 0
n_buracos = 0

for obstaculo in range(1, n_passos, +1):
    p_or_b = str(input('Escolha (P) para Pedras e (B) para Buracos:')).upper()
    
    if p_or_b == 'P':
        n_pedras += 1
        
    elif p_or_b == 'B':
        n_buracos += 1
        
    else:
        print(f'{p_or_b} não é Valido. Digite (P) para pedra e (B)  para Buraco.')

if n_buracos > n_pedras:
    print('Cuidado! Mais buracos do que pedras.')
    
else:
    print(f'Números de pedras {n_pedras}')
    print(f'Números de buracos {n_buracos}')

n = input('digite un numero: ')

for i in range(1, int(n)+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

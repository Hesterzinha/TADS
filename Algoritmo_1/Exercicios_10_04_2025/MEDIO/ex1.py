frase = str(input("Digite uma frase: "))
cont = 0

for i in range(len(frase)):
    if frase[i] == 'a' or frase[i] == 'á' or frase[i] == 'A'  or frase[i] == 'Á' or frase[i] == 'e' or frase[i] == 'é' or frase[i] == 'E' or frase[i] == 'É' or frase[i] == 'i' or frase[i] == 'í' or frase[i] == 'I' or frase[i] == 'Í' or frase[i] == 'o' or frase[i] == 'ó' or frase[i] == 'O' or frase[i] == 'Ó' or frase[i] == 'u' or frase[i] == 'ú' or frase[i] == 'U' or frase[i] == 'Ú':
        cont += 1

print(f"Tem {cont} vogais na frase.")

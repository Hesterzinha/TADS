# Converter segundos em horas, minutos e segundos
def segundos_para_hms(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return horas, minutos, segundos_restantes

# Converter horas, minutos e segundos em segundos
def hms_para_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

# Exemplo de uso
segundos = int(input("Digite o número de segundos: "))
horas, minutos, segundos_restantes = segundos_para_hms(segundos)
print(f"{segundos} segundos são equivalentes a {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")

horas = int(input("Digite o número de horas: "))
minutos = int(input("Digite o número de minutos: "))
segundos = int(input("Digite o número de segundos: "))
total_segundos = hms_para_segundos(horas, minutos, segundos)
print(f"{horas} horas, {minutos} minutos e {segundos} segundos são equivalentes a {total_segundos} segundos.")

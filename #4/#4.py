dias = float(input("Número de dias: "))
horas = float(input("Número de horas: "))
minutos = float(input("Número de minutos: "))
segundos = float(input("Número de segundos: "))

tempo = segundos + (minutos * 60) + (horas * 60 * 60) + (dias * 60 * 60 * 24)
print(f"Seu tempo em segundos foi de: {tempo:.2f}")

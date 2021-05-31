#esquece
#esquece
#esquece
#esquece
#esquece
n = float(input("kWh gastos: "))

base = n

valor = 0

if base > 5000:
    valor += base * 0.60

elif base == 5000:

    valor += base * 0.55

elif base > 1000:

    valor += (base - 1000) * 0.60
    
    base = 1000

elif base == 1000:
    valor +=  base * 0.60

elif base > 500:
    valor = base * 0.65

    base -= 500

elif base <= 500:
    valor += n * 0.40

print(f"{valor}")
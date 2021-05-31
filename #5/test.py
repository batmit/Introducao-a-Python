salário = float(input("Digite seu salário: "))
base = salário
imposto = 0

if base > 3000:
    imposto += (base - 3000) * 0.35

    base = 3000
  
if base > 1000:
    imposto += (base - 1000) * 0.20


print(f"{imposto}")
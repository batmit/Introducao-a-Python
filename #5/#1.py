n = int(input("Digite a velocidade que você estava dirigindo: "))
if n > 80:
    c = n - 80
    c = c * 5
    print(f"Sua multa será de: R${c:.2f}")

else:
    print("Continue assim") 
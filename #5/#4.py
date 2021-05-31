n = float(input('Quantos KM você gastou na viagem: '))

passagem = 0 

if n > 200:
    passagem = 0.45 * n
else:
    passagem = 0.50 * n

print(f"{passagem}")
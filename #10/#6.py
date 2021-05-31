v = [9, 8, 7, 12, 0, 13, 21]
p = []# valores ímpares
i = []# valores pares
for c in v:
    if c % 2 == 0: # se o resto da divisão por dois for igual a zero, acontece tal coisa
        p.append(c)
    else:
        i.append(c)
print(f"Pares: {p}")
print(f"ímpares: {i}")
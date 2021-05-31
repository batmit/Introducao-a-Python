n1 = float(input("N1: "))
n2 = float(input("N2: "))
n3 = float(input("N3: "))
maior = 0
if n1 > n2:
    maior = n1
    nome = "N1"
else:
    maior: n2
    nome = "N2"
if maior > n3:
    maior = maior
    
else:
    maior = n3
    nome = 'N3'

print(f"O maior é: {nome}, com {maior}")
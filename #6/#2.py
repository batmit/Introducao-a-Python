n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
x = 0
total = 0
while x < n2:
    total += n1 + n1
    x += 1
    total -= n1
print(f"{total}")
#progama top demais bro
l = []
while True:
    n = input("Digite algo (0 sai): ")
    l.append(n)
    if n == '0':
        break
x = 0
while x < len(l) - 1:
    print(l[x])
    x += 1
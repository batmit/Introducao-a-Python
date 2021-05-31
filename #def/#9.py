L = [1, 7, 2, 9, 15]

def soma(L):
    total = 0
    x = 0
    while x < len(L):
        total += L[x]
        x += 1
    return total

print(soma(L))
print(soma([1, 2, 3, 4, 5, 6]))

# usando o for:
def soma(L):
    total = 0
    for c in L:
        total += c # total += c in L
    return total
print(soma(L))
print(soma([1, 2, 3, 4, 5, 6]))
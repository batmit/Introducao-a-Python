primeira = input("Digite  a primeira string: ")
segunda = input("Digite  a segunda string: ")
terceira = []
for letra in primeira:
    if letra not in segunda and letra not in terceira:
        terceira.append(letra)
print("".join(terceira))

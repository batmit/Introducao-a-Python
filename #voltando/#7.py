a = input("Digite a primeira string: ")
b = input("Digite a segunda string: ")
l = 0
comum = [] # lsita com os comuns
while l < len(a):
    if a[l] in b and a[l] not in comum: # vai verificar se a[l] está no b e não está no comum
        comum.append(a[l]) # adiciona
    l += 1
print("".join(comum)) # usa o join  

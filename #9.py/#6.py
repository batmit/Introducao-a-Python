paren = input("Digite um determinado número de parênteses: ")
pilha = []
x = 0
while x < len(paren):
    if paren[x] == '(':
        pilha.append(paren[x])
    if paren[x] == ")":
        if len(pilha) == 0:
            pilha.append(")")
            break # para a repetição que continuaria mais uma vez            
        pilha.pop(-1) # elimina o último
    x += 1
if len(pilha) == 0 :
    print("OK")
else:
    print("Erro")
preço = 5.2
print(f"O preço é igual a: R${preço:<10.2f}")
print(f"O preço é igual a: R${preço:>10.2f}")
print(f"O preço é igual a: R${preço:^10.2f}") # esse ^ significa no meio. Alinha no meio

print("-" *100)

print(f"O preço é igual a: R${preço:_^10.2f}") # nesse exemplo eu coloco esse _ no meio do 10.2f (espaço destinado para a variável)
print(f"O preço é igual a: R${preço:-^10.2f}")

print("-" *100)

print(f"Inteiro: {int(preço)}")

print("-" *100)

print(f"""Olá meu amigo, como vai? 
Vou bem
Eu também \n Como vai a família?""")
# o for tem um else para que se nada acontecer, se um if não se realizar, ele executa o for
for c in range(101): #lembra que só vai até o penúltimo
    if c == 100:
        print("Elemento encontrado")
        break
else:
    print("lele")

# nesse caso ele verificou se o c fica igual a 99, como ele fica executou o texto e break
# como o comando break foi executado dentro de um if, não se executa o else do for
# se eu não sair, o c vai ficar == 100 e não vai ser mais verdadeiro
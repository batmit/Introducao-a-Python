def soma(x , y):
    a = x + y # essa é uma variável local e não global
    print(a) # posso imprimir aqui, mas não funcionaria fora da função
    return a, "lele"
somas = soma(10, 100) # a variável somas recebe a chamada da função soma com dois valores sendo enviados
print(somas)
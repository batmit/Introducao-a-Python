def somatorio(x):
    if x==1:
        return 1
    else:
        return x + somatorio(x-1)

while True:
    x = int(input("Somatorio de 1 até: "))
    print("Soma: ",somatorio(x) )
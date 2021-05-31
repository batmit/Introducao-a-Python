value = float(input("Qual é o valor da casa? "))
income = float(input("Qual é o seu salário? "))
month = float(input("Quantos meses você gastará? "))

valuemensal = value / month

porcen = income * 0.30

if valuemensal > porcen:
    print("A compra foi regeitada")


income = float(input("What is the initial income of the savings account: "))
time = int(input("How many months do you want to let the money in there? "))
porcent = 2.75
lele = 1
fees = (income / 100) * porcent
while lele < time:
    valor = float(input(f"How many will ye put this month? {lele}: "))
    income += valor
    fees += (income / 100) * porcent 
    lele += 1
print(f"You final value is: {fees + income}. The BTC still a better idea")
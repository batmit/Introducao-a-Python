tabela = {
    'Alface': 0.45,
    'Batata': 1.20,
    'Tomate': 2.30,
    'Feijão': 1.50 
    #lembrar que os valores booleans, ponto flutuante, no python, usam ponto e não vírgula.
}
while True:
    produto = input("Digite o nome do produto, fim para terminar: ")
    if produto == 'fim':
        break
    if produto in tabela:
        print(f"Preço: {tabela[produto]:5.2f} ")
    else:
        print("Num tem isso aqui não")
    print("_-_" * 100)
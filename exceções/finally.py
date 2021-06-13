# temos também o método finally, executa algo mesmo tendo erro
nomes =["Davi", "Daniel", "Mel"]
#tentativa = 0
for tentativa in range(len(nomes)):
    try:
        i = int(input("Digite o índicie: "))
        print(nomes[i - 1])
    except Exception as error:
        print("Erro: ", error)
    # roda o except e depois roda o finally, em outro tipo rodaria o except e acabaria a repetição
    # quando roda o except ocorre um erro e isso acaba fazendo um Break que acaba com o bloco try
    # mas quando usamos finally roda mesmo com esse break
    finally:
        print(f"Tentativa: {tentativa + 1}", )
        #tentativa += 1
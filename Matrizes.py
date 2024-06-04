def determ():
    matriz = []
    while True:
        linha = input("numero de linhas:\n")
        try:
            linha = int(linha)
        except:
            print("Erro, entrada incorreta")
            continue

        coluna = input("numero de colunas:\n")
        try:
            coluna = int(coluna)
        except:
            print("Erro, entrada incorreta")
            continue
        if linha*coluna != 4 and linha*coluna != 9:
            print("Erro, não aceito matrizes maiores que 3x3 e não quadradas")
            continue
        break
    for i in range(linha*coluna):
        matriz.append(0)
    for i in range(len(matriz)):
        x = input(f"digite o{i+1} numero:\n")
        try:
            x = int(x)
            matriz[i].append(x)
        except:
            print("Erro, não é um numero")
            return
        
        if len(matriz) == 4:
            det = (matriz[0]*matriz[-1]) - (matriz[1]*matriz[2])
            print("determinante:" + det)
            return
        else:
            det = (matriz[0]*matriz[4]*matriz[8]+matriz[1]*matriz[5]*matriz[6]+matriz[2]*matriz[3]*matriz[7])-(matriz[0]*matriz[5]*matriz[7]+matriz[1]*matriz[3]*matriz[8]+matriz[2]*matriz[4]*matriz[6])
            print("determinante:" + det)
            return

def mult_matriz():
    matriz = []
    matriz2 = []
    while True:
        linha = input("numero de linhas da primeira matriz:\n")
        try:
            linha = int(linha)
        except:
            print("Erro, entrada incorreta")
            continue

        coluna = input("numero de colunas da primeira matriz:\n")
        try:
            coluna = int(coluna)
        except:
            print("Erro, entrada incorreta")
            continue
        linha2 = input("numero de linhas da segunda matriz:\n")
        try:
            linha2 = int(linha2)
        except:
            print("Erro, entrada incorreta")
            continue

        coluna2 = input("numero de colunas da segunda matriz:\n")
        try:
            coluna2 = int(coluna2)
        except:
            print("Erro, entrada incorreta")
            continue
        if linha != coluna2:
            print("multiplicação não possivel")
            continue
        break
        

    for i in range(linha*coluna):
        matriz.append(0)

    for i in range(len(matriz)):
        x = input(f"digite o{i+1} numero da primeira matriz:\n")
        try:
            x = int(x)
            matriz[i].append(x)
        except:
            print("Erro, não é um numero")
            return
        
    lista = []
    lista2 = []
    for n in range(len(coluna)):
        for i in range(len(linha)):
            lista.append(linha[i])
        print(lista)
        lista2.append(lista)
        lista = []
    matriz = lista2


    for i in range(linha2*coluna2):
        matriz2.append(0)

    for i in range(len(matriz2)):
        x = input(f"digite o{i+1} numero da segunda matriz:\n")
        try:
            x = int(x)
            matriz[i].append(x)
        except:
            print("Erro, não é um numero")
            return


    lista = []
    lista2 = []
    for n in range(len(linha2)):
        for i in range(len(coluna2)):
            lista.append(coluna[i])
        print(lista)
        lista2.append(lista)
        lista = []
    matriz2 = lista2

    lista = []
    for i in range(len(coluna)):
        for n in range(linha):
            x += matriz[i][n]*matriz2[n][i]
        lista.append(x)
    
    print("AXB=" + lista)
    return
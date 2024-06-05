def determ():
    matriz = []
    while True:
        linha = input("Número de linhas:\n")
        try:
            linha = int(linha)
        except:
            print("Erro, entrada incorreta")
            continue
        
        coluna = input("Número de colunas:\n")
        try:
            coluna = int(coluna)
        except:
            print("Erro, entrada incorreta")
            continue
        
        if linha != coluna or linha not in [2, 3]:
            print("Erro, não aceito matrizes não quadradas ou maiores que 3x3")
            continue
        break

    for i in range(linha):
        linhas = []
        for j in range(coluna):
            while True:
                try:
                    x = int(input(f"Digite o número para a posição ({i+1},{j+1}):\n"))
                    linhas.append(x)
                    break
                except ValueError:
                    print("Erro, não é um número")
        matriz.append(linhas)

    if linha == 2:
        det = (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])
        print("Determinante:", det)
    else:  
        det = (matriz[0][0] * matriz[1][1] * matriz[2][2] +
               matriz[0][1] * matriz[1][2] * matriz[2][0] +
               matriz[0][2] * matriz[1][0] * matriz[2][1]) - (
              matriz[0][2] * matriz[1][1] * matriz[2][0] +
              matriz[0][0] * matriz[1][2] * matriz[2][1] +
              matriz[0][1] * matriz[1][0] * matriz[2][2])
        print("Determinante:", det)

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
        
        if coluna != linha2:
            print("multiplicação não possivel")
            continue
        
        break
    
    print("Digite os elementos da primeira matriz:")
    for i in range(linha):
        linhas = []
        for j in range(coluna):
            while True:
                x = input(f"Elemento ({i+1}, {j+1}): ")
                try:
                    x = int(x)
                    linhas.append(x)
                    break
                except:
                    print("Erro, não é um numero")
        matriz.append(linhas)
    
    print("Digite os elementos da segunda matriz:")
    for i in range(linha2):
        linhas = []
        for j in range(coluna2):
            while True:
                x = input(f"Elemento ({i+1}, {j+1}): ")
                try:
                    x = int(x)
                    linhas.append(x)
                    break
                except:
                    print("Erro, não é um numero")
        matriz2.append(linhas)
    
    resultado = [[0 for _ in range(coluna2)] for _ in range(linha)]
    
    for i in range(linha):
        for j in range(coluna2):
            for k in range(coluna):
                resultado[i][j] += matriz[i][k] * matriz2[k][j]
    
    print("AXB =")
    for linhas in resultado:
        print(linhas)

def transposta():
    matriz = []

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
        break
        

    for i in range(linha*coluna):
        matriz.append(0)

    for n in range(len(matriz)):
        try:
            num = int(input(f"digite o{n+1} numero da primeira matriz:\n"))
            matriz[n] = num
        except:
            print("Erro, não é um numero")
            return
        
    lista = []
    lista2 = []
    for n in range(coluna):
        for i in range(linha):
            lista.append(matriz[i])

        for valor in lista:
            matriz.remove(valor)
        print(lista)
        lista2.append(lista)
        lista = []
    matriz = lista2



    transposta = [[0]*linha for col in range(coluna)]
    
    for x in range(len(matriz)):
        for z in range(len(matriz[x])):
           transposta[z][x] = matriz[x][z]
    
    print(transposta)


def subconjuntos():
    A = []
    B = []
    while True:
        x = input('valor conjunto A:\n')
        try:
            x = int(x)
            A.append(x)
        except:
            print('ERRO DE VALOR')
            continue
        x = input('valor conjunto B:\n')
        try:
            x = int(x)
            B.append(x)
        except:
            print('ERRO DE VALOR')
            continue
        op2 = input('1 - Continuar\n2 - Parar de acrescentar valores ao conjuntos\n3 - Sair')
        try:
            op2 = int(op2)
        except:
            print("Valor de entrada errado, finalizando operacao")
            return
        if op2 == 1:
            continue
        elif op2 == 2:
            break
        elif op2 == 3:
            return
        else:
            print("Opção incorreta, encerrando")
            break
    
    x = 0
    for i in range(len(B)):
        for n in range(len(A)):
            if A[n] == B[i]:
                x += 1
    if x == len(A):
        return print("A é subconjunto próprio de B")
    else:
        return print("A não é subconjunto próprio de B")
    

def uniao():    
    A = []
    B = []
    while True:
        x = input('valor conjunto A:\n')
        try:
            x = int(x)
            A.append(x)
        except:
            print('ERRO DE VALOR')
            continue
        x = input('valor conjunto B:\n')
        try:
            x = int(x)
            B.append(x)
        except:
            print('ERRO DE VALOR')
            continue
        op2 = input('1 - Continuar\n2 - Parar de acrescentar valores ao conjuntos\n3 - Sair')
        try:
            op2 = int(op2)
        except:
            print("Valor de entrada errado, finalizando operacao")
            return
        if op2 == 1:
            continue
        elif op2 == 2:
            break
        elif op2 == 3:
            return
        else:
            print("Opção incorreta, encerrando")
            break

    answer = A|B
    return print(answer) 


def interseccao():    
    A = []
    B = []
    while True:
        x = input('valor conjunto A:\n')
        try:
            x = int(x)
            A.append(x)
        except:
            print('ERRO DE VALOR')
            continue
        x = input('valor conjunto B:\n')
        try:
            x = int(x)
            B.append(x)
        except:
            print('ERRO DE VALOR')
            continue
        op2 = input('1 - Continuar\n2 - Parar de acrescentar valores ao conjuntos\n3 - Sair')
        try:
            op2 = int(op2)
        except:
            print("Valor de entrada errado, finalizando operacao")
            return
        if op2 == 1:
            continue
        elif op2 == 2:
            break
        elif op2 == 3:
            return
        else:
            print("Opção incorreta, encerrando")
            break
    
    answer = A - B
    return print(answer)



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
        op2 = input('1 - Continuar conjunto A\n2 - Parar de acrescentar valores ao conjunto A\n')
        try:
            op2 = int(op2)
        except:
            print("Valor de entrada errado, finalizando operacao")
            return
        if op2 == 1:
            continue
        elif op2 == 2:
            break
        else:
            print("Opção incorreta, encerrando")
            return
        
    print(f'O conjunto A está completo: {A}')

    while True:
        x = input('valor conjunto B:\n')
        try:
            x = int(x)
            B.append(x)
        except:
            print('ERRO DE VALOR')
            continue
        op2 = input('1 - Continuar conjunto B\n2 - Parar de acrescentar valores ao conjunto B\n')
        try:
            op2 = int(op2)
        except:
            print("Valor de entrada errado, finalizando operacao")
            return
        if op2 == 1:
            continue
        elif op2 == 2:
            break
        else:
            print("Opção incorreta, encerrando")
            return
    
    print(f'O conjunto B está completo: {B}')
    
    if set(A).issubset(set(B)):
        print("A é subconjunto de B")
    else:
        print("A não é subconjunto de B")
    

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
        op2 = input('1 - Continuar conjunto A\n2 - Parar de acrescentar valores ao conjunto A\n')
        try:
            op2 = int(op2)
        except:
            print("Valor de entrada errado, finalizando operacao")
            return
        if op2 == 1:
            continue
        elif op2 == 2:
            break
        else:
            print("Opção incorreta, encerrando")
            return
        
    print(f'O conjunto A está completo: {A}')

    while True:
        x = input('valor conjunto B:\n')
        try:
            x = int(x)
            B.append(x)
        except:
            print('ERRO DE VALOR')
            continue
        op2 = input('1 - Continuar conjunto B\n2 - Parar de acrescentar valores ao conjunto B\n')
        try:
            op2 = int(op2)
        except:
            print("Valor de entrada errado, finalizando operacao")
            return
        if op2 == 1:
            continue
        elif op2 == 2:
            break
        else:
            print("Opção incorreta, encerrando")
            return
    
    print(f'O conjunto B está completo: {B}')
    resposta = set(A) | set(B)
    return print(resposta) 


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
        op2 = input('1 - Continuar conjunto A\n2 - Parar de acrescentar valores ao conjunto A\n')
        try:
            op2 = int(op2)
        except:
            print("Valor de entrada errado, finalizando operacao")
            return
        if op2 == 1:
            continue
        elif op2 == 2:
            break
        else:
            print("Opção incorreta, encerrando")
            return
        
    print(f'O conjunto A está completo: {A}')

    while True:
        x = input('valor conjunto B:\n')
        try:
            x = int(x)
            B.append(x)
        except:
            print('ERRO DE VALOR')
            continue
        op2 = input('1 - Continuar conjunto B\n2 - Parar de acrescentar valores ao conjunto B\n')
        try:
            op2 = int(op2)
        except:
            print("Valor de entrada errado, finalizando operacao")
            return
        if op2 == 1:
            continue
        elif op2 == 2:
            break
        else:
            print("Opção incorreta, encerrando")
            return
    
    print(f'O conjunto B está completo: {B}')
    
    resposta = set(A).intersection(set(B))
    return print(f'Interseção: {resposta}')



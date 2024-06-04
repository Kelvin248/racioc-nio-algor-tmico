def cres_decres():
    print("axb^x")
    while True:
        a = input("digite o valor de a\n")
        try:
            a = int(a)
            if a == 0:
                print("ERRO, isso anula a exponencial")
                continue
        except:
            print("ERRO, entrada incorreta")
            continue
        b = input("digite o valor de b\n")
        try:
            b = int(b)
            if b == 0:
                print("ERRO, isso anula a exponencial")
                continue
        except:
            print("ERRO, entrada incorreta")
            continue
        break
    if a > 0 and b > 0 or a<0 and b<0:
        print("fucao crescente")
        return
    elif a == 0 or b == 0:
        print("constante")
        return
        
    else:
        print("funcao decrescente")
        return
    
def cal_expo():
    print("axb^x")
    while True:
        a = input("digite o valor de a\n")
        try:
            a = int(a)
            if a == 0:
                print("ERRO, isso anula a exponencial")
                continue
        except:
            print("ERRO, entrada incorreta")
            continue
        b = input("digite o valor de b:\n")
        try:
            b = int(b)
            if b == 0:
                print("ERRO, isso anula a exponencial")
                continue
        except:
            print("ERRO, entrada incorreta")
            continue
        
        x = input("digite o valor de x:\n")
        try:
            x = int(x)
        except:
            print("ERRO, entrada incorreta")
            continue
        break
    y = a*b**x
    print("f(x):"+y)
    return


def expo_grafico():
    import matplotlib.pyplot as plt
    import numpy as np

    print("axb^x")
    while True:
        a = input("digite o valor de a:\n")
        try:
            a = int(a)
            if a == 0:
                print("ERRO, isso anula a exponencial")
                continue
        except:
            print("ERRO, entrada incorreta")
            continue
        b = input("digite o valor de b:\n")
        try:
            b = int(b)
            if b == 0:
                print("ERRO, isso anula a exponencial")
                continue
        except:
            print("ERRO, entrada incorreta")
            continue
        break
    x = np.linspace(0,10,100)
    y = a*b**x
    
    plt.plot(x,y)
    plt.show()
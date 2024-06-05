import matplotlib.pyplot as plt
import numpy as np
def raizes():
    print("função ax^2+bx+c")
    while True:
        a =input("valor de a:\n")
        try:
            a = int(a)
            if a == 0:
                print("Erro, a n pode ser igual a ZERO")
                continue
        except:
            print('erro, digite novamente os valores')
            continue
        b =input("valor de b:\n")
        try:
            b = int(b)
        except:
            print('erro, digite novamente os valores')
            continue
        c =input("valor de c:\n")
        try:
            c = int(c)
        except:
            print('erro, digite novamente os valores')
            continue

        delta = b**2 - 4*a*c
        if delta < 0:
            print("raizes não presente no conjunto dos reais")
            continue
        else:
            break
    if delta == 0:
        print("Raíz única: " + str((-b + delta**(1/2)) / (2*a)))
        return
    else:
        print("Raíz 1: " + str((-b + delta**(1/2)) / (2*a)) + "\nRaíz 2: " + str((-b - delta**(1/2)) / (2*a)))
        return
    
def valor_fx():
    print("função ax^2+bx+c")
    while True:
        a =input("valor de a:\n")
        try:
            a = int(a)
            if a == 0:
                print("Erro, a n pode ser igual a ZERO")
                continue
        except:
            print('erro, digite novamente os valores')
            continue
        b =input("valor de b:\n")
        try:
            b = int(b)
        except:
            print('erro, digite novamente os valores')
            continue
        c =input("valor de c:\n")
        try:
            c = int(c)
        except:
            print('erro, digite novamente os valores')
            continue
        x =input("valor de x:\n")
        try:
            x = int(x)
        except:
            print('erro, digite novamente os valores')
            continue
        
        break
    y = a*x**2 + b*x + c
    print("f(x)"+ y)
    return

def vertice():
    print("função ax^2+bx+c")
    while True:
        a =input("valor de a:\n")
        try:
            a = int(a)
            if a == 0:
                print("Erro, a n pode ser igual a ZERO")
                continue
        except:
            print('erro, digite novamente os valores')
            continue
        b =input("valor de b:\n")
        try:
            b = int(b)
        except:
            print('erro, digite novamente os valores')
            continue
        c =input("valor de c:\n")
        try:
            c = int(c)
        except:
            print('erro, digite novamente os valores')
            continue
        delta = b**2 - 4*a*c
        if delta < 0:
            print("raizes não presente no conjunto dos reais")
            continue
        break
    x = -b/(2*a)
    y = (b**2 -4*a*x)/4*a
    print("x:"+x+"\ny:"+y)
    return


def grafico():
    print("função ax^2+bx+c")
    while True:
        a =input("valor de a:\n")
        try:
            a = int(a)
            if a == 0:
                print("Erro, a n pode ser igual a ZERO")
                continue
        except:
            print('erro, digite novamente os valores')
            continue
        b =input("valor de b:\n")
        try:
            b = int(b)
        except:
            print('erro, digite novamente os valores')
            continue
        c =input("valor de c:\n")
        try:
            c = int(c)
        except:
            print('erro, digite novamente os valores')
            continue
        delta = b**2 - 4*a*c
        if delta < 0:
            print("raizes não presente no conjunto dos reais")
            continue
        break
    x = np.linspace(-10,10,250)
    y = a*x**2+b*x+c
    
    plt.plot(x,y)
    plt.show()
    return


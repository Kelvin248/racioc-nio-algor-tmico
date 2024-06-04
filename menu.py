import sys
from Conjuntos import *
from Funcoes import *
from exponencial import *
from Matrizes import *


def menu_principal():
    op = 0
    while True:
        print("1 - Conjuntos\n2 - Funcoes\n3 - Matrizes\n4 - exponenciais\n5 - Sair")
        op = int(input("Digite sua opção:\n"))
        if op == 5:
            print("Encerrando...")
            sys.exit()
        if op < 1 or op > 5:
            print("Opção inválida...")
            continue
        else:
            if op == 1:
                menu_conjuntos()
            elif op == 2:
                menu_funcoes()
            elif op == 3:
                menu_matrizes()
            elif op == 4:
                menu_exponencial()
def menu_conjuntos():
    op = 0
    while op != 4:
        print("Menu Conjuntos")
        print("1 - Subconjunto\n2 - Uniao\n3 - Interseccao\n4 - Voltar")
        op = int(input("Digite sua opção:\n"))
        if op < 1 or op > 4:
            print("Opção inválida...")
            continue
        else:
            if op == 1:
                subconjuntos()
            elif op == 2:
                uniao()
            elif op == 3:
                interseccao()
            else:
                menu_principal()
def menu_funcoes():
    op = 0
    while op != 5:
        print("Menu Funcoes")
        print("1 - Raizes\n2 - Calcular Valor f(x)\n3 - Vertice\n4 - Grafico\n5 - Voltar")
        op = int(input("Digite sua opção:\n"))
        if op < 1 or op > 5:
            print("Opção inválida...")
            continue
        else:
            if op == 1:
                raizes()
            elif op == 2:
                valor_fx()
            elif op == 3:
                vertice()
            elif op == 4:
                grafico()
            else:
                menu_principal()



def menu_matrizes():
    op = 0
    while op != 4:
        print("Menu Matrizes")
        print("1 - Determinante (2x2) ou (3x3)\n2 - Multiplicacao\n3 - Transposta\n4 - Voltar")
        op = int(input("Digite sua opção:\n"))
        if op < 1 or op > 4:
            print("Opção inválida...")
            continue
        else:
            if op == 1:
                determ()
            elif op == 2:
                print("Chamar a função que faz a opçao 2")
            elif op == 3:
                print("Chamar a função que faz a opçao 3")
            else:
                menu_principal()

def menu_exponencial():
    op = 0
    while op != 4:
        print("Menu Exponencial")
        print("1 - Crescente e Decrescente\n2 - Funcao em X\n3 - Grafico\n4 - Voltar")
        op = int(input("Digite sua opção:\n"))
        if op < 1 or op > 4:
            print("Opção inválida...")
            continue
        else:
            if op == 1:
                cres_decres()
            elif op == 2:
                cal_expo()
            elif op == 3:
                expo_grafico()
            else:
                menu_principal()



menu_principal()
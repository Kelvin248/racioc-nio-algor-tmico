requisitos = input("Digite os Requisitos: ")
file = open("RequisitosFuncionais.txt", "a")
file.write(f"{requisitos}\n")
file.closer()

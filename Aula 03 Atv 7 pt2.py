print("verificando se você pode ou não ir na montanha russa")
idade = int(input("digite sua idade: \n"))
peso = float(input("digite seu peso: \n"))

if idade >= 15 and peso <= 120:
	print("acesso liberado")
else:
	print("acesso negado")
idade = int(input("digite sua idade para saber se é eleitor: \n"))

if idade < 16:
	print(" Não é eleitor")
elif idade >= 16 and idade < 18:
	print(" eleitor facultativo")
elif idade >= 18 and idade <= 65:
	print("eleitor obrigatório")
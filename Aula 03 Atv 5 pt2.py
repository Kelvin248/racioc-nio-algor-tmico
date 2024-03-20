altura = float(input("digite sua altura: \n"))

peso = float(input("digite o seu peso: \n"))

gen = input("digite o seu genero sendo femenino [f] ou masculino [m]: \n")

if gen == "f":
	conta = (62.1*altura)-44.7
	print(f"seu peso ideal é {conta}")
elif gen == "m":
	conta = (72.7*altura)-58
	print(f"seu peso ideal é {conta}")
else:
	print("dados sobre o gênero estão errados, tente novamente")

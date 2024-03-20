idade = int(input("digite a sua idade: \n"))
servico = int(input("digite seu temo de serviço: \n"))

if idade >= 65 or servico >= 30 or idade >= 60 and servico >= 25:
	print("pode se aposentar")
else:
	print("não pode se aposentar")
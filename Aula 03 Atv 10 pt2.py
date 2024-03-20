codigo = int(input("digite o código da faculdade para saber sua situação: [1] PUCPR ou [2]UNICAMP \n"))

if codigo == 1:
	media = float(input("digite sua média: \n"))
	if media >= 7 and media <= 10:
		print("aprovado")
	elif media < 7 and media >=4:
		print("recuperação")
	elif media > 4 and media <= 0:
		print("reprovado")
	else:
		print("ERROR")
elif codigo == 2:
	media = float(input("digite sua média: \n"))
	if media >= 5 and media <= 10:
		print("aprovado")
	elif media < 5 and media >=0:
		print("em exame")
	else:
		print("ERROR")
else:
	print("ERROR")
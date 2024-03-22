status = "c"

while status == "c":
	oper = str(input("[+] soma [-] subtração \n[/] divisão [*] multiplicação \n[s] sair \n"))
	if oper == "+":
		val1 = float(input("?"))
		val2 = float(input("??"))
		print(val1 + val2)
	elif oper == "-":
		val1 = float(input("?"))
		val2 = float(input("??"))
		print(val1 - val2)
	elif oper == "/":
		val1 = float(input("?"))
		val2 = float(input("??"))
		print(val1 / val2)
	elif oper == "*":
		val1 = float(input("?"))
		val2 = float(input("??"))
		print(val1 * val2)
	elif oper == "s":
		status = "s"
	else:
		print("ERROR")
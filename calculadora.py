status = "c"

while status == "c":
	oper = str(input("[+] soma [-] subtração \n[/] divisão [*] multiplicação \n[s] sair \n"))
    	
	if oper == "s":
        	break
    	val1 = float(input("?"))
    	val2 = float(input("??"))
    
	elif oper == "+":
		print(val1 + val2)
	elif oper == "-":
		print(val1 - val2)
	elif oper == "/":
		print(val1 / val2)
	elif oper == "*":
		print(val1 * val2)
	else:
		print("ERROR")


status = "c"

while status == "c":
	oper = str(input("[+] soma [-] subtração \n[/] divisão [*] multiplicação \n[s] sair \n"))
    	
	if oper == "s":
        	break
	if oper !="+" and oper !="-" and oper!="/" and oper!="*":
		print("ERROR")
		continue
	
	val1 = float(input("?"))
	val2 = float(input("??"))
    
	if oper == "+":
		print(val1 + val2)
	elif oper == "-":
		print(val1 - val2)
	elif oper == "/":
		print(val1 / val2)
	elif oper == "*":
		print(val1 * val2)
import time

print("equação: \n ax^2+bx+c = 0")

time.sleep(2)

a = int(input("digite o valor de a: \n"))
b = int(input("digite o valor de b: \n"))
c = int(input("digite o valor de c: \n"))

if a == 0:
	print("o valor de 'a' não pode ser 0")

equacao = b^2-4*a*c

if equacao > 0:
	print("existem duas raízes possíveis")
if equacao < 0:
	print("existem duas raízes imaginárias conjugadas")
if equacao == 0:
	print("existem duas raízes reais iguais")

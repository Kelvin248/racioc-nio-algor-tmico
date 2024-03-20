nota = float(input("digite sua nota de 0 a 10: \n"))

if nota >= 7 and nota <= 10:
	print("aluno passou na matéria")
elif nota < 7 and nota >= 4:
	print("aluno está de recuperação")
elif nota >= 0 and nota < 4:
	print("aluno reprovou na matéria")
else:
	print('o aluno digitou a nota errada')
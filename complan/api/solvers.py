import cmath

def rpn(problem):
	stack = []
	rez = ""
	i = 0
	print(problem)
	# очищаем от пробелов строку
	a = problem.split()
	problem = ""
	for i in a:
		problem += i
	#print(problem)	
	# тут бы сделать проверку на наличие лишних символов и прочего гівна
	
	# ещё бы чекнуть частный случай, когда чисел вообще нет и сделать отдельную для этого ошибку
	
	# отрицательные числа перевести в разность 0 и числа
	old_problem = problem
	problem = ""
	i = 0
	while i < len(old_problem):
		#print(i)
		if i == 0 and (old_problem[i] == '+' or old_problem[i] == '-') and old_problem[i+1].isdigit():
			problem = "0" +  old_problem[i:i+2:]
			i += 2
		elif old_problem[i] == '(' and (old_problem[i+1] == '+' or old_problem[i+1] == '-') and old_problem[i+2].isdigit():
			problem += "(0" +  old_problem[i+1:i+3:]
			i += 3
		else:
			problem += old_problem[i]			
			i += 1
		
	
	# начинаем перевод в обратную польскую запись
	brackets_error = False
	i = 0
	while i < len(problem) and not brackets_error:
		print(problem[i])
		if problem[i].isdigit():
			num = ""
			will = True
			while i < len(problem) and will:
				
				if (problem[i].isdigit() or problem[i] == '.' or problem[i] == 'i'):
					#print(problem[i])
					num += problem[i]
				elif problem[i] == ')':
				#	if len(stack) != 0:
				#		while stack[len(stack)-1] != '(':
				#			rez += stack[len(stack)-1]  + " "
				#			stack.pop()
				#			if len(stack) == 0:
				#				break
						
				#		if len(stack) == 0:
				#			brackets_error = True	
				#		elif stack[len(stack)-1] == '(':
				#			stack.pop()
					will = False		
					i -= 1
				else:
					will = False	
				i += 1
			rez += num + " "

			if (i < len(problem)):
				i -= 2

		elif problem[i] == "e":
			if i < len(problem)-1:
				if problem[i+1] == "i":
					stack.append(problem[i] + "i")
				else:
					stack.append(problem[i])
			else:
				stack.append(problem[i])
			
		
		elif problem[i:i+2:] == "pi":
			if i < len(problem)-2:
				if problem[i+2] == "i":
					stack.append(problem[i:i+2:] + "i")
				else:
					stack.append(problem[i:i+2:])
			else:
				stack.append(problem[i:i+2:])
			
		
		elif problem[i:i+2:] == "re" or problem[i:i+2:] == "im" or problem[i:i+2:] == "tg" or problem[i:i+2:] == "sh" or problem[i:i+2:] == "ch" or problem[i:i+2:] == "th":
			if problem[i+2] != '(':
				brackets_error = True
			else:
				stack.append(problem[i:i+2:])
				i += 1
				
		elif problem[i:i+3:] == "arg" or problem[i:i+3:] == "abs" or problem[i:i+3:] == "exp" or problem[i:i+3:] == "sin" or problem[i:i+3:] == "cos" or problem[i:i+3:] == "ctg" or problem[i:i+3:] == "cth":
			if problem[i+3] != '(':
				brackets_error = True
			else:
				stack.append(problem[i:i+3:])
				i += 2
				
		elif problem[i:i+4:] == "conj" or problem[i:i+4:] == "arsh" or problem[i:i+4:] == "arch" or problem[i:i+4:] == "arth":
			if problem[i+4] != '(':
				brackets_error = True
			else:
				stack.append(problem[i:i+4:])	
				i += 3
		
		elif problem[i:i+5:] == "arctg" or problem[i:i+5:] == "arсth":
			if problem[i+5] != '(':
				brackets_error = True
			else:
				stack.append(problem[i:i+5:])	
				i += 4
		
		elif problem[i:i+6:] == "arcsin" or problem[i:i+6:] == "arccos" or problem[i:i+6:] == "arcctg":
			if problem[i+6] != '(':
				brackets_error = True
			else:
				stack.append(problem[i:i+6:])	
				i += 5
		
		elif problem[i] == '(':
			stack.append('(')
		
		elif problem[i] == ')':
			if len(stack) != 0:
				while stack[len(stack)-1] != '(':
					rez += stack[len(stack)-1]  + " "
					stack.pop()
					if len(stack) == 0:
						break
				
				if len(stack) == 0:
					brackets_error = True	
				elif stack[len(stack)-1] == '(':
					stack.pop()
		
		elif problem[i] == '+' or problem[i] == '-':
			while len(stack) != 0:
				if stack[len(stack)-1] != '(' and stack[len(stack)-1] != ')':
					rez += stack[len(stack)-1]  + " "
					stack.pop()
				else:
					break
			stack.append(problem[i])

		elif problem[i] == '*' and problem[i+1] != '*':	
			while len(stack) != 0:
				if stack[len(stack)-1] != '(' and stack[len(stack)-1] != ')' and stack[len(stack)-1] != '+' and stack[len(stack)-1] != '-':
					rez += stack[len(stack)-1]  + " "
					stack.pop()
				else:
					break
			stack.append(problem[i])
			
		elif problem[i] == ':':
			while len(stack) != 0:
				if stack[len(stack)-1] != '(' and stack[len(stack)-1] != ')' and stack[len(stack)-1] != '+' and stack[len(stack)-1] != '-':
					rez += stack[len(stack)-1]  + " "
					stack.pop()
				else:
					break
			stack.append("/")

		elif problem[i] == '^':
			stack.append(problem[i])

		print("rez = "+rez)
		print("stack = "+str(stack))	
		i += 1

	
	if not brackets_error and stack.count('(') == 0 and stack.count(')') == 0:
		i = len(stack) - 1
		while i >= 0:
			rez += stack[i] + " "
			i -= 1
			
	else:
		rez = "Error with brackets!"

	return rez

def simple_action(problem):
	parsed = problem.split(" ")
	stack = []
	rez = 0
	parsed.pop()
	print(parsed)
	for elem in parsed:
		if elem.isdigit():
			stack.append(complex(elem))
		
		elif elem[0:len(elem)-1:].isdigit() and elem[len(elem)-1] == 'i':
			stack.append(complex(elem.replace('i', 'j')))
			
		elif elem[0:2:] == "pi":
			if len(elem) == 3:
				stack.append(cmath.pi * complex('1j'))
			else:
				stack.append(cmath.pi)
				
		elif elem[0] == "e":
			if len(elem) == 2:
				stack.append(cmath.e * complex('1j'))
			else:
				stack.append(cmath.e)
				
		else:
			if elem == "+":
				stack[len(stack)-2] = stack[len(stack)-2] + stack[len(stack)-1]
				stack.pop()
			elif elem == "-":
				stack[len(stack)-2] = stack[len(stack)-2] - stack[len(stack)-1]
				stack.pop()
			elif elem == "*":
				stack[len(stack)-2] = stack[len(stack)-2] * stack[len(stack)-1]
				stack.pop()
			elif elem == "/":
				stack[len(stack)-2] = stack[len(stack)-2] / stack[len(stack)-1]
				stack.pop()
			elif elem == "^":
				stack[len(stack)-2] = stack[len(stack)-2] ** stack[len(stack)-1]
				stack.pop()
				
			elif elem == "re":
				stack[len(stack)-1] = complex(stack[len(stack)-1].real)
			elif elem == "im":
				stack[len(stack)-1] = complex(stack[len(stack)-1].imag)
			elif elem == "conj":
				stack[len(stack)-1] = complex(stack[len(stack)-1].conjugate())
			
			elif elem == "arg":
				stack[len(stack)-1] = cmath.phase(stack[len(stack)-1])
			elif elem == "abs":
				stack[len(stack)-1] = abs(stack[len(stack)-1])
				
			elif elem == "exp":
				stack[len(stack)-1] = cmath.exp(stack[len(stack)-1])
			elif elem == "ln":
				stack[len(stack)-1] = cmath.log(stack[len(stack)-1])
			
			elif elem == "sin":
				stack[len(stack)-1] = cmath.sin(stack[len(stack)-1])
			elif elem == "cos":
				stack[len(stack)-1] = cmath.cos(stack[len(stack)-1])	
			elif elem == "tg":
				stack[len(stack)-1] = cmath.tan(stack[len(stack)-1])
			elif elem == "ctg":
				stack[len(stack)-1] = cmath.cos(stack[len(stack)-1]) / cmath.sin(stack[len(stack)-1]) # не ну а чо раз котангенса нема
			
			elif elem == "arcsin":
				stack[len(stack)-1] = cmath.asin(stack[len(stack)-1])
			elif elem == "arccos":
				stack[len(stack)-1] = cmath.acos(stack[len(stack)-1])	
			elif elem == "arctg":
				stack[len(stack)-1] = cmath.atan(stack[len(stack)-1])
			elif elem == "arсctg":
				stack[len(stack)-1] = cmath.pi / 2 - cmath.atan(stack[len(stack)-1]) # опять, да
				
			elif elem == "sh":
				stack[len(stack)-1] = cmath.sinh(stack[len(stack)-1])
			elif elem == "ch":
				stack[len(stack)-1] = cmath.cosh(stack[len(stack)-1])	
			elif elem == "th":
				stack[len(stack)-1] = cmath.tanh(stack[len(stack)-1])
			elif elem == "cth":
				stack[len(stack)-1] = cmath.cosh(stack[len(stack)-1]) / cmath.sinh(stack[len(stack)-1]) # не ну а чо раз котангенса нема
				
			elif elem == "arsh":
				stack[len(stack)-1] = cmath.asinh(stack[len(stack)-1])
			elif elem == "arch":
				stack[len(stack)-1] = cmath.acosh(stack[len(stack)-1])	
			elif elem == "arth":
				stack[len(stack)-1] = cmath.atanh(stack[len(stack)-1])
		print(stack)
	
	return str(stack[0])

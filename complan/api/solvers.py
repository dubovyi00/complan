import cmath
from .models import *
import re
 
def isfloat(s):
    find = re.findall(r"\d*\.\d+", s)  
    if find:
        return True
    else:
        return False

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
		elif i <= len(old_problem)-2 and old_problem[i] == '(' and (old_problem[i+1] == '+' or old_problem[i+1] == '-') and old_problem[i+2].isdigit():
			problem += "(0" +  old_problem[i+1:i+3:]
			i += 3
		else:
			problem += old_problem[i]			
			i += 1
		
	problem += " "
	# начинаем перевод в обратную польскую запись
	brackets_error = False
	i = 0
	while i < len(problem) and not brackets_error:
		print()
		print("symbol = "+problem[i])
		if problem[i].isdigit():
			num = ""
			will = True
			while i < len(problem) and will:
				print(problem[i])
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
				#	i -= 1
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

def simple_action(problem, idp):
	parsed = problem.split(" ")
	stack = []
	rez = 0
	parsed.pop()
	n = 1
	print(parsed)
	for elem in parsed:
		if elem.isdigit() or (isfloat(elem) and elem.find('i') == -1):
			stack.append(complex(elem))
		
		elif (elem[0:len(elem)-1:].isdigit() or isfloat(elem[0:len(elem)-1:])) and elem[len(elem)-1] == 'i':
			print(elem)
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
				act_rez = stack[len(stack)-2] + stack[len(stack)-1]
				SolutionStep.objects.create(problem_id=idp, n=n, formula=str(stack[len(stack)-2]) + " + " + str(stack[len(stack)-1]) + " = " + str(act_rez))
				stack[len(stack)-2] = act_rez
				stack.pop()
			elif elem == "-":
				act_rez = stack[len(stack)-2] - stack[len(stack)-1]
				SolutionStep.objects.create(problem_id=idp, n=n, formula=str(stack[len(stack)-2]) + " - " + str(stack[len(stack)-1]) + " = " + str(act_rez))
				stack[len(stack)-2] = act_rez
				stack.pop()
			elif elem == "*":
				act_rez = stack[len(stack)-2] * stack[len(stack)-1]
				SolutionStep.objects.create(problem_id=idp, n=n, formula=str(stack[len(stack)-2]) + " * " + str(stack[len(stack)-1]) + " = " + str(act_rez))
				stack[len(stack)-2] = act_rez
				stack.pop()
			elif elem == "/":
				act_rez = stack[len(stack)-2] / stack[len(stack)-1]
				SolutionStep.objects.create(problem_id=idp, n=n, formula=str(stack[len(stack)-2]) + " / " + str(stack[len(stack)-1]) + " = " + str(act_rez))
				stack[len(stack)-2] = act_rez
				stack.pop()
			elif elem == "^":
				act_rez = stack[len(stack)-2] ** stack[len(stack)-1]
				SolutionStep.objects.create(problem_id=idp, n=n, formula=str(stack[len(stack)-2]) + " ^ " + str(stack[len(stack)-1]) + " = " + str(act_rez))
				stack[len(stack)-2] = act_rez
				stack.pop()
				
			elif elem == "re":
				act_rez = complex(stack[len(stack)-1].real)
				SolutionStep.objects.create(problem_id=idp, n=n, formula="re(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
			elif elem == "im":
				act_rez = complex(stack[len(stack)-1].imag)
				SolutionStep.objects.create(problem_id=idp, n=n, formula="im(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
			elif elem == "conj":
				act_rez = complex(stack[len(stack)-1].conjugate())
				SolutionStep.objects.create(problem_id=idp, n=n, formula="conj(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
			
			elif elem == "arg":
				act_rez = cmath.phase(stack[len(stack)-1])
				SolutionStep.objects.create(problem_id=idp, n=n, formula="arg(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
			elif elem == "abs":
				act_rez = abs(stack[len(stack)-1])
				SolutionStep.objects.create(problem_id=idp, n=n, formula="abs(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
				
			elif elem == "exp":
				act_rez = cmath.exp(stack[len(stack)-1])
				SolutionStep.objects.create(problem_id=idp, n=n, formula="exp(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
			elif elem == "ln":
				act_rez = cmath.log(stack[len(stack)-1])
				SolutionStep.objects.create(problem_id=idp, n=n, formula="ln(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
			
			elif elem == "sin":
				act_rez = cmath.sin(stack[len(stack)-1])
				SolutionStep.objects.create(problem_id=idp, n=n, formula="sin(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
			elif elem == "cos":
				act_rez = cmath.cos(stack[len(stack)-1])
				SolutionStep.objects.create(problem_id=idp, n=n, formula="cos(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))	
				stack[len(stack)-1] = act_rez
			elif elem == "tg":
				act_rez = cmath.tan(stack[len(stack)-1])
				SolutionStep.objects.create(problem_id=idp, n=n, formula="tg(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
			elif elem == "ctg":
				act_rez = cmath.cos(stack[len(stack)-1]) / cmath.sin(stack[len(stack)-1]) # не ну а чо раз котангенса нема
				SolutionStep.objects.create(problem_id=idp, n=n, formula="ctg(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
			
			elif elem == "arcsin":
				act_rez = cmath.asin(stack[len(stack)-1])
				SolutionStep.objects.create(problem_id=idp, n=n, formula="arcsin(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
			elif elem == "arccos":
				act_rez = cmath.acos(stack[len(stack)-1])	
				SolutionStep.objects.create(problem_id=idp, n=n, formula="arccos(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
			elif elem == "arctg":
				act_rez = cmath.atan(stack[len(stack)-1])
				SolutionStep.objects.create(problem_id=idp, n=n, formula="arctg(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
			elif elem == "arсctg":
				act_rez = cmath.pi / 2 - cmath.atan(stack[len(stack)-1]) # опять, да
				SolutionStep.objects.create(problem_id=idp, n=n, formula="arсctg(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
				
			elif elem == "sh":
				act_rez = cmath.sinh(stack[len(stack)-1])
				SolutionStep.objects.create(problem_id=idp, n=n, formula="sh(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
			elif elem == "ch":
				act_rez = cmath.cosh(stack[len(stack)-1])	
				SolutionStep.objects.create(problem_id=idp, n=n, formula="ch(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
			elif elem == "th":
				act_rez = cmath.tanh(stack[len(stack)-1])
				SolutionStep.objects.create(problem_id=idp, n=n, formula="th(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
			elif elem == "cth":
				act_rez = cmath.cosh(stack[len(stack)-1]) / cmath.sinh(stack[len(stack)-1]) # не ну а чо раз котангенса нема
				SolutionStep.objects.create(problem_id=idp, n=n, formula="cth(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
				
			elif elem == "arsh":
				act_rez = cmath.asinh(stack[len(stack)-1])
				SolutionStep.objects.create(problem_id=idp, n=n, formula="arsh(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
			elif elem == "arch":
				act_rez = cmath.acosh(stack[len(stack)-1])	
				SolutionStep.objects.create(problem_id=idp, n=n, formula="arch(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
			elif elem == "arth":
				act_rez = cmath.atanh(stack[len(stack)-1])
				SolutionStep.objects.create(problem_id=idp, n=n, formula="arth(" + str(stack[len(stack)-1]) + ") = " + str(act_rez))
				stack[len(stack)-1] = act_rez
			n += 1
		print(stack)
	
	return str(stack[0])

A = 4
B = 10
C = 4
D = True
E = False

#1. Qual é o resultado da expressão abaixo? Avalie manualmente e depois confirme no interpretador Python.
print("1 - ", A == C)
#Resposta: True

#2. Qual é o resultado da expressão abaixo? Avalie manualmente e depois confirme no interpretador Python.
print("2 - ", B > A and B > C)
#Resposta: True

#3. Qual é o resultado da expressão abaixo? Avalie manualmente e depois confirme no interpretador Python.
print("3 - ", A != C or B == 10)
#Resposta: True

#4. Qual é o resultado da expressão abaixo? Avalie manualmente e depois confirme no interpretador Python.
print("4 - ", not D)
#Resposta: False

#5. Qual é o resultado da expressão abaixo? Avalie manualmente e depois confirme no interpretador Python.
print("5 - ", D and not E)
#Resposta: True

#6. Python permite encadear operadores relacionais como açúcar sintático. As duas expressões abaixo são equivalentes?
print("6.1 - ", A < B and B > C)
print("6.2 - ", A < B > C)
#resp1: Sim.
#Execute as duas no interpretador e compare os resultados. São equivalentes? Por quê?
#Elas são equivalentes porque o Python interpreta a expressão "A < B > C" é "A < B and B > C" em forma de símobolos matemáticos/encadeamento de operadores relacionais.

#7. Reescreva a expressão abaixo usando o açúcar sintático de encadeamento do Python (sem usar and):
#A >= 1 and A <= 10
print("7 -", 1 <= A <= 10)

#8. Qual é o resultado da expressão abaixo? Avalie manualmente respeitando a precedência de operadores e depois confirme no interpretador Python.
print("8 -", not E and A + 1 < B or D)
#Resposta: True

#9. Qual é o resultado da expressão abaixo? Avalie manualmente respeitando a precedência de operadores e depois confirme no interpretador Python.
print("9 -", not (E and A + 1 < B or D))
#Resposta: False

#10. Usando operadores lógicos e relacionais, escreva uma expressão em Python que resulte em True somente quando A for um número par e estiver entre 1 e 9 (inclusive). Use o açúcar sintático de encadeamento na parte da comparação de intervalo.
if A % 2 == 0 and 1 <= A <= 9:
	print("10 -", True)
else:
	print("10 -", False)

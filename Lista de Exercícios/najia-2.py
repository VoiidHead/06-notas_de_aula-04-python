A = 4
B = 10
C = 4
D = True
E = False
F = 0
G = -3
I = [1, 2, 3, 4, 5]

#11. Em Python, valores numéricos podem ser usados diretamente em contextos lógicos: 0 é considerado False e qualquer número diferente de zero é considerado True. Qual é o resultado das expressões abaixo?
#bool(F)
#bool(A)
#Resposta: Respectivamente, False e True.

#12. Usando os valores de F e A, avalie o resultado da expressão abaixo. Justifique levando em conta a interpretação lógica do valor 0.
#not F and A > 0
#Resposta: False, pois F = 0 e zero é interpretado como false, enquanto A > 0 é verdadeiro (True)

#12. Usando os valores de F e A, avalie o resultado da expressão abaixo. Justifique levando em conta a interpretação lógica do valor 0.
#not F and A > 0
#Resposta: True, pois F = 0 e zero é interpretado como false, enquanto A > 0 é verdadeiro (True)

#13. Avalie manualmente o resultado da expressão abaixo, passo a passo, e depois confirme no interpretador.
print("13 -", G < 0 and G > -10)
#Resposta: True, pois G é realmente menor que 0 e também é maior que -10.

#14. Reescreva a expressão da questão anterior usando o açúcar sintático de encadeamento do Python (sem usar and):
#G < 0 and G > -10
print("14 -", -10 < G < 0)

#15. Qual é o resultado da expressão abaixo? Identifique a ordem de avaliação respeitando a precedência dos operadores.
#A == C and B > A or not E
#Resposta: True, pois A == C é verdadeiro (True), B > A é verdadeiro (True) e not E é verdadeiro (True).
#..A expressão é avaliada da seguinte forma: (A == C and B > A) or not E -> (True and True) or True -> True or True -> True.

#16. A expressão abaixo tem resultado diferente da expressão da questão anterior? Avalie e explique o que muda com o uso dos parênteses.
#A == C and (B > A or not E)
#Resposta: O resultado é o mesmo da questão anterior (True). A expressão demtro dos parênteses é executada primeiro e logo depois, interpretada como um valor só (seu resultado, nesse caso, "True")

#17. Qual é o resultado da expressão abaixo? Avalie com cuidado e confirme no interpretador.
print("17 -", not (A == B) == (A != B))
#Resposta: True

#18. Python possui o operador in para verificar se um elemento pertence a uma sequência, e not in para o inverso. Qual é o resultado da expressão abaixo?
#A in I and B not in I
#Resposta: True

#19. Avalie o resultado passo a passo, respeitando a precedência dos operadores:
#not G < 0 or A >= C and B != 9
#Resposta: True, esse código seria lido como "falso ou erdadeiro e verdadeiro" e quando o computador vê "falso ou verdadeiro", ele entende como "verdadeiro"

#20
if A > C or B == 10 and G < 0 and E == False:
    print("20 -", True)
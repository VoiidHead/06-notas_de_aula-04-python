A = 4
B = 10
C = 4
D = True
E = False
F = 0
G = -3
I = [1, 2, 3, 4, 5]

#21. Em Python, os operadores and e or não retornam necessariamente True ou False — eles retornam um dos próprios operandos. Avalie cada expressão abaixo e explique por que o resultado é o que é:
#A and B
#Resposta: A saída é 10 (B). Isso acontece porque quando os dois operandos são verdadeiros, o último é impresso.
#E and A
#Resposta: A saída é False, pois A é verdadeiro e E é falso, considerando que estamos usando 'and', o computador interpreta isso como falso.
#D or B
#Resposta: A saída é True, porque tanto D quanto B são verdadeiros
#E or A
#Resposta: A saída é 4 (A), porque E é falso e A é verdadeiro, considerando que estamos usando 'or', o computador interpreta isso como verdadeiro.

#22. Usando F = 0, avalie as expressões abaixo e explique o comportamento (curto-circuito e valor retornado):
#F or A
#Resposta: A saída é 4 (A). Isso ocorre porque 'or' tem um curto-circuito. Ele avalia o primeiro operando (F) e, por ser falso, ele não avalia o segundo operando (A) e retorna o valor do segundo operando (A).
#F and A
#Resposta: A saída é 0 (F). Isso ocorre porque 'and' tem um curto-circuito. Ele avalia o primeiro operando (F) e, por ser falso, ele não avalia o segundo operando (A) e retorna o valor do primeiro operando (F).

#23. O padrão x and y or z era usado antigamente em Python como uma alternativa ao operador ternário y if x else z. Avalie a expressão abaixo com D = True e depois com D = False, e explique o que cada caso retorna:
#Observação: hoje a forma recomendada é 'B if D else A'. Teste ambas e compare os resultados.
print("23.1 -", D and A or B)
#Resposta: Com D = True, a saída é 4 (A). Isso acontece porque 'and' tem um curto-circuito. Ele avalia o primeiro operando (D) e, por ser verdadeiro, ele avalia o segundo operando (A) e retorna o valor do segundo operando (A). 
#Com D = False, a saída é 10 (B). Isso acontece porque 'and' tem um curto-circuito. Ele avalia o primeiro operando (D) e, por ser falso, ele não avalia o segundo operando (A) e retorna o valor do último operando (B).
print("23.2 -", B if D else A)
#Resposta: Ele responde de forma inversa ao anterior. Com D = True, a saída é 10 (B).
#Isso acontece porque a expressão 'B if D else A' avalia D e, por ser verdadeiro, retorna o valor de B.
#Com D = False, a saída é 4 (A). Isso acontece porque a expressão 'B if D else A' avalia D e, por ser falso, retorna o valor de A.

#24. Avalie a expressão abaixo e explique por que o resultado pode ser surpreendente:
#1 < 2 == True
#Resposta: A saída é False. Isso se dá em decorrência do computador ler isso como "1 < 2 and 2 == True", pelo fato de 1 não ser menor que 2, o resultado é falso.
#Isso pode surpreender porque matemáticamente, a expressão "1 < 2 == True" é verdadeira, mas nesse caso, com o 2 sendo comparado com o valor booleano True, o resultado é falso.

#25. Combine tudo que aprendeu e escreva uma única expressão que resulte em True somente quando todas as condições abaixo forem verdadeiras ao mesmo tempo:
#- A é par
#- B é maior que o dobro de A
#- G está no intervalo [-5, -1] (inclusive)
#- D é verdadeiro
#Use o açúcar sintático de encadeamento para a verificação do intervalo de G e organize a expressão de forma legível.

if A % 2 == 0 and B > (2 * A) and -1 > G > -5 and D == True:
    print("25 -", True)
else:
    print("25 -", False)
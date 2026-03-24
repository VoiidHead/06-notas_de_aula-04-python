# Lista de exercícios - Operadores lógicos e relacionais em Python

Considere que as variáveis abaixo estão definidas para todos os exercícios:

```python
A = 4
B = 10
C = 4
D = True
E = False
```

---

## Questões

**1.** Qual é o resultado da expressão abaixo? Avalie manualmente e depois confirme no interpretador Python.

```python
A == C
```

---

**2.** Qual é o resultado da expressão abaixo? Avalie manualmente e depois confirme no interpretador Python.

```python
B > A and B > C
```

---

**3.** Qual é o resultado da expressão abaixo? Avalie manualmente e depois confirme no interpretador Python.

```python
A != C or B == 10
```

---

**4.** Qual é o resultado da expressão abaixo? Avalie manualmente e depois confirme no interpretador Python.

```python
not D
```

---

**5.** Qual é o resultado da expressão abaixo? Avalie manualmente e depois confirme no interpretador Python.

```python
D and not E
```

---

**6.** Python permite encadear operadores relacionais como açúcar sintático. As duas expressões abaixo são equivalentes?

```python
A < B and B > C
A < B > C
```

Execute as duas no interpretador e compare os resultados. São equivalentes? Por quê?

---

**7.** Reescreva a expressão abaixo usando o açúcar sintático de encadeamento do Python (sem usar `and`):

```python
A >= 1 and A <= 10
```

---

**8.** Qual é o resultado da expressão abaixo? Avalie manualmente respeitando a precedência de operadores e depois confirme no interpretador Python.

```python
not E and A + 1 < B or D
```

---

**9.** Qual é o resultado da expressão abaixo? Avalie manualmente respeitando a precedência de operadores e depois confirme no interpretador Python.

```python
not (E and A + 1 < B or D)
```

---

**10.** Usando operadores lógicos e relacionais, escreva uma expressão em Python que resulte em `True` somente quando `A` for um número par **e** estiver entre 1 e 9 (inclusive). Use o açúcar sintático de encadeamento na parte da comparação de intervalo.

> **Dica**: um número é par quando o resto da divisão por 2 é igual a zero (`A % 2 == 0`).

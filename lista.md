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

---

## Questões intermediárias

Para as questões a seguir, considere as variáveis adicionais abaixo além das já definidas:

```python
F = 0
G = -3
I = [1, 2, 3, 4, 5]
```

---

**11.** Em Python, valores numéricos podem ser usados diretamente em contextos lógicos: `0` é considerado `False` e qualquer número diferente de zero é considerado `True`. Qual é o resultado das expressões abaixo?

```python
bool(F)
bool(A)
```

---

**12.** Usando os valores de `F` e `A`, avalie o resultado da expressão abaixo. Justifique levando em conta a interpretação lógica do valor `0`.

```python
not F and A > 0
```

---

**13.** Avalie manualmente o resultado da expressão abaixo, passo a passo, e depois confirme no interpretador.

```python
G < 0 and G > -10
```

---

**14.** Reescreva a expressão da questão anterior usando o açúcar sintático de encadeamento do Python (sem usar `and`):

```python
G < 0 and G > -10
```

---

**15.** Qual é o resultado da expressão abaixo? Identifique a ordem de avaliação respeitando a precedência dos operadores.

```python
A == C and B > A or not E
```

---

**16.** A expressão abaixo tem resultado diferente da expressão da questão anterior? Avalie e explique o que muda com o uso dos parênteses.

```python
A == C and (B > A or not E)
```

---

**17.** Qual é o resultado da expressão abaixo? Avalie com cuidado e confirme no interpretador.

```python
not (A == B) == (A != B)
```

---

**18.** Python possui o operador `in` para verificar se um elemento pertence a uma sequência, e `not in` para o inverso. Qual é o resultado da expressão abaixo?

```python
A in I and B not in I
```

---

**19.** Avalie o resultado passo a passo, respeitando a precedência dos operadores:

```python
not G < 0 or A >= C and B != 9
```

---

**20.** Escreva uma expressão Python que resulte em `True` somente quando **todas** as condições abaixo forem satisfeitas ao mesmo tempo:

- `A` é maior que `C`  ou  `B` é igual a `10`
- `G` é negativo
- `E` é `False`

---

## Questões avançadas

---

**21.** Em Python, os operadores `and` e `or` não retornam necessariamente `True` ou `False` — eles retornam um dos próprios operandos. Avalie cada expressão abaixo e explique por que o resultado é o que é:

```python
A and B
E and A
D or B
E or A
```

---

**22.** Usando `F = 0`, avalie as expressões abaixo e explique o comportamento (curto-circuito e valor retornado):

```python
F or A
F and A
```

---

**23.** O padrão `x and y or z` era usado antigamente em Python como uma alternativa ao operador ternário `y if x else z`. Avalie a expressão abaixo com `D = True` e depois com `D = False`, e explique o que cada caso retorna:

```python
D and B or A
```

> **Observação**: hoje a forma recomendada é `B if D else A`. Teste ambas e compare os resultados.

---

**24.** Avalie a expressão abaixo e explique por que o resultado pode ser surpreendente:

```python
1 < 2 == True
```

> **Dica**: `True` é igual a `1` em Python (`True == 1` resulta em `True`). O encadeamento `1 < 2 == True` é avaliado como `1 < 2 and 2 == True`. O que vale `2 == True`?

---

**25.** Combine tudo que aprendeu e escreva **uma única expressão** que resulte em `True` somente quando **todas** as condições abaixo forem verdadeiras ao mesmo tempo:

- `A` é par
- `B` é maior que o dobro de `A`
- `G` está no intervalo `[-5, -1]` (inclusive)
- `D` é verdadeiro

Use o açúcar sintático de encadeamento para a verificação do intervalo de `G` e organize a expressão de forma legível.

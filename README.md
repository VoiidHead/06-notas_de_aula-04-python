# Notas de aula de 2026.1.06 - Python 04

## Informações gerais

- **Público alvo**: alunos da disciplina de **Introdução a lógica e programação** do curso de [Infoweb (Técnico Integrado em Informática para Internet)](https://diatinf.ifrn.edu.br/cursos/tecnico-em-informatica-para-internet/) na [DIATINF (Diretoria Acadêmica de Gestão e Tecnologia da Informação)](https://diatinf.ifrn.edu.br/) no [CNAT-IFRN (Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte - Campus Natal-Central)](https://portal.ifrn.edu.br/campus/natalcentral/)
- **Professor**: [L A Minora](https://github.com/leonardo-minora/)
- **Objetivo**:
  1. Conhecer os operadores lógicos e relacionais

---
## Notas de aula [slides pdf](/04-Operadores_Lógicos_e_Relacionais.pdf)
1. Tipo de dado lógico `bool` tem 2 possíveis valores `True` e `False`
2. **Operadores relacionais** compara 2 valores e resulta num valor do tipo `bool`.
   - **maior** : operador `>` - exemplo `5 > 5` resulta em `False`
   - **maior ou igual** : operador `>=` - exemplo `5 >= 5` resulta em `True`
   - **menor** : operador `<=` - exemplo `5 < 3` resulta em `False`
   - **menor ou igual** : operador `<=` - exemplo `1 < 3` resulta em `True`
   - **igualdade** : operador `==` - exemplo `5 == 3` resulta em `False`
   - **diferença** : operador `!=` - exemplo `5 != 3` resulta em `True`
3. **Operadores lógicos** encadeiam avaliação de valores lógicos e resultam em 1 valor lógico
   - **e** : operador `and` tem o resultado como `True` se todos os valores são `True` - exemplos:
     - `True and True` resulta em `True`
     - `True and False` resulta em `False`
     - `True and True and False` resulta em `False`
   - **ou** : operador `or` tem o resultado como `True` se pelo menos um dos valores for `True` - exemplos:
     - `True or True` resulta em `True`
     - `True or False` resulta em `True`
     - `True or True or False` resulta em `True`
   - **negação** : operador `not` tem o resultado trocado - exemplos:
     - `not True` resulta em `False`
     - `not False` resulta em `True`
     - `not (True or True or False)` resulta em `False`
4. **Precedência de operadores** define a ordem de qual operação matemática ou lógica deve ser avaliada (executada) dentro de uma mesma linha de código. Em python a ordem é definida abaixo
   1. `( )`
   2. `**`
   3. `*`, `/`, `//`, `%`
   4. `+`, `-`
   5. `==`, `!=`, `>`, `>=`, `<`, `<=`
   6. `not`
   7. `and`
   8. `or`
5. **Açucar sintático** do python para **encadeamento**
   - no lugar de `x < y and y < z` use `x < y < z`
   - no lugar de `x >= y and y >= z` use `x >= y >= z`

---
## Exercícios
[Lista de exercícios](/lista.md)

[Respostas dos Exercícios do PDF](/tararaterere.txt)

Respostas da lista de exercícios: [Parte 1](https://github.com/VoiidHead/06-notas_de_aula-04-python/blob/main/Lista%20de%20Exerc%C3%ADcios/najia-1.py)
[Parte 2](https://github.com/VoiidHead/06-notas_de_aula-04-python/blob/main/Lista%20de%20Exerc%C3%ADcios/najia-2.py)
[Parte 3](https://github.com/VoiidHead/06-notas_de_aula-04-python/blob/main/Lista%20de%20Exerc%C3%ADcios/najia-3.py)
1. Tente avaliar os resultados de cada uma das expressões a seguir. Considere que as variáveis A, B e C armazenam respectivamente os valores 2, 7 e False. Caso não consiga, use o interpretador de comandos python para avaliar o resultado.
   - `B == A * 2`
   - `B > A + 5`
   - `B > A or B == A`
   - `C and B / A == 3.5`
   - `not C and C`
   - `B >= 0 and B < 5`
   - `A < 0 or A >= 1`
   - `A % 2 != 0`
   - `True or C and A + 1 < B`
   - `(True or C) and A + 1 < B`


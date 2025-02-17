# [Linux] Bash expr Uso equivalente: Avaliação de expressões

## Overview
O comando `expr` é utilizado no Bash para avaliar expressões aritméticas, lógicas e de string. Ele pode realizar operações matemáticas simples, comparar valores e manipular strings, tornando-se uma ferramenta útil em scripts de shell.

## Usage
A sintaxe básica do comando `expr` é a seguinte:

```bash
expr [opções] [argumentos]
```

## Common Options
- `-e`: Permite a avaliação de expressões com precedência de operadores.
- `length`: Retorna o comprimento de uma string.
- `index`: Retorna a posição da primeira ocorrência de uma substring em uma string.
- `match`: Verifica se uma string corresponde a uma expressão regular.

## Common Examples

### Exemplo 1: Avaliação Aritmética
Para realizar uma soma simples:

```bash
expr 5 + 3
```
Saída:
```
8
```

### Exemplo 2: Comparação de Números
Para verificar se um número é maior que outro:

```bash
expr 10 \> 5
```
Saída:
```
1
```
(1 indica verdadeiro)

### Exemplo 3: Comprimento de uma String
Para obter o comprimento de uma string:

```bash
expr length "Olá, Mundo!"
```
Saída:
```
12
```

### Exemplo 4: Índice de uma Substring
Para encontrar a posição da letra "M" na string:

```bash
expr index "Olá, Mundo!" M
```
Saída:
```
7
```

### Exemplo 5: Verificação de Correspondência
Para verificar se uma string contém um padrão:

```bash
expr "Bash é incrível!" : '.*incrível.*'
```
Saída:
```
17
```
(17 indica que a correspondência começa na posição 17)

## Tips
- Sempre escape operadores como `+`, `-`, `*`, e `/` com uma barra invertida (`\`) para evitar que o Bash os interprete como operadores de shell.
- Use `expr` em scripts onde a simplicidade é necessária, mas considere outras ferramentas como `bc` para operações matemáticas mais complexas.
- Lembre-se de que `expr` retorna 0 para verdadeiro e 1 para falso em comparações, o que pode ser útil em estruturas condicionais.
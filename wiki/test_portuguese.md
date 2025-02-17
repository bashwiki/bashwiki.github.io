# [Linux] Bash test uso: Avalia expressões verdadeiras ou falsas

## Overview
O comando `test` é utilizado no Bash para avaliar expressões e determinar se elas são verdadeiras ou falsas. Ele é frequentemente usado em scripts para tomar decisões baseadas em condições, como verificar a existência de arquivos, comparar valores e muito mais.

## Usage
A sintaxe básica do comando `test` é a seguinte:

```bash
test [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `test`:

- `-e arquivo`: Verifica se o arquivo existe.
- `-f arquivo`: Verifica se o arquivo é um arquivo regular.
- `-d diretório`: Verifica se o diretório existe.
- `-z string`: Verifica se a string é vazia.
- `-n string`: Verifica se a string não é vazia.
- `string1 = string2`: Compara se duas strings são iguais.
- `int1 -eq int2`: Compara se dois inteiros são iguais.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `test`:

### Verificar se um arquivo existe
```bash
test -e arquivo.txt && echo "O arquivo existe."
```

### Verificar se um diretório existe
```bash
test -d /caminho/para/diretorio && echo "O diretório existe."
```

### Comparar duas strings
```bash
string1="hello"
string2="hello"
test "$string1" = "$string2" && echo "As strings são iguais."
```

### Verificar se uma variável está vazia
```bash
variavel=""
test -z "$variavel" && echo "A variável está vazia."
```

### Comparar dois números
```bash
num1=10
num2=20
test "$num1" -lt "$num2" && echo "$num1 é menor que $num2."
```

## Tips
- Utilize `[` como uma alternativa ao `test`, pois eles são funcionalmente equivalentes. Por exemplo, `[` é um comando que pode ser usado da mesma forma que `test`.
- Sempre coloque variáveis entre aspas para evitar erros com espaços em branco ou strings vazias.
- Combine o uso de `test` com estruturas de controle como `if` para criar scripts mais robustos. Por exemplo:

```bash
if test -e arquivo.txt; then
    echo "O arquivo existe."
else
    echo "O arquivo não existe."
fi
```
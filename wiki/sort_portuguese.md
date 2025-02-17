# [Linux] Bash sort uso: Ordenar linhas de texto

## Overview
O comando `sort` é utilizado para ordenar linhas de texto em arquivos ou na entrada padrão. Ele organiza as linhas em ordem alfabética ou numérica, facilitando a análise e a visualização de dados.

## Usage
A sintaxe básica do comando `sort` é a seguinte:

```
sort [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `sort`:

- `-n`: Ordena numericamente.
- `-r`: Inverte a ordem de classificação (ordem decrescente).
- `-k`: Especifica a coluna a ser usada para a ordenação.
- `-u`: Remove linhas duplicadas.
- `-o`: Escreve a saída em um arquivo especificado.

## Common Examples

### Exemplo 1: Ordenar um arquivo
Para ordenar um arquivo chamado `lista.txt` em ordem alfabética, use:

```bash
sort lista.txt
```

### Exemplo 2: Ordenar numericamente
Para ordenar um arquivo chamado `numeros.txt` que contém números, use:

```bash
sort -n numeros.txt
```

### Exemplo 3: Ordenar em ordem decrescente
Para ordenar um arquivo chamado `nomes.txt` em ordem decrescente, use:

```bash
sort -r nomes.txt
```

### Exemplo 4: Ordenar por uma coluna específica
Se você tiver um arquivo `dados.txt` com várias colunas e quiser ordenar pela segunda coluna, use:

```bash
sort -k2 dados.txt
```

### Exemplo 5: Remover duplicatas
Para ordenar um arquivo e remover linhas duplicadas, use:

```bash
sort -u lista.txt
```

### Exemplo 6: Salvar a saída em um arquivo
Para salvar a saída ordenada em um novo arquivo chamado `ordenado.txt`, use:

```bash
sort lista.txt -o ordenado.txt
```

## Tips
- Sempre verifique se o arquivo de entrada está no formato correto para evitar resultados inesperados.
- Combine `sort` com outros comandos, como `uniq`, para manipulações de dados mais complexas.
- Utilize a opção `-k` para ordenar por colunas específicas em arquivos delimitados, como CSV.
- Experimente usar `sort` em conjunto com `grep` para filtrar e ordenar dados ao mesmo tempo.
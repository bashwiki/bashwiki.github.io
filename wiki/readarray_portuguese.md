# [Linux] Bash readarray Uso: Lê linhas de um arquivo em um array

## Overview
O comando `readarray` é utilizado em Bash para ler linhas de um arquivo e armazená-las em um array. Isso é especialmente útil quando você precisa manipular ou processar dados linha por linha.

## Usage
A sintaxe básica do comando `readarray` é a seguinte:

```bash
readarray [opções] [nome_do_array]
```

## Common Options
- `-t`: Remove a nova linha do final de cada linha lida.
- `-n N`: Lê apenas as primeiras N linhas do arquivo.
- `-s N`: Ignora as primeiras N linhas do arquivo.

## Common Examples

### Exemplo 1: Ler um arquivo em um array
```bash
readarray linhas < arquivo.txt
```
Neste exemplo, todas as linhas do `arquivo.txt` são lidas e armazenadas no array `linhas`.

### Exemplo 2: Ler um arquivo e remover novas linhas
```bash
readarray -t linhas < arquivo.txt
```
Aqui, as linhas do `arquivo.txt` são lidas e armazenadas no array `linhas`, mas sem as novas linhas no final.

### Exemplo 3: Ler apenas as primeiras 5 linhas
```bash
readarray -n 5 linhas < arquivo.txt
```
Este comando lê apenas as primeiras 5 linhas do `arquivo.txt` e as armazena no array `linhas`.

### Exemplo 4: Ignorar as primeiras 2 linhas
```bash
readarray -s 2 linhas < arquivo.txt
```
Neste caso, as duas primeiras linhas do `arquivo.txt` são ignoradas, e as linhas subsequentes são armazenadas no array `linhas`.

## Tips
- Sempre use a opção `-t` se você não precisar das novas linhas, pois isso facilita o processamento posterior dos dados.
- Verifique se o arquivo que você está tentando ler existe e tem permissões adequadas para evitar erros.
- Experimente usar `declare -p` para visualizar o conteúdo do array após a leitura, facilitando a depuração.
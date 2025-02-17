# [Linux] Bash mapfile Uso: Lê linhas de um arquivo em um array

## Overview
O comando `mapfile` é utilizado no Bash para ler linhas de um arquivo e armazená-las em um array. Isso é útil quando você precisa manipular ou processar dados linha por linha de forma eficiente.

## Usage
A sintaxe básica do comando `mapfile` é a seguinte:

```bash
mapfile [opções] [argumentos]
```

## Common Options
- `-t`: Remove a nova linha do final de cada linha lida.
- `-n <n>`: Lê no máximo `<n>` linhas do arquivo.
- `-O <n>`: Define o índice inicial do array onde as linhas serão armazenadas.

## Common Examples

### Exemplo 1: Ler um arquivo em um array
```bash
mapfile linhas < arquivo.txt
```
Neste exemplo, todas as linhas do `arquivo.txt` são lidas e armazenadas no array `linhas`.

### Exemplo 2: Remover novas linhas
```bash
mapfile -t linhas < arquivo.txt
```
Aqui, as linhas do `arquivo.txt` são lidas e armazenadas no array `linhas`, mas sem as novas linhas no final.

### Exemplo 3: Ler um número específico de linhas
```bash
mapfile -n 5 linhas < arquivo.txt
```
Este comando lê apenas as primeiras 5 linhas do `arquivo.txt` e as armazena no array `linhas`.

### Exemplo 4: Definir o índice inicial do array
```bash
mapfile -O 1 linhas < arquivo.txt
```
Neste caso, as linhas do `arquivo.txt` são armazenadas no array `linhas`, começando a partir do índice 1.

## Tips
- Sempre use a opção `-t` se você não precisar das novas linhas, pois isso pode evitar problemas ao processar os dados.
- Verifique o tamanho do array após a leitura usando `${#linhas[@]}` para garantir que você leu o número esperado de linhas.
- Combine `mapfile` com outros comandos como `grep` ou `awk` para filtrar ou processar dados antes de armazená-los no array.
# [리눅스] Bash mapfile 사용법

## Overview
O comando `mapfile`, também conhecido como `readarray`, é uma ferramenta do Bash que permite ler linhas de um arquivo ou da entrada padrão e armazená-las em um array. O principal propósito do `mapfile` é facilitar a manipulação de dados em formato de linha, permitindo que os desenvolvedores e engenheiros processem rapidamente informações sem a necessidade de loops complexos.

## Usage
A sintaxe básica do comando `mapfile` é a seguinte:

```bash
mapfile [opções] [nome_do_array]
```

### Opções Comuns:
- `-t`: Remove a nova linha no final de cada linha lida, armazenando apenas o conteúdo.
- `-n N`: Lê até N linhas, onde N é um número inteiro.
- `-O N`: Define o índice inicial do array para N.
- `-s N`: Ignora as primeiras N linhas do arquivo ou da entrada.

## Examples

### Exemplo 1: Ler um arquivo em um array
Suponha que você tenha um arquivo chamado `dados.txt` com o seguinte conteúdo:

```
linha 1
linha 2
linha 3
```

Você pode usar o `mapfile` para ler essas linhas em um array chamado `linhas`:

```bash
mapfile linhas < dados.txt
echo "${linhas[@]}"
```

Isso irá imprimir:

```
linha 1 linha 2 linha 3
```

### Exemplo 2: Usar opções para manipulação
Se você quiser ler apenas as duas primeiras linhas do arquivo e remover as quebras de linha, você pode fazer o seguinte:

```bash
mapfile -t -n 2 linhas < dados.txt
echo "${linhas[@]}"
```

A saída será:

```
linha 1 linha 2
```

## Tips
- Utilize a opção `-t` para evitar que quebras de linha indesejadas sejam incluídas nos elementos do array.
- Combine `mapfile` com outros comandos do Bash, como `grep` ou `awk`, para filtrar ou processar dados antes de armazená-los no array.
- Lembre-se de que o `mapfile` pode ler da entrada padrão, permitindo que você redirecione a saída de outros comandos diretamente para ele.

Com essas informações, você deve estar apto a utilizar o comando `mapfile` de forma eficaz em seus scripts Bash.
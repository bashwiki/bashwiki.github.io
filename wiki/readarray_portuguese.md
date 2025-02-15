# [리눅스] Bash readarray 사용법

## Overview
O comando `readarray` (ou `mapfile`) é uma ferramenta do Bash que permite ler linhas de um arquivo ou da entrada padrão e armazená-las em um array. Este comando é especialmente útil quando você precisa manipular dados linha por linha, como processar arquivos de texto ou capturar saídas de comandos.

## Usage
A sintaxe básica do comando `readarray` é a seguinte:

```bash
readarray [opções] array_name
```

### Opções Comuns:
- `-t`: Remove a nova linha (`\n`) do final de cada linha lida, evitando que as entradas do array tenham quebras de linha indesejadas.
- `-n`: Lê apenas as primeiras N linhas do arquivo ou da entrada padrão.
- `-s`: Ignora as primeiras N linhas do arquivo ou da entrada padrão.
- `-d delim`: Define um delimitador personalizado para separar as entradas.

## Examples

### Exemplo 1: Ler um arquivo em um array
Suponha que você tenha um arquivo chamado `lista.txt` com o seguinte conteúdo:

```
linha1
linha2
linha3
```

Você pode usar o `readarray` para ler esse arquivo em um array:

```bash
readarray linhas < lista.txt
echo "${linhas[@]}"
```

Este comando irá armazenar cada linha do arquivo `lista.txt` em um elemento do array `linhas` e, em seguida, imprimir todas as linhas.

### Exemplo 2: Ler a saída de um comando
Você também pode usar `readarray` para capturar a saída de um comando. Por exemplo, para armazenar a lista de arquivos em um diretório:

```bash
readarray -t arquivos < <(ls)
echo "${arquivos[@]}"
```

Neste caso, `ls` lista os arquivos do diretório atual, e `readarray` armazena cada nome de arquivo em um elemento do array `arquivos`.

## Tips
- Sempre use a opção `-t` se você não quiser que as quebras de linha sejam incluídas nos elementos do array.
- Para depuração, você pode usar `printf '%s\n' "${array_name[@]}"` para visualizar o conteúdo do array de forma clara.
- Considere usar `readarray` em scripts onde você precisa processar dados de forma eficiente, especialmente ao lidar com grandes volumes de dados.

Com essas informações, você agora pode utilizar o comando `readarray` de forma eficaz em seus scripts Bash!
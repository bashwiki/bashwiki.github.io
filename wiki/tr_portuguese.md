# [리눅스] Bash tr 사용법

## Overview
O comando `tr` (translate) é uma ferramenta do Unix/Linux utilizada para traduzir ou deletar caracteres de uma entrada padrão. Ele é frequentemente usado para manipular texto, permitindo que os desenvolvedores realizem operações como a substituição de caracteres, a remoção de espaços em branco, e a conversão de letras maiúsculas para minúsculas, entre outras funcionalidades. O `tr` é especialmente útil em scripts de shell e em pipelines de processamento de texto.

## Usage
A sintaxe básica do comando `tr` é a seguinte:

```bash
tr [opções] SET1 [SET2]
```

### Opções Comuns:
- `-d`: Deleta os caracteres especificados em SET1.
- `-s`: Substitui sequências de caracteres repetidos por um único caractere.
- `-c`: Complementa SET1, ou seja, opera sobre todos os caracteres que não estão em SET1.
- `-t`: Limita a tradução a um conjunto de caracteres.

## Examples

### Exemplo 1: Substituição de caracteres
Para substituir todas as letras minúsculas "a" por "b" em um texto, você pode usar:

```bash
echo "banana" | tr 'a' 'b'
```
Saída:
```
bbnbnb
```

### Exemplo 2: Remoção de espaços em branco
Para remover todos os espaços em branco de uma string, você pode usar:

```bash
echo "Olá Mundo" | tr -d ' '
```
Saída:
```
OláMundo
```

## Tips
- O `tr` opera apenas em caracteres e não em strings, portanto, tenha cuidado ao usar conjuntos de caracteres.
- Combine `tr` com outros comandos, como `grep` ou `awk`, para criar pipelines poderosos que manipulam e filtram texto de forma eficiente.
- Lembre-se de que `tr` não altera o arquivo original; ele apenas imprime a saída no terminal. Para salvar a saída em um arquivo, você pode redirecionar a saída usando `>`.

Utilizar o `tr` de forma eficaz pode simplificar muitas tarefas de manipulação de texto em scripts e na linha de comando.
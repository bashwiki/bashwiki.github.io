# [Linux] Bash readonly uso: Define variáveis como somente leitura

## Overview
O comando `readonly` no Bash é utilizado para marcar variáveis como somente leitura. Isso significa que, uma vez que uma variável é definida como readonly, seu valor não pode ser alterado ou removido durante a execução do script ou da sessão do terminal.

## Usage
A sintaxe básica do comando `readonly` é a seguinte:

```bash
readonly [opções] [variáveis]
```

## Common Options
O comando `readonly` não possui muitas opções, mas aqui estão algumas que podem ser úteis:

- `-p`: Exibe uma lista de todas as variáveis que estão marcadas como somente leitura.

## Common Examples

### Exemplo 1: Definindo uma variável como somente leitura
```bash
my_var="Hello, World!"
readonly my_var
```
Neste exemplo, `my_var` é definida como somente leitura. Qualquer tentativa de alterar seu valor resultará em um erro.

### Exemplo 2: Tentando modificar uma variável readonly
```bash
my_var="Hello, World!"
readonly my_var
my_var="New Value"  # Isso causará um erro
```
Aqui, a tentativa de modificar `my_var` após defini-la como readonly resultará em uma mensagem de erro.

### Exemplo 3: Listando variáveis somente leitura
```bash
readonly -p
```
Este comando exibirá todas as variáveis que estão marcadas como somente leitura na sessão atual.

## Tips
- Use `readonly` para proteger variáveis que não devem ser alteradas acidentalmente, especialmente em scripts complexos.
- Lembre-se de que variáveis de ambiente também podem ser definidas como readonly, garantindo que não sejam modificadas durante a execução do script.
- Para remover a proteção de uma variável readonly, você precisará redefini-la sem a palavra-chave `readonly`, mas isso só é possível se você não estiver em um contexto onde a variável já foi definida como readonly.
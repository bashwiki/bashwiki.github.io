# [리눅스] Bash typeset 사용법

## Overview
O comando `typeset` é utilizado em scripts Bash para declarar variáveis e definir suas propriedades. Ele permite que você especifique atributos para variáveis, como se são somente leitura, arrays ou inteiros. O principal objetivo do `typeset` é fornecer um controle mais rigoroso sobre como as variáveis são tratadas dentro de um script, ajudando a evitar erros e a melhorar a legibilidade do código.

## Usage
A sintaxe básica do comando `typeset` é a seguinte:

```bash
typeset [opções] nome_variável
```

### Opções Comuns:
- `-r`: Define a variável como somente leitura. Uma vez atribuída, não pode ser alterada.
- `-i`: Trata a variável como um número inteiro. Qualquer valor atribuído será convertido para um inteiro.
- `-a`: Declara a variável como um array.
- `-x`: Exporta a variável para o ambiente do shell, tornando-a disponível para subprocessos.
- `-p`: Exibe as variáveis e seus atributos.

## Examples
### Exemplo 1: Declarar uma variável somente leitura
```bash
typeset -r VAR_IMUTAVEL="Não pode ser alterado"
echo $VAR_IMUTAVEL
# Saída: Não pode ser alterado
# Tentar alterar a variável resultará em erro
```

### Exemplo 2: Declarar um array e um inteiro
```bash
typeset -a MEU_ARRAY
MEU_ARRAY=(um dois três)

typeset -i NUMERO_INTEIRO=10
NUMERO_INTEIRO+=5  # O valor agora será 15

echo "Array: ${MEU_ARRAY[@]}"
echo "Número Inteiro: $NUMERO_INTEIRO"
# Saída: Array: um dois três
# Saída: Número Inteiro: 15
```

## Tips
- Utilize `typeset` para garantir que suas variáveis tenham o tipo correto, especialmente em scripts complexos onde a manipulação de dados é crítica.
- Considere usar `-r` para variáveis que não devem ser alteradas após a inicialização, ajudando a evitar bugs.
- Lembre-se de que `typeset` é uma construção específica do Bash e pode não estar disponível em outros shells, como o Dash ou o Sh. Portanto, use-o em scripts que você sabe que serão executados em um ambiente Bash.
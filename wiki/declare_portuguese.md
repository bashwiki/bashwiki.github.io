# [리눅스] Bash declare 사용법

## Overview
O comando `declare` no Bash é utilizado para declarar variáveis e suas propriedades. Ele permite que os desenvolvedores especifiquem características de variáveis, como se são arrays, se são somente leitura, se são inteiros, entre outras opções. Isso é útil para garantir que as variáveis se comportem conforme esperado durante a execução de scripts.

## Usage
A sintaxe básica do comando `declare` é a seguinte:

```bash
declare [opções] [nome_variável]
```

### Opções Comuns
- `-a`: Declara uma variável como um array.
- `-i`: Declara uma variável como um inteiro, permitindo operações aritméticas.
- `-r`: Declara uma variável como somente leitura, impedindo que seu valor seja alterado.
- `-x`: Exporta a variável para o ambiente, tornando-a disponível para subprocessos.
- `-p`: Exibe as variáveis e suas propriedades.

## Examples

### Exemplo 1: Declarar um Array
```bash
declare -a frutas
frutas=("maçã" "banana" "laranja")
echo "${frutas[1]}"  # Saída: banana
```
Neste exemplo, declaramos uma variável `frutas` como um array e atribuímos três valores a ela. Em seguida, exibimos o segundo elemento do array.

### Exemplo 2: Variável Somente Leitura
```bash
declare -r PI=3.14
echo $PI  # Saída: 3.14
# PI=3.14159  # Isso resultará em um erro, pois PI é somente leitura.
```
Aqui, a variável `PI` é declarada como somente leitura. Qualquer tentativa de alterar seu valor resultará em um erro.

## Tips
- Utilize `declare` para garantir que suas variáveis tenham o tipo correto, especialmente em scripts complexos onde a manipulação de dados é crítica.
- Sempre que possível, use a opção `-r` para variáveis que não devem ser alteradas após a inicialização, isso ajuda a evitar bugs.
- Use `declare -p` para depurar e verificar o estado das variáveis em seu script, o que pode ser útil durante o desenvolvimento.

Compreender e utilizar o comando `declare` pode melhorar significativamente a robustez e a legibilidade de seus scripts Bash.
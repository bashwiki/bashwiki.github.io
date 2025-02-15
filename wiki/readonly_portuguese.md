# [리눅스] Bash readonly 사용법

## Overview
O comando `readonly` no Bash é utilizado para marcar variáveis como somente leitura. Uma vez que uma variável é definida como readonly, seu valor não pode ser alterado ou removido durante a execução do script ou da sessão do terminal. Isso é útil para proteger valores que não devem ser modificados acidentalmente, garantindo a integridade dos dados em scripts e aplicações.

## Usage
A sintaxe básica do comando `readonly` é a seguinte:

```bash
readonly NOME_VARIAVEL=valor
```

Você também pode usar o comando `readonly` sem atribuir um valor, apenas para tornar uma variável existente como somente leitura:

```bash
readonly NOME_VARIAVEL
```

### Opções Comuns
- `-p`: Esta opção exibe uma lista de todas as variáveis que estão marcadas como somente leitura no ambiente atual.

## Examples
### Exemplo 1: Definindo uma variável como somente leitura
```bash
readonly MEU_NOME="João"
echo $MEU_NOME  # Saída: João
MEU_NOME="Maria"  # Isso resultará em um erro
```

Neste exemplo, a variável `MEU_NOME` é definida como somente leitura. Tentar alterar seu valor resultará em um erro.

### Exemplo 2: Listando variáveis somente leitura
```bash
readonly VAR1="Valor1"
readonly VAR2="Valor2"
readonly -p  # Saída: declare -r VAR1="Valor1"; declare -r VAR2="Valor2"
```

Aqui, duas variáveis são definidas como somente leitura e, em seguida, a opção `-p` é usada para listar todas as variáveis somente leitura no ambiente atual.

## Tips
- Utilize `readonly` para proteger variáveis que contêm configurações críticas ou constantes que não devem ser alteradas durante a execução do script.
- Lembre-se de que uma vez que uma variável é marcada como somente leitura, você não poderá alterá-la ou removê-la. Portanto, use essa funcionalidade com cautela.
- Para verificar se uma variável é somente leitura, você pode tentar reatribuir um valor a ela. Se a variável for readonly, você receberá um erro informando que a variável não pode ser modificada.
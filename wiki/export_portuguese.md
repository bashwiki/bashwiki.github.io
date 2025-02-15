# [리눅스] Bash export 사용법

## Overview
O comando `export` no Bash é utilizado para definir variáveis de ambiente que estarão disponíveis para processos filhos. Isso significa que, ao usar `export`, você pode tornar uma variável acessível para qualquer programa ou script que seja executado a partir do shell atual. O principal propósito do `export` é facilitar a comunicação de informações entre diferentes processos.

## Usage
A sintaxe básica do comando `export` é a seguinte:

```bash
export NOME_VARIAVEL=valor
```

- `NOME_VARIAVEL`: O nome da variável que você deseja criar ou modificar.
- `valor`: O valor que você deseja atribuir à variável.

Você também pode usar `export` sem argumentos para listar todas as variáveis de ambiente atualmente exportadas:

```bash
export
```

## Examples
### Exemplo 1: Definindo uma variável de ambiente
```bash
export MEU_CAMINHO="/usr/local/bin"
```
Neste exemplo, a variável `MEU_CAMINHO` é criada e exportada, tornando-se disponível para qualquer processo filho que seja iniciado a partir deste shell.

### Exemplo 2: Usando uma variável de ambiente em um comando
```bash
export NOME="João"
echo "Olá, $NOME!"
```
Aqui, a variável `NOME` é definida e, em seguida, utilizada no comando `echo`, que imprime "Olá, João!" no terminal.

## Tips
- Sempre use letras maiúsculas para nomes de variáveis de ambiente, pois é uma convenção comum e ajuda a distinguir variáveis de ambiente de variáveis locais.
- Para remover uma variável de ambiente exportada, você pode usar o comando `unset`:
  ```bash
  unset NOME_VARIAVEL
  ```
- Lembre-se de que as variáveis definidas com `export` só estarão disponíveis para processos filhos que são iniciados após a definição da variável. Se você precisar que uma variável esteja disponível em sessões futuras, considere adicioná-la ao seu arquivo de configuração do shell, como `~/.bashrc` ou `~/.bash_profile`.
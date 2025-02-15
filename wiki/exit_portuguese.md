# [리눅스] Bash exit 사용법

## Overview
O comando `exit` no Bash é utilizado para encerrar a execução de um script ou de uma sessão de terminal. Ele permite que o usuário saia de um shell ou finalize um script, retornando um código de saída que pode ser utilizado para indicar o sucesso ou a falha da operação. O código de saída é um número inteiro que pode ser interpretado por outros processos ou scripts.

## Usage
A sintaxe básica do comando `exit` é a seguinte:

```bash
exit [número]
```

- `número`: (opcional) Um código de saída que pode ser um inteiro entre 0 e 255. O padrão é 0, que geralmente indica que o script foi executado com sucesso. Qualquer número diferente de 0 geralmente indica que ocorreu um erro.

## Examples

### Exemplo 1: Saindo de um script com sucesso
```bash
#!/bin/bash
echo "Executando o script..."
# Código do script
exit 0
```
Neste exemplo, o script é executado e, ao final, o comando `exit 0` é chamado, indicando que o script foi concluído com sucesso.

### Exemplo 2: Saindo de um script com erro
```bash
#!/bin/bash
echo "Executando o script..."
# Simulando um erro
exit 1
```
Aqui, o script é executado e, ao final, o comando `exit 1` é chamado, indicando que ocorreu um erro durante a execução do script.

## Tips
- Sempre utilize códigos de saída apropriados para facilitar a depuração de scripts. O código 0 deve ser usado para indicar sucesso, enquanto números diferentes de 0 devem ser usados para indicar diferentes tipos de erros.
- Em scripts complexos, considere usar variáveis para armazenar códigos de saída e facilitar a manutenção do código.
- Lembre-se de que, ao sair de um shell interativo, o código de saída pode ser verificado usando o comando `echo $?` logo após o uso do `exit`.
# [Linux] Bash env Uso: [executar comandos com variáveis de ambiente]

## Overview
O comando `env` é utilizado para executar um comando em um ambiente modificado. Ele permite que você defina ou altere variáveis de ambiente temporariamente antes de executar um comando específico. Isso é útil para testar diferentes configurações de ambiente sem alterar permanentemente o ambiente do shell.

## Usage
A sintaxe básica do comando `env` é a seguinte:

```bash
env [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `env`:

- `-i`: Ignora o ambiente atual e executa o comando em um ambiente vazio.
- `-u VAR`: Remove a variável de ambiente especificada antes de executar o comando.
- `VAR=value`: Define uma nova variável de ambiente ou altera o valor de uma variável existente para o comando que será executado.

## Common Examples

### Executar um comando com uma variável de ambiente
```bash
env VAR1=valor1 comando
```
Este exemplo define `VAR1` como `valor1` apenas para a execução de `comando`.

### Ignorar o ambiente atual
```bash
env -i comando
```
Aqui, `comando` será executado em um ambiente completamente vazio, sem nenhuma variável de ambiente definida.

### Remover uma variável de ambiente
```bash
env -u VAR1 comando
```
Neste caso, `VAR1` será removida do ambiente antes da execução de `comando`.

### Definir várias variáveis de ambiente
```bash
env VAR1=valor1 VAR2=valor2 comando
```
Este exemplo define `VAR1` e `VAR2` com valores específicos para o comando que será executado.

## Tips
- Use `env` para testar scripts em ambientes limpos, garantindo que não haja interferência de variáveis de ambiente existentes.
- Quando precisar de um ambiente específico para um comando, combine `env` com outras ferramentas como `bash` ou `sh` para maior flexibilidade.
- Lembre-se de que as alterações feitas com `env` são temporárias e só afetam o comando que está sendo executado.
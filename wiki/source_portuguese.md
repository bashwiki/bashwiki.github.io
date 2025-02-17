# [Linux] Bash source uso equivalente: Executar comandos de um arquivo

## Overview
O comando `source` é utilizado em Bash para executar comandos contidos em um arquivo no contexto do shell atual. Isso significa que qualquer variável ou função definida no arquivo será acessível após a execução do comando.

## Usage
A sintaxe básica do comando `source` é a seguinte:

```bash
source [opções] [argumentos]
```

## Common Options
- `-h`, `--help`: Exibe uma mensagem de ajuda com informações sobre o uso do comando.
- `-V`, `--version`: Mostra a versão do shell Bash em uso.

## Common Examples

### Executar um script
Para executar um script chamado `meu_script.sh`, você pode usar:

```bash
source meu_script.sh
```

### Carregar variáveis de ambiente
Se você tiver um arquivo chamado `variaveis.sh` que define algumas variáveis de ambiente, pode carregá-las assim:

```bash
source variaveis.sh
```

### Definir funções
Se você tiver um arquivo `funcoes.sh` que contém definições de funções, você pode carregá-las no shell atual:

```bash
source funcoes.sh
```

### Atualizar o ambiente atual
Após fazer alterações em um arquivo de configuração, como `.bashrc`, você pode aplicar as mudanças sem reiniciar o terminal:

```bash
source ~/.bashrc
```

## Tips
- Sempre verifique se o arquivo que você está tentando carregar possui permissões de leitura.
- Utilize `source` para evitar a criação de subshells, garantindo que as variáveis e funções definidas no arquivo estejam disponíveis no shell atual.
- Se você estiver usando scripts que precisam ser executados frequentemente, considere adicionar o comando `source` em seu arquivo de inicialização do shell, como `.bash_profile` ou `.bashrc`.
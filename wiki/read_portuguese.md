# [리눅스] Bash read 사용법

## Overview
O comando `read` no Bash é utilizado para ler a entrada do usuário a partir do terminal. Ele permite que você armazene a entrada em variáveis, facilitando a interação com scripts e a coleta de dados. O `read` é especialmente útil em scripts interativos, onde é necessário obter informações do usuário antes de prosseguir com a execução do script.

## Usage
A sintaxe básica do comando `read` é a seguinte:

```bash
read [opções] [variáveis]
```

### Opções Comuns:
- `-p "mensagem"`: Exibe uma mensagem antes de ler a entrada do usuário.
- `-s`: Silencia a entrada do usuário, útil para senhas.
- `-a nome_array`: Lê a entrada em um array.
- `-d delimitador`: Define um delimitador para a entrada, em vez de usar a nova linha padrão.

## Examples

### Exemplo 1: Leitura Simples
```bash
#!/bin/bash
echo "Por favor, insira seu nome:"
read nome
echo "Olá, $nome!"
```
Neste exemplo, o script solicita que o usuário insira seu nome e, em seguida, exibe uma saudação personalizada.

### Exemplo 2: Usando a Opção -p
```bash
#!/bin/bash
read -p "Digite sua idade: " idade
echo "Você tem $idade anos."
```
Aqui, o script utiliza a opção `-p` para exibir uma mensagem antes de solicitar a idade do usuário.

## Tips
- Sempre valide a entrada do usuário após usar o `read` para garantir que os dados sejam do tipo e formato esperado.
- Considere usar a opção `-s` ao solicitar senhas para evitar que a entrada seja exibida no terminal.
- Utilize arrays para coletar múltiplas entradas em uma única linha, facilitando a manipulação de dados no seu script.
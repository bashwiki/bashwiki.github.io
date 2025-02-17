# [Linux] Bash read uso: Lê a entrada do usuário

## Overview
O comando `read` no Bash é utilizado para ler a entrada do usuário a partir do terminal. Ele permite que você capture dados inseridos pelo usuário e os armazene em variáveis, facilitando a interação em scripts.

## Usage
A sintaxe básica do comando `read` é a seguinte:

```bash
read [opções] [variáveis]
```

## Common Options
- `-p`: Exibe uma mensagem de prompt antes de ler a entrada.
- `-s`: Lê a entrada de forma silenciosa, não exibindo os caracteres digitados (útil para senhas).
- `-a`: Lê a entrada e a armazena em um array.
- `-t`: Define um tempo limite para a leitura da entrada.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `read`:

### Exemplo 1: Leitura simples
```bash
echo "Digite seu nome:"
read nome
echo "Olá, $nome!"
```

### Exemplo 2: Leitura com prompt
```bash
read -p "Digite sua idade: " idade
echo "Você tem $idade anos."
```

### Exemplo 3: Leitura silenciosa
```bash
read -s -p "Digite sua senha: " senha
echo -e "\nSenha recebida."
```

### Exemplo 4: Leitura em um array
```bash
read -a frutas -p "Digite algumas frutas separadas por espaço: "
echo "Você digitou: ${frutas[@]}"
```

### Exemplo 5: Leitura com tempo limite
```bash
if read -t 5 -p "Você tem 5 segundos para responder (s/n): " resposta; then
    echo "Você respondeu: $resposta"
else
    echo "Tempo esgotado!"
fi
```

## Tips
- Sempre valide a entrada do usuário para evitar erros em seu script.
- Utilize a opção `-s` ao solicitar senhas para garantir que a entrada não seja exibida.
- Considere usar arrays quando precisar capturar múltiplos valores de entrada.
- Use mensagens de prompt claras para guiar o usuário na entrada de dados.
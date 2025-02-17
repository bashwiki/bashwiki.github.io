# [Linux] Bash history uso: Exibe o histórico de comandos

## Overview
O comando `history` no Bash é utilizado para exibir uma lista dos comandos que foram executados anteriormente na sessão do terminal. Isso é útil para relembrar comandos usados, reutilizá-los ou até mesmo para depuração.

## Usage
A sintaxe básica do comando `history` é a seguinte:

```bash
history [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `history`:

- `-c`: Limpa o histórico atual.
- `-d <n>`: Remove a entrada de histórico na posição `n`.
- `-a`: Adiciona o histórico atual ao arquivo de histórico.
- `-r`: Lê o histórico do arquivo e o adiciona ao histórico atual.
- `-n`: Lê novas entradas do arquivo de histórico, mas não as adiciona ao histórico atual.

## Common Examples

### Exibir o histórico de comandos
Para visualizar todos os comandos que você executou, basta usar:

```bash
history
```

### Limpar o histórico
Para limpar todo o histórico de comandos, use:

```bash
history -c
```

### Remover uma entrada específica
Para remover a entrada de histórico na posição 5, você pode usar:

```bash
history -d 5
```

### Adicionar o histórico atual ao arquivo
Para garantir que os comandos da sessão atual sejam salvos, execute:

```bash
history -a
```

### Ler novas entradas do arquivo de histórico
Para atualizar seu histórico com novas entradas do arquivo, utilize:

```bash
history -n
```

## Tips
- Utilize o comando `!n` para executar rapidamente o comando na posição `n` do histórico.
- Use as setas para cima e para baixo no teclado para navegar rapidamente pelos comandos anteriores.
- Considere limpar o histórico regularmente para manter a privacidade, especialmente em sistemas compartilhados.
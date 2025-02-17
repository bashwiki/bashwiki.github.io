# [Linux] Bash logout uso: Sair da sessão do terminal

## Overview
O comando `logout` é utilizado para encerrar a sessão atual do terminal em sistemas Unix e Linux. Quando executado, ele finaliza a sessão do shell, o que pode ser útil quando você deseja sair de uma sessão de terminal ou de um ambiente de login.

## Usage
A sintaxe básica do comando `logout` é a seguinte:

```bash
logout [opções]
```

## Common Options
O comando `logout` não possui muitas opções, mas aqui estão algumas que podem ser relevantes:

- `--help`: Exibe uma mensagem de ajuda com informações sobre o uso do comando.
- `--version`: Mostra a versão do comando `logout` que está sendo utilizada.

## Common Examples

### Exemplo 1: Sair da sessão do terminal
Para encerrar a sessão atual do terminal, basta digitar:

```bash
logout
```

### Exemplo 2: Sair de uma sessão SSH
Se você estiver conectado a um servidor remoto via SSH e quiser sair, você pode usar o comando `logout`:

```bash
logout
```

### Exemplo 3: Usando logout em um script
Se você estiver escrevendo um script e precisar encerrar a sessão, você pode incluir o `logout` no final do seu script:

```bash
#!/bin/bash
# Seu script aqui
logout
```

## Tips
- Use o comando `exit` como alternativa ao `logout`, pois ele também encerra a sessão do terminal.
- Lembre-se de salvar seu trabalho antes de usar `logout`, pois todas as sessões e processos em execução serão encerrados.
- Se você estiver em um ambiente gráfico, considere usar a opção de logout do menu em vez de usar o terminal.
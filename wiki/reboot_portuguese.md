# [Linux] Bash reboot uso: Reinicia o sistema

## Overview
O comando `reboot` é utilizado para reiniciar o sistema operacional de forma controlada. Ele encerra todos os processos em execução e reinicia a máquina, garantindo que todas as alterações sejam salvas e que o sistema volte a ser iniciado corretamente.

## Usage
A sintaxe básica do comando `reboot` é a seguinte:

```bash
reboot [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `reboot`:

- `-f`: Força o reinício do sistema sem realizar um desligamento adequado.
- `-p`: Desliga o sistema após o reinício, se suportado.
- `--halt`: Para o sistema e o desliga em vez de reiniciá-lo.

## Common Examples

### Exemplo 1: Reiniciar o sistema
Para reiniciar o sistema normalmente, você pode usar o comando:

```bash
reboot
```

### Exemplo 2: Forçar o reinício
Se você precisar forçar o reinício do sistema, use a opção `-f`:

```bash
reboot -f
```

### Exemplo 3: Reiniciar e desligar
Para reiniciar o sistema e, em seguida, desligá-lo, utilize a opção `-p`:

```bash
reboot -p
```

### Exemplo 4: Reiniciar com uma mensagem
Você pode enviar uma mensagem para todos os usuários antes de reiniciar:

```bash
shutdown -r now "O sistema será reiniciado em 1 minuto."
```

## Tips
- Sempre salve seu trabalho antes de executar o comando `reboot`, pois ele encerrará todos os processos em execução.
- Use a opção `-f` com cautela, pois ela não permite que os processos sejam encerrados adequadamente.
- Considere usar o comando `shutdown` se você precisar de um aviso prévio para os usuários antes de reiniciar o sistema.
# [리눅스] Bash shutdown 사용법

## Overview
O comando `shutdown` é utilizado no sistema operacional Linux para desligar ou reiniciar o sistema de forma controlada. Ele permite que os usuários programem o desligamento do sistema, informando todos os usuários conectados sobre a ação que será realizada. O principal objetivo do comando é garantir que todos os processos sejam finalizados corretamente e que os dados sejam salvos antes que o sistema seja desligado.

## Usage
A sintaxe básica do comando `shutdown` é a seguinte:

```
shutdown [OPÇÕES] [TEMPO] [MENSAGEM]
```

### Opções Comuns:
- `-h` ou `--halt`: Desliga o sistema.
- `-r` ou `--reboot`: Reinicia o sistema.
- `-P` ou `--poweroff`: Desliga o sistema e desliga a energia.
- `now`: Especifica que o desligamento deve ocorrer imediatamente.
- `+m`: Especifica o tempo em minutos após o qual o sistema deve ser desligado (por exemplo, `+5` para 5 minutos).
- `MENSAGEM`: Uma mensagem opcional que será enviada a todos os usuários conectados.

## Examples
### Exemplo 1: Desligar o sistema imediatamente
Para desligar o sistema imediatamente, você pode usar o seguinte comando:

```bash
shutdown -h now
```

### Exemplo 2: Reiniciar o sistema após 10 minutos
Se você deseja reiniciar o sistema após 10 minutos, utilize o comando:

```bash
shutdown -r +10 "O sistema será reiniciado em 10 minutos. Salve seu trabalho!"
```

## Tips
- Sempre informe os usuários conectados sobre o desligamento ou reinício do sistema, utilizando a opção de mensagem. Isso ajuda a evitar perda de dados.
- Para cancelar um desligamento programado, você pode usar o comando `shutdown -c`.
- Utilize o comando com cautela, especialmente em servidores de produção, para evitar interrupções inesperadas nos serviços.
- Considere agendar desligamentos durante horários de baixa utilização para minimizar o impacto nos usuários.
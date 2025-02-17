# [Linux] Bash shutdown uso: Desligar o sistema

O comando `shutdown` é utilizado para desligar, reiniciar ou colocar o sistema em modo de espera de forma segura.

## Overview
O comando `shutdown` permite que você desligue ou reinicie o sistema de forma controlada. Ele notifica os usuários conectados e pode ser agendado para um horário específico, garantindo que todos os processos sejam finalizados corretamente.

## Usage
A sintaxe básica do comando é a seguinte:

```bash
shutdown [opções] [tempo] [motivo]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o comando `shutdown`:

- `-h`: Desliga o sistema.
- `-r`: Reinicia o sistema.
- `-P`: Desliga o sistema e corta a energia (apenas em alguns sistemas).
- `now`: Executa o comando imediatamente.
- `+n`: Agenda o desligamento para `n` minutos a partir de agora.
- `hh:mm`: Agenda o desligamento para uma hora específica.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `shutdown`:

1. Para desligar o sistema imediatamente:
   ```bash
   shutdown -h now
   ```

2. Para reiniciar o sistema após 5 minutos:
   ```bash
   shutdown -r +5
   ```

3. Para desligar o sistema às 22:30:
   ```bash
   shutdown -h 22:30
   ```

4. Para enviar uma mensagem a todos os usuários antes de desligar:
   ```bash
   shutdown -h +1 "O sistema será desligado em 1 minuto. Salve seu trabalho!"
   ```

5. Para cancelar um desligamento agendado:
   ```bash
   shutdown -c
   ```

## Tips
- Sempre avise os usuários conectados antes de desligar o sistema, especialmente em ambientes multiusuário.
- Use o comando `shutdown -c` para cancelar um desligamento agendado se necessário.
- Considere usar `shutdown -r` em vez de desligar se você precisar reiniciar o sistema, pois isso pode ser mais eficiente em algumas situações.
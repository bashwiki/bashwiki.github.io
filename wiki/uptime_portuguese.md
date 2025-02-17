# [Linux] Bash uptime Uso: Exibe o tempo de atividade do sistema

## Overview
O comando `uptime` é utilizado para mostrar há quanto tempo o sistema está em funcionamento, além de fornecer informações sobre o número de usuários logados e a carga média do sistema nos últimos 1, 5 e 15 minutos.

## Usage
A sintaxe básica do comando é a seguinte:

```bash
uptime [opções]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `uptime`:

- `-p` : Exibe o tempo de atividade de forma legível, como "up 5 horas, 10 minutos".
- `-s` : Mostra a data e hora em que o sistema foi iniciado.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `uptime`:

1. Exibir o tempo de atividade do sistema:
   ```bash
   uptime
   ```

2. Exibir o tempo de atividade de forma legível:
   ```bash
   uptime -p
   ```

3. Mostrar a data e hora de início do sistema:
   ```bash
   uptime -s
   ```

4. Usar `uptime` em um script para monitorar a carga do sistema:
   ```bash
   if [ $(uptime | awk '{print $NF}' | sed 's/,//') > 1.0 ]; then
       echo "A carga do sistema está alta!"
   fi
   ```

## Tips
- Utilize `uptime` regularmente para monitorar a saúde do seu sistema e identificar possíveis problemas de desempenho.
- Combine `uptime` com outros comandos, como `top` ou `htop`, para obter uma visão mais completa do estado do sistema.
- Considere agendar o uso do `uptime` em scripts de monitoramento para registrar a carga do sistema ao longo do tempo.
# [Linux] Bash mpstat Uso: Monitoramento de estatísticas de CPU

## Overview
O comando `mpstat` é utilizado para exibir estatísticas de uso da CPU em sistemas Linux. Ele fornece informações detalhadas sobre a utilização do processador, permitindo que os usuários monitorem o desempenho do sistema em tempo real.

## Usage
A sintaxe básica do comando `mpstat` é a seguinte:

```bash
mpstat [opções] [intervalo] [contagem]
```

## Common Options
- `-P ALL`: Exibe estatísticas para todas as CPUs disponíveis.
- `-u`: Mostra a utilização da CPU em porcentagem.
- `-h`: Exibe a saída em um formato mais legível (com unidades apropriadas).
- `-V`: Mostra a versão do `mpstat`.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `mpstat`:

1. **Exibir estatísticas de CPU para todas as CPUs a cada 5 segundos:**
   ```bash
   mpstat -P ALL 5
   ```

2. **Mostrar a utilização da CPU em porcentagem:**
   ```bash
   mpstat -u 5 3
   ```

3. **Exibir a versão do mpstat:**
   ```bash
   mpstat -V
   ```

4. **Mostrar estatísticas de CPU com formato legível:**
   ```bash
   mpstat -h 5
   ```

## Tips
- Utilize o `mpstat` em conjunto com outros comandos, como `grep`, para filtrar informações específicas.
- Monitore o desempenho do sistema durante períodos de pico para identificar gargalos.
- Considere usar scripts para automatizar a coleta de dados de desempenho com `mpstat` em intervalos regulares.
# [Linux] Bash journalctl Uso: Visualizar logs do sistema

## Overview
O comando `journalctl` é uma ferramenta utilizada para acessar e visualizar os logs do sistema gerenciados pelo systemd. Ele permite que os usuários consultem mensagens de log de forma organizada, facilitando a identificação de problemas e a análise do comportamento do sistema.

## Usage
A sintaxe básica do comando `journalctl` é a seguinte:

```bash
journalctl [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o `journalctl`:

- `-b` ou `--boot`: Mostra logs do sistema desde o último boot.
- `-f` ou `--follow`: Segue a saída de logs em tempo real, semelhante ao comando `tail -f`.
- `-p` ou `--priority`: Filtra as mensagens de log por prioridade (ex: emerg, alert, crit, err, warning, notice, info, debug).
- `-u` ou `--unit`: Mostra logs de uma unidade específica do systemd.
- `--since` e `--until`: Filtra logs entre duas datas ou horários específicos.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `journalctl`:

1. **Visualizar todos os logs do sistema:**
   ```bash
   journalctl
   ```

2. **Ver os logs desde o último boot:**
   ```bash
   journalctl -b
   ```

3. **Seguir os logs em tempo real:**
   ```bash
   journalctl -f
   ```

4. **Filtrar logs por prioridade (ex: erros):**
   ```bash
   journalctl -p err
   ```

5. **Visualizar logs de uma unidade específica (ex: apache2.service):**
   ```bash
   journalctl -u apache2.service
   ```

6. **Filtrar logs entre datas específicas:**
   ```bash
   journalctl --since "2023-10-01" --until "2023-10-10"
   ```

## Tips
- Utilize a opção `-f` para monitorar logs em tempo real durante a resolução de problemas.
- Combine filtros de data com a opção `-u` para obter logs mais específicos de serviços.
- Salve a saída de logs em um arquivo para análise posterior usando a redireção:
  ```bash
  journalctl > logs.txt
  ```
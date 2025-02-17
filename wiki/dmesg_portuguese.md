# [Linux] Bash dmesg Uso: Exibir mensagens do kernel

## Overview
O comando `dmesg` é utilizado para exibir mensagens do buffer do kernel do Linux. Essas mensagens geralmente incluem informações sobre hardware, drivers e eventos do sistema, sendo útil para diagnosticar problemas e monitorar o funcionamento do sistema.

## Usage
A sintaxe básica do comando `dmesg` é a seguinte:

```bash
dmesg [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `dmesg`:

- `-C`: Limpa o buffer de mensagens do kernel.
- `-c`: Exibe as mensagens e limpa o buffer ao mesmo tempo.
- `-n nível`: Define o nível de log a ser exibido (por exemplo, `-n 1` para exibir apenas mensagens de emergência).
- `-T`: Exibe as mensagens com timestamps legíveis por humanos.
- `--follow`: Monitora o buffer de mensagens em tempo real, semelhante ao comando `tail -f`.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `dmesg`:

1. **Exibir todas as mensagens do kernel:**
   ```bash
   dmesg
   ```

2. **Limpar o buffer de mensagens:**
   ```bash
   dmesg -C
   ```

3. **Exibir mensagens com timestamps legíveis:**
   ```bash
   dmesg -T
   ```

4. **Monitorar mensagens em tempo real:**
   ```bash
   dmesg --follow
   ```

5. **Exibir mensagens de nível de log 1 (emergência):**
   ```bash
   dmesg -n 1
   ```

## Tips
- Utilize `dmesg -T` para facilitar a leitura das mensagens, especialmente ao investigar problemas recentes.
- Combine `dmesg` com `grep` para filtrar mensagens específicas, por exemplo:
  ```bash
  dmesg | grep erro
  ```
- Lembre-se de que as mensagens do `dmesg` podem ser úteis para entender problemas de hardware ou falhas de driver, então verifique-as ao solucionar problemas do sistema.
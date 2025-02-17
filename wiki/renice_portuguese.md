# [Linux] Bash renice Uso: Ajustar a prioridade de processos em execução

## Overview
O comando `renice` é utilizado para alterar a prioridade de processos que já estão em execução no sistema. A prioridade de um processo determina a quantidade de tempo de CPU que ele receberá em relação a outros processos. Um valor de prioridade mais baixo indica uma prioridade mais alta.

## Usage
A sintaxe básica do comando `renice` é a seguinte:

```bash
renice [opções] [valores de prioridade] [PID]
```

- `[opções]`: opções adicionais que podem ser usadas com o comando.
- `[valores de prioridade]`: o novo valor de prioridade que você deseja atribuir ao processo.
- `[PID]`: o identificador do processo que você deseja modificar.

## Common Options
- `-n`: Especifica o novo valor de prioridade. Este valor pode ser positivo (menor prioridade) ou negativo (maior prioridade).
- `-p`: Permite especificar o PID do processo que você deseja alterar.
- `-g`: Altera a prioridade de todos os processos em um grupo de processos.

## Common Examples

1. **Alterar a prioridade de um processo específico:**
   Para aumentar a prioridade (tornar mais importante) de um processo com PID 1234, você pode usar:
   ```bash
   renice -n -5 -p 1234
   ```

2. **Reduzir a prioridade de um processo:**
   Para reduzir a prioridade de um processo com PID 5678, você pode usar:
   ```bash
   renice -n 10 -p 5678
   ```

3. **Alterar a prioridade de todos os processos de um grupo:**
   Para alterar a prioridade de todos os processos em um grupo com GID 1000, você pode usar:
   ```bash
   renice -n 5 -g 1000
   ```

4. **Verificar a prioridade atual de um processo:**
   Embora `renice` não mostre a prioridade atual, você pode usar o comando `ps` para verificar:
   ```bash
   ps -o pid,ni,cmd -p 1234
   ```

## Tips
- Sempre verifique a prioridade atual de um processo antes de alterá-la para evitar conflitos indesejados.
- Use valores de prioridade com cautela; definir uma prioridade muito alta para um processo pode afetar o desempenho de outros processos no sistema.
- Para usar `renice`, você pode precisar de permissões de superusuário, especialmente ao alterar a prioridade de processos que não pertencem ao seu usuário.
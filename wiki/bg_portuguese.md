# [Linux] Bash bg Uso equivalente: Colocar processos em segundo plano

## Overview
O comando `bg` é utilizado no Bash para retomar a execução de processos que estão em estado de suspensão (suspended) e colocá-los em segundo plano. Isso permite que você continue utilizando o terminal enquanto o processo é executado.

## Usage
A sintaxe básica do comando `bg` é a seguinte:

```bash
bg [opções] [número do trabalho]
```

## Common Options
- `job_spec`: Especifica o trabalho que você deseja colocar em segundo plano. Você pode usar o número do trabalho (precedido por um `%`) ou o nome do processo.
- `-n`: Não exibe mensagens de status.

## Common Examples

1. **Colocar um trabalho em segundo plano**
   Se você tiver um trabalho suspenso, como um editor de texto, pode usar o seguinte comando:
   ```bash
   bg %1
   ```

2. **Colocar o último trabalho suspenso em segundo plano**
   Para colocar o último trabalho suspenso em segundo plano, você pode simplesmente usar:
   ```bash
   bg
   ```

3. **Colocar um trabalho específico em segundo plano**
   Se você tiver vários trabalhos e quiser colocar um específico em segundo plano, use:
   ```bash
   bg %2
   ```

4. **Colocar um trabalho em segundo plano sem mensagens**
   Para colocar um trabalho em segundo plano sem exibir mensagens de status, você pode usar:
   ```bash
   bg -n %1
   ```

## Tips
- Sempre verifique a lista de trabalhos suspensos com o comando `jobs` antes de usar o `bg`, para saber qual trabalho você deseja retomar.
- Lembre-se de que os processos em segundo plano ainda podem gerar saída no terminal. Use redirecionamento se você não quiser ver a saída.
- Combine o `bg` com o comando `disown` se você quiser que o processo continue executando mesmo após fechar o terminal.
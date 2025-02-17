# [Linux] Bash nice uso equivalente: Ajustar a prioridade de execução de processos

## Overview
O comando `nice` é utilizado para iniciar processos com uma prioridade ajustada. Ele permite que os usuários especifiquem a prioridade de um comando, ajudando a gerenciar a carga do sistema e a alocar recursos de forma mais eficiente.

## Usage
A sintaxe básica do comando `nice` é a seguinte:

```bash
nice [opções] [comando]
```

## Common Options
Aqui estão algumas opções comuns do comando `nice`:

- `-n, --adjustment=N`: Define o valor de ajuste da prioridade. O padrão é 10, e valores negativos aumentam a prioridade.
- `-h, --help`: Mostra a ajuda sobre o comando.
- `--version`: Exibe a versão do comando.

## Common Examples

1. **Executar um comando com prioridade padrão:**
   ```bash
   nice ls -l
   ```

2. **Executar um comando com prioridade reduzida (mais baixa):**
   ```bash
   nice -n 19 ./meu_script.sh
   ```

3. **Executar um comando com prioridade aumentada (mais alta):**
   ```bash
   nice -n -5 ./meu_programa
   ```

4. **Verificar a prioridade de um processo em execução:**
   ```bash
   ps -o pid,nice,cmd
   ```

## Tips
- Use valores negativos com cautela, pois eles aumentam a prioridade do processo e podem afetar a performance de outros processos.
- Para verificar a prioridade de processos em execução, utilize o comando `ps` com as opções apropriadas.
- Combine `nice` com outros comandos, como `nohup`, para executar processos em segundo plano sem interrupções.
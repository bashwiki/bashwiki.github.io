# [Linux] Bash jobs Uso: Gerenciar trabalhos em segundo plano

## Overview
O comando `jobs` no Bash é utilizado para listar os trabalhos em segundo plano que estão sendo executados na sessão atual do terminal. Ele permite que os usuários vejam quais processos estão ativos, suas IDs e seus estados, facilitando o gerenciamento de tarefas.

## Usage
A sintaxe básica do comando `jobs` é a seguinte:

```
jobs [opções]
```

## Common Options
- `-l`: Exibe o PID (Process ID) dos trabalhos.
- `-n`: Mostra apenas os trabalhos que mudaram de estado desde a última execução do comando.
- `-p`: Exibe apenas os PIDs dos trabalhos.

## Common Examples

1. **Listar todos os trabalhos em segundo plano:**
   ```bash
   jobs
   ```

2. **Listar trabalhos com PIDs:**
   ```bash
   jobs -l
   ```

3. **Listar apenas trabalhos que mudaram de estado:**
   ```bash
   jobs -n
   ```

4. **Listar apenas PIDs dos trabalhos:**
   ```bash
   jobs -p
   ```

## Tips
- Utilize o comando `bg` para retomar um trabalho em segundo plano após pausá-lo com `Ctrl+Z`.
- Combine o comando `jobs` com `fg` para trazer um trabalho em segundo plano para o primeiro plano.
- Sempre verifique o estado dos seus trabalhos antes de fechar o terminal para evitar a perda de processos em execução.
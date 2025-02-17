# [Linux] Bash no at: Agendar tarefas

## Overview
O comando `at` é utilizado para agendar a execução de tarefas em um momento específico no futuro. Ele permite que os usuários programem comandos ou scripts para serem executados uma única vez em um horário determinado.

## Usage
A sintaxe básica do comando `at` é a seguinte:

```bash
at [opções] [hora]
```

## Common Options
Aqui estão algumas opções comuns do comando `at`:

- `-f`: Especifica um arquivo que contém os comandos a serem executados.
- `-m`: Envia um e-mail ao usuário após a execução do comando, mesmo que não haja saída.
- `-q`: Define a fila de execução (por exemplo, `a`, `b`, `c`, etc.).
- `-v`: Exibe a hora em que o comando será executado.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `at`:

1. **Agendar um comando para ser executado agora**:
   ```bash
   echo "echo 'Olá, mundo!'" | at now
   ```

2. **Agendar um comando para ser executado em uma hora específica**:
   ```bash
   echo "backup.sh" | at 14:00
   ```

3. **Agendar um comando para ser executado amanhã**:
   ```bash
   echo "limpar_temp.sh" | at tomorrow
   ```

4. **Usar um arquivo para agendar comandos**:
   ```bash
   at -f script.sh 15:00
   ```

5. **Agendar um comando e receber um e-mail após a execução**:
   ```bash
   echo "report.sh" | at -m 18:00
   ```

## Tips
- Sempre verifique se o serviço `atd` está em execução no seu sistema, pois ele é necessário para que os comandos agendados sejam executados.
- Utilize o comando `atq` para listar os trabalhos agendados e `atrm` para remover um trabalho específico.
- Para agendar tarefas recorrentes, considere usar o comando `cron`, que é mais adequado para execuções repetidas.
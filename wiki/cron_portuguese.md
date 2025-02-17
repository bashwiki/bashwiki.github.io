# [Linux] Bash cron uso: Agendar tarefas automaticamente

## Overview
O comando `cron` é utilizado para agendar a execução de tarefas em intervalos regulares no sistema operacional Linux. Ele permite que os usuários automatizem processos, como backups, atualizações e scripts, sem a necessidade de intervenção manual.

## Usage
A sintaxe básica do comando `cron` é a seguinte:

```bash
crontab [opções] [arquivo]
```

## Common Options
- `-e`: Editar o crontab do usuário atual.
- `-l`: Listar as tarefas agendadas no crontab do usuário atual.
- `-r`: Remover o crontab do usuário atual.
- `-i`: Solicitar confirmação antes de remover o crontab.

## Common Examples
Aqui estão alguns exemplos práticos de como usar o `cron`:

1. **Agendar um script para rodar diariamente às 2 da manhã:**
   ```bash
   0 2 * * * /caminho/para/seu/script.sh
   ```

2. **Executar um comando a cada hora:**
   ```bash
   0 * * * * /usr/bin/some-command
   ```

3. **Rodar um script todos os domingos às 5 da tarde:**
   ```bash
   0 17 * * 0 /caminho/para/seu/script.sh
   ```

4. **Executar um backup a cada 15 minutos:**
   ```bash
   */15 * * * * /caminho/para/seu/backup.sh
   ```

## Tips
- Sempre verifique o log de execução das tarefas agendadas para identificar possíveis erros.
- Use caminhos absolutos para scripts e comandos para evitar problemas de localização.
- Teste seus scripts manualmente antes de agendá-los com `cron` para garantir que funcionem corretamente.
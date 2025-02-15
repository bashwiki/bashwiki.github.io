# [리눅스] Bash at 사용법

## Overview
O comando `at` é uma ferramenta do sistema Linux que permite agendar a execução de comandos ou scripts em um momento específico no futuro. É especialmente útil para tarefas que precisam ser realizadas uma única vez, como backups, relatórios ou qualquer outra tarefa automatizada que não requer repetição regular.

## Usage
A sintaxe básica do comando `at` é a seguinte:

```bash
at [opções] [hora]
```

### Opções Comuns:
- `-f arquivo`: Especifica um arquivo que contém os comandos a serem executados.
- `-m`: Envia um e-mail para o usuário após a execução do comando, mesmo que não haja saída.
- `-q fila`: Permite especificar uma fila de trabalho diferente para o comando.
- `-l`: Lista os trabalhos agendados.
- `-d`: Remove um trabalho agendado.

## Examples
### Exemplo 1: Agendar um comando simples
Para agendar a execução do comando `echo` para ser executado às 15:00 de hoje, você pode usar:

```bash
echo "Hello, World!" | at 15:00
```

### Exemplo 2: Agendar um script
Se você tiver um script chamado `backup.sh` que deseja executar amanhã às 2:00 da manhã, você pode fazer assim:

```bash
at 02:00 tomorrow -f backup.sh
```

## Tips
- Sempre verifique se o serviço `atd` está em execução no seu sistema, pois ele é necessário para que os trabalhos agendados sejam executados.
- Utilize o comando `at -l` para listar todos os trabalhos agendados e `at -d [job_id]` para remover um trabalho específico.
- Para horários, você pode usar formatos como "now + 1 hour", "tomorrow", ou "5:00 PM" para maior flexibilidade.
- Considere usar a opção `-m` se você precisar de uma confirmação por e-mail após a execução do comando, especialmente para tarefas críticas.
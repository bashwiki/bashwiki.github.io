# [Linux] Bash tail Uso: Exibir as últimas linhas de um arquivo

## Overview
O comando `tail` é utilizado para exibir as últimas linhas de um arquivo de texto. É especialmente útil para monitorar logs ou arquivos que estão sendo atualizados em tempo real.

## Usage
A sintaxe básica do comando `tail` é a seguinte:

```bash
tail [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `tail`:

- `-n [número]`: Especifica o número de linhas a serem exibidas. Por padrão, exibe as últimas 10 linhas.
- `-f`: Segue o arquivo em tempo real, exibindo novas linhas à medida que são adicionadas.
- `-c [número]`: Exibe os últimos bytes do arquivo em vez de linhas.
- `--help`: Mostra a ajuda do comando.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `tail`:

1. Exibir as últimas 10 linhas de um arquivo chamado `exemplo.txt`:
   ```bash
   tail exemplo.txt
   ```

2. Exibir as últimas 20 linhas de um arquivo:
   ```bash
   tail -n 20 exemplo.txt
   ```

3. Seguir um arquivo de log em tempo real:
   ```bash
   tail -f /var/log/syslog
   ```

4. Exibir os últimos 50 bytes de um arquivo:
   ```bash
   tail -c 50 exemplo.txt
   ```

5. Combinar opções para seguir um arquivo e exibir as últimas 5 linhas:
   ```bash
   tail -n 5 -f exemplo.txt
   ```

## Tips
- Use `tail -f` para monitorar logs em tempo real, como arquivos de log de servidores, para facilitar a depuração.
- Combine `tail` com outros comandos, como `grep`, para filtrar as linhas exibidas. Por exemplo:
  ```bash
  tail -f /var/log/syslog | grep "erro"
  ```
- Lembre-se de que você pode usar `Ctrl + C` para interromper o comando `tail -f` quando não precisar mais monitorar o arquivo.
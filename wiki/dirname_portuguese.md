# [Linux] Bash dirname Uso: Extrai o diretório de um caminho

## Overview
O comando `dirname` é utilizado para extrair o diretório de um caminho de arquivo. Ele remove o nome do arquivo e retorna apenas o caminho do diretório que contém esse arquivo.

## Usage
A sintaxe básica do comando `dirname` é a seguinte:

```bash
dirname [opções] [argumentos]
```

## Common Options
- `-z`: Trata os argumentos como uma lista separada por nulos.
- `--help`: Mostra a ajuda sobre o comando.
- `--version`: Exibe a versão do comando.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `dirname`:

1. **Extraindo o diretório de um caminho absoluto:**
   ```bash
   dirname /home/usuario/documentos/arquivo.txt
   ```
   Saída:
   ```
   /home/usuario/documentos
   ```

2. **Usando com um caminho relativo:**
   ```bash
   dirname ./imagens/foto.jpg
   ```
   Saída:
   ```
   ./imagens
   ```

3. **Extraindo o diretório de um caminho com múltiplos níveis:**
   ```bash
   dirname /var/log/syslog
   ```
   Saída:
   ```
   /var/log
   ```

4. **Tratando uma lista de caminhos:**
   ```bash
   dirname /usr/local/bin/script.sh /home/user/arquivo.txt
   ```
   Saída:
   ```
   /usr/local/bin
   /home/user
   ```

## Tips
- Utilize `dirname` em scripts para manipular caminhos de arquivos de forma eficiente.
- Combine `dirname` com outros comandos, como `basename`, para obter tanto o diretório quanto o nome do arquivo em uma única linha de comando.
- Lembre-se de que `dirname` não verifica se o caminho existe; ele apenas manipula a string fornecida.
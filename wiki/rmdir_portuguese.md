# [Linux] Bash rmdir uso: Remove diretórios vazios

## Overview
O comando `rmdir` é utilizado para remover diretórios vazios no sistema de arquivos. Se o diretório contiver arquivos ou subdiretórios, o comando não conseguirá removê-lo, e uma mensagem de erro será exibida.

## Usage
A sintaxe básica do comando `rmdir` é a seguinte:

```
rmdir [opções] [argumentos]
```

## Common Options
- `-p`: Remove diretórios vazios pai, se eles também estiverem vazios.
- `--ignore-fail-on-non-empty`: Ignora erros se o diretório não estiver vazio.
- `--verbose`: Exibe uma mensagem para cada diretório removido.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `rmdir`:

1. **Remover um diretório vazio:**
   ```bash
   rmdir meu_diretorio
   ```

2. **Remover diretórios vazios pai:**
   ```bash
   rmdir -p meu_diretorio/pai
   ```

3. **Remover um diretório vazio e mostrar uma mensagem:**
   ```bash
   rmdir --verbose meu_diretorio
   ```

4. **Ignorar erro se o diretório não estiver vazio:**
   ```bash
   rmdir --ignore-fail-on-non-empty meu_diretorio
   ```

## Tips
- Sempre verifique se o diretório está realmente vazio antes de usar `rmdir`, para evitar erros.
- Utilize a opção `-p` com cuidado, pois ela pode remover diretórios pai que você pode precisar.
- Considere usar `rm -r` se precisar remover diretórios que contêm arquivos ou subdiretórios, mas tenha cuidado, pois essa opção é destrutiva.
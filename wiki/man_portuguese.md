# [Linux] Bash man uso: Exibe a documentação de comandos

## Overview
O comando `man` é utilizado para acessar as páginas de manual dos comandos disponíveis no sistema Linux. Essas páginas contêm informações detalhadas sobre como usar os comandos, suas opções e exemplos práticos.

## Usage
A sintaxe básica do comando `man` é a seguinte:

```bash
man [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `man`:

- `-k`: Busca por palavras-chave nas páginas de manual.
- `-f`: Exibe uma breve descrição de um comando.
- `-a`: Exibe todas as páginas de manual disponíveis para um comando, uma após a outra.
- `-M`: Especifica um diretório alternativo para as páginas de manual.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `man`:

1. Para visualizar a página de manual do comando `ls`:
   ```bash
   man ls
   ```

2. Para buscar por uma palavra-chave, como "copy":
   ```bash
   man -k copy
   ```

3. Para obter uma breve descrição do comando `cp`:
   ```bash
   man -f cp
   ```

4. Para visualizar todas as páginas de manual do comando `printf`:
   ```bash
   man -a printf
   ```

5. Para especificar um diretório alternativo para as páginas de manual:
   ```bash
   man -M /caminho/para/manual ls
   ```

## Tips
- Sempre utilize `man` para entender melhor os comandos que você está utilizando, especialmente se você não estiver familiarizado com eles.
- Combine `man` com `grep` para filtrar informações específicas dentro da página de manual. Por exemplo:
  ```bash
  man ls | grep "opções"
  ```
- Lembre-se de que as páginas de manual podem variar entre distribuições, então sempre verifique a documentação específica da sua versão do Linux.
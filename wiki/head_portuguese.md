# [Linux] Bash head Uso: Exibir as primeiras linhas de um arquivo

## Overview
O comando `head` é utilizado para exibir as primeiras linhas de um ou mais arquivos. Por padrão, ele mostra as primeiras 10 linhas, mas isso pode ser ajustado conforme necessário.

## Usage
A sintaxe básica do comando `head` é a seguinte:

```bash
head [opções] [argumentos]
```

## Common Options
- `-n [número]`: Especifica o número de linhas a serem exibidas. Por exemplo, `-n 5` exibirá as primeiras 5 linhas.
- `-c [número]`: Exibe os primeiros bytes do arquivo. Por exemplo, `-c 100` mostrará os primeiros 100 bytes.
- `-q`: Não exibe os cabeçalhos dos arquivos quando múltiplos arquivos são fornecidos.
- `-v`: Sempre exibe os cabeçalhos dos arquivos, mesmo que haja apenas um arquivo.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `head`:

1. Exibir as primeiras 10 linhas de um arquivo chamado `exemplo.txt`:
   ```bash
   head exemplo.txt
   ```

2. Exibir as primeiras 5 linhas de um arquivo:
   ```bash
   head -n 5 exemplo.txt
   ```

3. Exibir os primeiros 100 bytes de um arquivo:
   ```bash
   head -c 100 exemplo.txt
   ```

4. Exibir as primeiras 10 linhas de múltiplos arquivos:
   ```bash
   head arquivo1.txt arquivo2.txt
   ```

5. Exibir as primeiras 3 linhas de um arquivo e mostrar o cabeçalho:
   ```bash
   head -n 3 -v exemplo.txt
   ```

## Tips
- Utilize `head` em combinação com outros comandos, como `grep`, para filtrar resultados. Por exemplo:
  ```bash
  grep "erro" log.txt | head -n 10
  ```
- Para visualizar rapidamente o início de arquivos grandes, `head` é uma ferramenta eficiente e rápida.
- Lembre-se de que `head` pode ser usado em arquivos binários, mas a saída pode não ser legível.
# [Linux] Bash tac Uso: Inverter o conteúdo de arquivos

## Overview
O comando `tac` é utilizado para inverter a ordem das linhas de um arquivo. Ao contrário do comando `cat`, que exibe o conteúdo de um arquivo da primeira linha para a última, o `tac` faz o oposto, mostrando a última linha primeiro e a primeira linha por último.

## Usage
A sintaxe básica do comando `tac` é a seguinte:

```bash
tac [opções] [argumentos]
```

## Common Options
- `-b`, `--before`: Insere uma linha em branco antes das linhas de saída.
- `-r`, `--regex`: Trata as linhas como expressões regulares.
- `-s`, `--separator`: Define um separador específico entre as linhas.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `tac`:

1. **Inverter um arquivo de texto simples**:
   ```bash
   tac arquivo.txt
   ```

2. **Inverter um arquivo e salvar a saída em um novo arquivo**:
   ```bash
   tac arquivo.txt > arquivo_invertido.txt
   ```

3. **Inverter o conteúdo de um arquivo e adicionar uma linha em branco antes de cada linha**:
   ```bash
   tac -b arquivo.txt
   ```

4. **Usar um separador específico ao inverter as linhas**:
   ```bash
   tac -s ',' arquivo.csv
   ```

## Tips
- Utilize `tac` em combinação com outros comandos, como `grep` ou `sort`, para manipulações mais complexas de texto.
- Lembre-se de que `tac` é útil para visualizar rapidamente a ordem inversa de linhas, especialmente em arquivos de log.
- Teste o comando com arquivos pequenos antes de aplicá-lo em arquivos grandes para garantir que o resultado atenda às suas expectativas.
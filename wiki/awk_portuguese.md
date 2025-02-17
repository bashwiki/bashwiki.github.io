# [Linux] Bash awk Uso: Processamento de texto e análise de dados

## Overview
O comando `awk` é uma poderosa ferramenta de processamento de texto no Bash, amplamente utilizada para manipulação e análise de dados em arquivos de texto. Ele permite que os usuários realizem operações como filtragem, formatação e relatórios de dados de maneira eficiente.

## Usage
A sintaxe básica do comando `awk` é a seguinte:

```bash
awk [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `awk`:

- `-F`: Define o delimitador de campo. Por padrão, o `awk` usa espaços em branco como delimitador.
- `-v`: Permite definir variáveis antes da execução do script `awk`.
- `-f`: Especifica um arquivo que contém um script `awk` a ser executado.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `awk`:

1. **Imprimir a primeira coluna de um arquivo:**
   ```bash
   awk '{print $1}' arquivo.txt
   ```

2. **Usar um delimitador diferente (por exemplo, vírgula):**
   ```bash
   awk -F',' '{print $2}' arquivo.csv
   ```

3. **Filtrar linhas com base em uma condição:**
   ```bash
   awk '$3 > 50 {print $1, $2}' arquivo.txt
   ```

4. **Contar o número de linhas em um arquivo:**
   ```bash
   awk 'END {print NR}' arquivo.txt
   ```

5. **Somar valores de uma coluna:**
   ```bash
   awk '{soma += $1} END {print soma}' arquivo.txt
   ```

## Tips
- Sempre use aspas ao redor de suas instruções `awk` para evitar problemas com a interpretação do shell.
- Teste seus comandos `awk` em pequenos arquivos para garantir que eles funcionem como esperado antes de aplicá-los em arquivos maiores.
- Combine `awk` com outros comandos do Bash, como `grep` e `sort`, para realizar análises de dados mais complexas.
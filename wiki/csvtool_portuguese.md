# [Linux] Bash csvtool Uso: Manipulação de arquivos CSV

## Overview
O comando `csvtool` é uma ferramenta poderosa para manipulação de arquivos CSV (Comma-Separated Values). Ele permite que os usuários realizem operações como seleção de colunas, filtragem de linhas e formatação de dados de maneira simples e eficiente.

## Usage
A sintaxe básica do comando `csvtool` é a seguinte:

```bash
csvtool [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `csvtool`:

- `cut`: Seleciona colunas específicas de um arquivo CSV.
- `head`: Exibe as primeiras linhas de um arquivo CSV.
- `tail`: Exibe as últimas linhas de um arquivo CSV.
- `format`: Formata a saída de um arquivo CSV.

## Common Examples

### Exibir as primeiras 5 linhas de um arquivo CSV
```bash
csvtool head -n 5 arquivo.csv
```

### Selecionar colunas específicas
```bash
csvtool cut -c 1,3 arquivo.csv
```

### Exibir as últimas 10 linhas de um arquivo CSV
```bash
csvtool tail -n 10 arquivo.csv
```

### Formatar a saída de um arquivo CSV
```bash
csvtool format '%s' arquivo.csv
```

## Tips
- Sempre faça uma cópia de segurança dos seus arquivos CSV antes de realizar operações que possam modificar os dados.
- Utilize a opção `--help` para obter mais informações sobre as opções disponíveis no `csvtool`.
- Experimente combinar várias opções para realizar operações mais complexas de maneira eficiente.
# [Linux] Bash column uso: Formatar texto em colunas

## Overview
O comando `column` é utilizado para formatar texto em colunas, facilitando a leitura de dados tabulares no terminal. Ele organiza a saída de texto em um formato alinhado, tornando informações como listas e tabelas mais compreensíveis.

## Usage
A sintaxe básica do comando `column` é a seguinte:

```bash
column [options] [arguments]
```

## Common Options
- `-t`: Alinha as colunas em uma tabela, separando os dados por espaços em branco.
- `-s`: Especifica um delimitador diferente para separar as colunas (por exemplo, uma vírgula).
- `-n`: Não numera as linhas da saída.
- `-x`: Preenche as colunas em ordem de linha, em vez de coluna.

## Common Examples

### Exemplo 1: Formatar uma lista simples
```bash
echo -e "Nome\nJoão\nMaria\nCarlos" | column
```
Saída:
```
Nome   
João   
Maria  
Carlos 
```

### Exemplo 2: Usar um delimitador personalizado
```bash
echo -e "Nome,Idade\nJoão,30\nMaria,25\nCarlos,28" | column -s, -t
```
Saída:
```
Nome    Idade
João    30
Maria   25
Carlos  28
```

### Exemplo 3: Criar uma tabela a partir de um arquivo
Supondo que você tenha um arquivo `dados.txt` com o seguinte conteúdo:
```
Produto Preço
Maçã    1.00
Banana  0.50
Laranja 0.75
```
Você pode formatar este arquivo assim:
```bash
column -t dados.txt
```
Saída:
```
Produto  Preço
Maçã     1.00
Banana   0.50
Laranja  0.75
```

## Tips
- Utilize o `-t` para garantir que suas colunas estejam sempre alinhadas, especialmente ao lidar com dados de diferentes tamanhos.
- Se você estiver trabalhando com arquivos CSV, use a opção `-s` para definir a vírgula como delimitador.
- Experimente o `-x` para visualizar dados em uma ordem diferente, o que pode ser útil para certas análises.
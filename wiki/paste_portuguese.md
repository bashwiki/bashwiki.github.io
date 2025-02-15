# [리눅스] Bash paste 사용법

## Overview
O comando `paste` é uma ferramenta do Bash utilizada para mesclar linhas de arquivos de texto. Seu principal propósito é combinar linhas correspondentes de múltiplos arquivos, separando-as por um delimitador, que por padrão é uma tabulação. Isso é especialmente útil para manipulação de dados em formato tabular, onde você pode querer combinar informações de diferentes fontes em uma única linha.

## Usage
A sintaxe básica do comando `paste` é a seguinte:

```bash
paste [opções] [arquivo1] [arquivo2] ...
```

### Opções Comuns:
- `-d DELIM`: Especifica um delimitador diferente do padrão (tabulação) para separar as linhas combinadas. Você pode usar múltiplos delimitadores, que serão aplicados ciclicamente.
- `-s`: Junta as linhas de cada arquivo em uma única linha, em vez de combinar linhas correspondentes de múltiplos arquivos.
- `-z`: Trata os arquivos de entrada como se fossem terminados por null (NUL) em vez de nova linha.

## Examples
### Exemplo 1: Combinar duas linhas de arquivos
Suponha que você tenha dois arquivos, `file1.txt` e `file2.txt`, com o seguinte conteúdo:

**file1.txt**
```
A
B
C
```

**file2.txt**
```
1
2
3
```

Você pode usar o comando `paste` para combinar as linhas correspondentes desses arquivos:

```bash
paste file1.txt file2.txt
```

**Saída:**
```
A       1
B       2
C       3
```

### Exemplo 2: Usar um delimitador personalizado
Se você quiser usar um delimitador diferente, como uma vírgula, você pode fazer o seguinte:

```bash
paste -d ',' file1.txt file2.txt
```

**Saída:**
```
A,1
B,2
C,3
```

## Tips
- Quando usar o `paste`, é importante garantir que os arquivos tenham o mesmo número de linhas, caso contrário, as linhas extras de um arquivo serão ignoradas.
- Utilize a opção `-d` para personalizar a saída e torná-la mais legível ou adequada para o seu caso de uso.
- Combine `paste` com outros comandos do Bash, como `sort` e `uniq`, para realizar operações mais complexas em dados tabulares.
- Lembre-se de que o `paste` não altera os arquivos de entrada; ele apenas gera uma saída combinada no terminal ou em um arquivo, se redirecionado.
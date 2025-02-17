# [Linux] Bash basename Uso: Extrair o nome do arquivo

## Overview
O comando `basename` é utilizado para extrair o nome do arquivo a partir de um caminho completo. Ele remove o diretório e, opcionalmente, a extensão do arquivo, retornando apenas o nome.

## Usage
A sintaxe básica do comando é a seguinte:

```bash
basename [opções] [argumentos]
```

## Common Options
- `-a`: Aceita múltiplos argumentos e retorna o nome base de cada um.
- `-s`: Remove a extensão especificada do nome do arquivo.
- `--help`: Exibe a ajuda sobre o comando.

## Common Examples

1. **Extrair o nome do arquivo de um caminho completo:**

```bash
basename /home/usuario/documentos/arquivo.txt
```
Saída:
```
arquivo.txt
```

2. **Remover a extensão do arquivo:**

```bash
basename /home/usuario/documentos/arquivo.txt .txt
```
Saída:
```
arquivo
```

3. **Usar com múltiplos arquivos:**

```bash
basename -a /home/usuario/documentos/arquivo1.txt /home/usuario/documentos/arquivo2.txt
```
Saída:
```
arquivo1.txt
arquivo2.txt
```

4. **Remover a extensão de múltiplos arquivos:**

```bash
basename -a /home/usuario/documentos/arquivo1.txt /home/usuario/documentos/arquivo2.txt .txt
```
Saída:
```
arquivo1
arquivo2
```

## Tips
- Utilize `basename` em scripts para simplificar o processamento de nomes de arquivos.
- Combine `basename` com outros comandos, como `find`, para manipular arquivos de forma mais eficiente.
- Lembre-se de que o `basename` não altera os arquivos; ele apenas retorna o nome base.
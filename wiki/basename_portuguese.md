# [리눅스] Bash basename 사용법

## Overview
O comando `basename` é uma ferramenta do Bash utilizada para extrair o nome do arquivo de um caminho completo. Ele remove todos os diretórios do caminho fornecido, retornando apenas o nome do arquivo ou diretório final. Este comando é especialmente útil em scripts e automações, onde é necessário manipular ou exibir apenas o nome do arquivo sem a necessidade de seu caminho completo.

## Usage
A sintaxe básica do comando `basename` é a seguinte:

```bash
basename [caminho] [sufixo]
```

- **caminho**: O caminho completo do arquivo ou diretório do qual você deseja extrair o nome.
- **sufixo** (opcional): Um sufixo que, se presente no nome do arquivo, será removido do resultado.

### Opções Comuns
- `-a`: Aceita múltiplos caminhos e retorna o nome base de cada um deles.
- `-s`: Permite especificar um sufixo a ser removido do nome do arquivo.

## Examples
Aqui estão alguns exemplos práticos de como usar o comando `basename`.

### Exemplo 1: Extraindo o nome de um arquivo
```bash
basename /home/usuario/documentos/relatorio.txt
```
**Saída:**
```
relatorio.txt
```
Neste exemplo, o comando retorna apenas o nome do arquivo `relatorio.txt`, removendo o caminho anterior.

### Exemplo 2: Removendo um sufixo
```bash
basename /home/usuario/documentos/relatorio.txt .txt
```
**Saída:**
```
relatorio
```
Aqui, o comando remove o sufixo `.txt`, retornando apenas o nome do arquivo sem a extensão.

## Tips
- Utilize `basename` em scripts para facilitar o processamento de arquivos, especialmente quando você precisa trabalhar apenas com os nomes dos arquivos.
- Combine `basename` com outros comandos, como `find` ou `ls`, para manipular listas de arquivos de forma mais eficiente.
- Lembre-se de que o `basename` não altera os arquivos ou diretórios; ele apenas retorna o nome base, tornando-o seguro para uso em scripts.
# [리눅스] Bash stat 사용법

## Overview
O comando `stat` é uma ferramenta do Bash utilizada para exibir informações detalhadas sobre arquivos e diretórios no sistema de arquivos. Ele fornece dados como o tamanho do arquivo, permissões, proprietário, grupo, data de criação, data de modificação e data de acesso, entre outras informações. O `stat` é especialmente útil para desenvolvedores e engenheiros que precisam verificar atributos de arquivos de forma rápida e eficiente.

## Usage
A sintaxe básica do comando `stat` é a seguinte:

```bash
stat [opções] [arquivo]
```

### Opções Comuns:
- `-c` ou `--format`: Permite especificar um formato de saída personalizado.
- `-f` ou `--file-system`: Exibe informações sobre o sistema de arquivos em vez de um arquivo específico.
- `--help`: Mostra uma mensagem de ajuda com informações sobre o uso do comando.
- `--version`: Exibe a versão do comando `stat`.

## Examples
Aqui estão alguns exemplos práticos de como usar o comando `stat`:

1. **Exibir informações padrão de um arquivo**:
   ```bash
   stat arquivo.txt
   ```
   Este comando mostrará informações detalhadas sobre `arquivo.txt`, incluindo tamanho, permissões e datas.

2. **Usar formato personalizado**:
   ```bash
   stat -c 'Tamanho: %s bytes, Modificado em: %y' arquivo.txt
   ```
   Neste exemplo, o comando exibe apenas o tamanho do arquivo em bytes e a data da última modificação, utilizando um formato personalizado.

## Tips
- Utilize a opção `-c` para personalizar a saída do `stat` e facilitar a leitura das informações que você precisa.
- Combine o `stat` com outros comandos, como `grep`, para filtrar informações específicas.
- Sempre verifique as permissões do arquivo, especialmente ao trabalhar em ambientes de desenvolvimento colaborativos, para evitar problemas de acesso.

Com essas informações, você pode utilizar o comando `stat` de forma eficaz para obter detalhes sobre arquivos e diretórios no seu sistema.
# [리눅스] Bash mv 사용법

## Overview
O comando `mv` é utilizado no sistema operacional Linux para mover arquivos e diretórios de um local para outro. Além de mover, ele também pode ser usado para renomear arquivos e diretórios. É uma ferramenta essencial para a organização e gestão de arquivos em ambientes de desenvolvimento e engenharia.

## Usage
A sintaxe básica do comando `mv` é a seguinte:

```bash
mv [opções] origem destino
```

### Opções Comuns:
- `-i`: Pergunta antes de sobrescrever um arquivo existente.
- `-u`: Move apenas se o arquivo de origem for mais recente que o arquivo de destino ou se o arquivo de destino não existir.
- `-v`: Exibe o que está sendo feito, mostrando os arquivos que estão sendo movidos.
- `-n`: Não sobrescreve arquivos existentes.

## Examples
### Exemplo 1: Mover um arquivo
Para mover um arquivo chamado `documento.txt` do diretório atual para um diretório chamado `backup`, você pode usar o seguinte comando:

```bash
mv documento.txt backup/
```

### Exemplo 2: Renomear um arquivo
Para renomear um arquivo de `relatorio.txt` para `relatorio_final.txt`, você pode usar:

```bash
mv relatorio.txt relatorio_final.txt
```

## Tips
- Sempre use a opção `-i` se você estiver preocupado em sobrescrever arquivos existentes, especialmente em ambientes de produção.
- Utilize a opção `-v` para ter um feedback visual do que está acontecendo, o que pode ser útil em scripts ou operações em lote.
- Ao mover arquivos entre sistemas de arquivos diferentes, esteja ciente de que o comando pode se comportar de maneira diferente dependendo das permissões e do espaço disponível no destino.
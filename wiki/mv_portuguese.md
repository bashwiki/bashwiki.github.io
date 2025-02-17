# [Linux] Bash mv Uso: Mover ou renomear arquivos e diretórios

## Overview
O comando `mv` é utilizado no Bash para mover ou renomear arquivos e diretórios. Ele é uma ferramenta essencial para a organização de arquivos no sistema de arquivos.

## Usage
A sintaxe básica do comando `mv` é a seguinte:

```bash
mv [opções] [origem] [destino]
```

## Common Options
Aqui estão algumas opções comuns do comando `mv`:

- `-i`: Pergunta antes de sobrescrever um arquivo existente.
- `-u`: Move apenas se o arquivo de origem for mais recente que o arquivo de destino ou se o arquivo de destino não existir.
- `-v`: Exibe os arquivos sendo movidos, mostrando o que está sendo feito.

## Common Examples

### Mover um arquivo
Para mover um arquivo chamado `documento.txt` para um diretório chamado `Documentos`, você pode usar:

```bash
mv documento.txt Documentos/
```

### Renomear um arquivo
Para renomear `documento.txt` para `novo_documento.txt`, utilize:

```bash
mv documento.txt novo_documento.txt
```

### Mover e renomear ao mesmo tempo
Para mover `documento.txt` para `Documentos` e renomeá-lo para `novo_documento.txt`, faça:

```bash
mv documento.txt Documentos/novo_documento.txt
```

### Mover vários arquivos
Para mover vários arquivos, como `arquivo1.txt` e `arquivo2.txt`, para o diretório `Documentos`, você pode usar:

```bash
mv arquivo1.txt arquivo2.txt Documentos/
```

## Tips
- Sempre use a opção `-i` se você estiver preocupado em sobrescrever arquivos existentes.
- Utilize a opção `-v` para ver um resumo das operações que estão sendo realizadas, especialmente útil em operações com muitos arquivos.
- Verifique se você tem permissões adequadas para mover ou renomear arquivos, especialmente em diretórios do sistema.
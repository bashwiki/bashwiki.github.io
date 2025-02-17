# [Linux] Bash rar uso: Comprimir e descomprimir arquivos

## Overview
O comando `rar` é utilizado para criar e manipular arquivos no formato RAR, que é um formato de compressão de dados. Ele permite compactar arquivos para economizar espaço em disco e facilitar o compartilhamento.

## Usage
A sintaxe básica do comando `rar` é a seguinte:

```bash
rar [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `rar`:

- `a`: Adiciona arquivos a um arquivo RAR existente.
- `x`: Extrai arquivos de um arquivo RAR.
- `t`: Testa a integridade dos arquivos em um arquivo RAR.
- `v`: Exibe informações detalhadas durante a execução do comando.
- `r`: Adiciona arquivos recursivamente de diretórios.

## Common Examples

### Criar um arquivo RAR
Para criar um arquivo RAR chamado `meus_arquivos.rar` contendo todos os arquivos do diretório atual, use:

```bash
rar a meus_arquivos.rar *
```

### Extrair um arquivo RAR
Para extrair os arquivos de `meus_arquivos.rar` para o diretório atual, use:

```bash
rar x meus_arquivos.rar
```

### Testar um arquivo RAR
Para verificar a integridade do arquivo `meus_arquivos.rar`, execute:

```bash
rar t meus_arquivos.rar
```

### Adicionar arquivos a um arquivo RAR existente
Para adicionar um arquivo chamado `novo_arquivo.txt` ao arquivo `meus_arquivos.rar`, use:

```bash
rar a meus_arquivos.rar novo_arquivo.txt
```

## Tips
- Sempre teste a integridade dos arquivos RAR após a criação para garantir que não haja corrupção.
- Utilize a opção `v` para obter mais informações sobre o processo de compressão ou extração.
- Considere usar a compressão recursiva com a opção `r` para incluir subdiretórios ao criar arquivos RAR.
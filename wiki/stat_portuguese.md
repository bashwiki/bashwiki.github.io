# [Linux] Bash stat Uso: Exibe informações sobre arquivos e sistemas de arquivos

## Overview
O comando `stat` é utilizado para exibir informações detalhadas sobre arquivos e diretórios no sistema de arquivos. Ele fornece dados como tamanho, permissões, data de modificação e acesso, entre outros.

## Usage
A sintaxe básica do comando `stat` é a seguinte:

```bash
stat [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `stat`:

- `-c` : Formato de saída personalizado.
- `-f` : Exibe informações sobre o sistema de arquivos.
- `--format` : Permite especificar um formato de saída.
- `-L` : Seguir links simbólicos.

## Common Examples

### Exibir informações básicas de um arquivo
Para obter informações detalhadas sobre um arquivo específico, você pode usar:

```bash
stat arquivo.txt
```

### Usar formato personalizado
Para exibir apenas o tamanho do arquivo em bytes, utilize:

```bash
stat -c %s arquivo.txt
```

### Informações sobre o sistema de arquivos
Para visualizar informações sobre o sistema de arquivos onde um arquivo está localizado, use:

```bash
stat -f arquivo.txt
```

### Seguir links simbólicos
Para obter informações sobre o arquivo que um link simbólico aponta, utilize:

```bash
stat -L link_simbólico
```

## Tips
- Utilize a opção `-c` para personalizar a saída e obter apenas as informações que você precisa.
- Combine o comando `stat` com outros comandos, como `grep`, para filtrar informações específicas.
- Lembre-se de que `stat` pode ser útil para scripts de automação, onde você precisa verificar propriedades de arquivos antes de realizar operações.
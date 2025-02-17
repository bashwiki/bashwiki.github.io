# [Linux] Bash unxz Uso: Descompactar arquivos .xz

## Overview
O comando `unxz` é utilizado para descompactar arquivos que estão no formato `.xz`. Este formato é um método de compressão que oferece alta taxa de compressão, sendo bastante utilizado em sistemas Linux para reduzir o tamanho de arquivos.

## Usage
A sintaxe básica do comando `unxz` é a seguinte:

```bash
unxz [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o comando `unxz`:

- `-k`, `--keep`: Mantém o arquivo original após a descompactação.
- `-f`, `--force`: Força a descompactação, sobrescrevendo arquivos existentes sem pedir confirmação.
- `-v`, `--verbose`: Exibe informações detalhadas sobre o processo de descompactação.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `unxz`:

1. **Descompactar um arquivo .xz**:
   ```bash
   unxz arquivo.xz
   ```

2. **Descompactar e manter o arquivo original**:
   ```bash
   unxz -k arquivo.xz
   ```

3. **Forçar a descompactação, sobrescrevendo arquivos existentes**:
   ```bash
   unxz -f arquivo.xz
   ```

4. **Descompactar um arquivo e exibir informações detalhadas**:
   ```bash
   unxz -v arquivo.xz
   ```

## Tips
- Sempre verifique se você tem espaço suficiente em disco antes de descompactar arquivos grandes.
- Utilize a opção `-k` se você quiser manter o arquivo original, especialmente se não tiver certeza se a descompactação será bem-sucedida.
- Para descompactar vários arquivos ao mesmo tempo, você pode usar um wildcard, como `*.xz`, para descompactar todos os arquivos `.xz` no diretório atual:
  ```bash
  unxz *.xz
  ```
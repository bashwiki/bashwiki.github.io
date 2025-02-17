# [Linux] Bash lsblk Uso: Exibir informações sobre dispositivos de bloco

## Overview
O comando `lsblk` é utilizado para listar informações sobre todos os dispositivos de bloco disponíveis no sistema, como discos rígidos, partições e dispositivos de armazenamento removíveis. Ele exibe detalhes como o nome do dispositivo, tamanho, tipo e ponto de montagem, facilitando a visualização da estrutura de armazenamento do sistema.

## Usage
A sintaxe básica do comando `lsblk` é a seguinte:

```bash
lsblk [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o `lsblk`:

- `-a`, `--all`: Exibe todos os dispositivos, incluindo aqueles que não estão montados.
- `-f`, `--fs`: Mostra informações sobre o sistema de arquivos, como tipo e rótulo.
- `-l`, `--list`: Exibe a saída em formato de lista, em vez de árvore.
- `-o`, `--output`: Permite especificar quais colunas exibir na saída.
- `-p`, `--paths`: Exibe os caminhos completos dos dispositivos.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `lsblk`:

1. **Listar todos os dispositivos de bloco:**

   ```bash
   lsblk
   ```

2. **Listar todos os dispositivos, incluindo os não montados:**

   ```bash
   lsblk -a
   ```

3. **Exibir informações sobre o sistema de arquivos:**

   ```bash
   lsblk -f
   ```

4. **Listar dispositivos em formato de lista:**

   ```bash
   lsblk -l
   ```

5. **Especificar colunas a serem exibidas:**

   ```bash
   lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
   ```

## Tips
- Utilize a opção `-f` para obter informações detalhadas sobre o sistema de arquivos, o que pode ser útil para identificar partições.
- Combine `lsblk` com outros comandos, como `grep`, para filtrar a saída e encontrar dispositivos específicos.
- Para uma visualização mais clara, considere usar a opção `-p` para ver os caminhos completos dos dispositivos, especialmente em sistemas com múltiplos discos.
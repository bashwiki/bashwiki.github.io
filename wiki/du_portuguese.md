# [Linux] Bash du Uso: Exibir o uso de espaço em disco

## Overview
O comando `du` (disk usage) é utilizado para estimar e relatar o uso de espaço em disco de arquivos e diretórios no sistema de arquivos. Ele fornece informações sobre o tamanho dos arquivos e diretórios, ajudando os usuários a entender como o espaço em disco está sendo utilizado.

## Usage
A sintaxe básica do comando `du` é a seguinte:

```bash
du [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `du`:

- `-h`: Exibe os tamanhos em um formato legível por humanos (por exemplo, KB, MB).
- `-s`: Mostra apenas o total para cada argumento, em vez de listar todos os arquivos e subdiretórios.
- `-a`: Inclui arquivos individuais na saída, além de diretórios.
- `-c`: Fornece um total cumulativo no final da saída.
- `--max-depth=N`: Limita a profundidade da listagem de diretórios a N níveis.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `du`:

1. **Ver o uso de espaço em disco de um diretório:**
   ```bash
   du /caminho/para/diretorio
   ```

2. **Ver o uso de espaço em disco de um diretório em formato legível:**
   ```bash
   du -h /caminho/para/diretorio
   ```

3. **Obter o total de espaço usado por um diretório:**
   ```bash
   du -sh /caminho/para/diretorio
   ```

4. **Listar o uso de espaço de todos os arquivos e diretórios em um diretório:**
   ```bash
   du -ah /caminho/para/diretorio
   ```

5. **Limitar a profundidade da listagem a 1 nível:**
   ```bash
   du --max-depth=1 -h /caminho/para/diretorio
   ```

## Tips
- Utilize a opção `-h` para facilitar a leitura dos tamanhos, especialmente em diretórios grandes.
- Combine `-s` com `-c` para obter um resumo total de vários diretórios.
- Para uma análise mais detalhada, a opção `-a` pode ser muito útil, pois inclui todos os arquivos.
- Lembre-se de que o comando `du` pode levar algum tempo para ser executado em diretórios muito grandes ou com muitos arquivos.
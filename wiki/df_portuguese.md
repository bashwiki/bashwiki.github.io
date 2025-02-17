# [Linux] Bash df Uso: Exibir informações sobre o uso do sistema de arquivos

## Overview
O comando `df` é utilizado para exibir informações sobre o espaço em disco disponível e utilizado em sistemas de arquivos montados. Ele fornece uma visão geral do uso do armazenamento em um sistema, permitindo que os usuários monitorem a capacidade de disco.

## Usage
A sintaxe básica do comando `df` é a seguinte:

```bash
df [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `df`:

- `-h`: Exibe os tamanhos em um formato legível por humanos (ex: KB, MB, GB).
- `-T`: Mostra o tipo de sistema de arquivos.
- `-a`: Inclui sistemas de arquivos com 0 blocos.
- `-i`: Exibe informações sobre o uso de inodes em vez de blocos.

## Common Examples

1. **Exibir informações básicas sobre todos os sistemas de arquivos:**
   ```bash
   df
   ```

2. **Exibir informações em um formato legível por humanos:**
   ```bash
   df -h
   ```

3. **Mostrar o tipo de sistema de arquivos:**
   ```bash
   df -T
   ```

4. **Incluir sistemas de arquivos com 0 blocos:**
   ```bash
   df -a
   ```

5. **Exibir informações sobre o uso de inodes:**
   ```bash
   df -i
   ```

## Tips
- Utilize a opção `-h` para facilitar a leitura dos resultados, especialmente em sistemas com grandes volumes de dados.
- Combine opções, como `df -hT`, para obter uma visão mais detalhada e legível dos sistemas de arquivos.
- Regularmente verifique o uso do disco para evitar problemas de espaço, especialmente em servidores e sistemas críticos.
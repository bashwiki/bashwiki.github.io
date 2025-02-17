# [Linux] Bash lspci Uso: Exibir informações sobre dispositivos PCI

## Overview
O comando `lspci` é utilizado para listar todos os dispositivos conectados ao barramento PCI (Peripheral Component Interconnect) do sistema. Ele fornece informações detalhadas sobre cada dispositivo, incluindo o fabricante, o modelo e o tipo de dispositivo.

## Usage
A sintaxe básica do comando `lspci` é a seguinte:

```bash
lspci [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o `lspci`:

- `-v`: Exibe informações detalhadas sobre cada dispositivo.
- `-vv`: Fornece ainda mais detalhes do que a opção `-v`.
- `-k`: Mostra os módulos do kernel associados a cada dispositivo.
- `-n`: Exibe os IDs de fornecedor e dispositivo em formato numérico.
- `-s <slot>`: Filtra a saída para mostrar apenas o dispositivo no slot especificado.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `lspci`:

1. **Listar todos os dispositivos PCI:**
   ```bash
   lspci
   ```

2. **Listar dispositivos com informações detalhadas:**
   ```bash
   lspci -v
   ```

3. **Listar dispositivos com módulos do kernel associados:**
   ```bash
   lspci -k
   ```

4. **Listar dispositivos em formato numérico:**
   ```bash
   lspci -n
   ```

5. **Filtrar para um dispositivo específico:**
   ```bash
   lspci -s 00:1f.0
   ```

## Tips
- Use a opção `-v` para obter mais informações sobre os dispositivos, especialmente se você estiver solucionando problemas de hardware.
- Combine opções, como `lspci -vv -k`, para obter uma visão abrangente dos dispositivos e seus módulos do kernel.
- Se você estiver procurando por um dispositivo específico, use a opção `-s` para filtrar a saída e facilitar a localização.
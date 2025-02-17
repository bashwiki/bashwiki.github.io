# [Linux] Bash lsusb Uso: Exibir informações sobre dispositivos USB conectados

## Overview
O comando `lsusb` é utilizado para listar todos os dispositivos USB conectados ao sistema. Ele fornece informações detalhadas sobre cada dispositivo, como o fabricante, o produto e o ID do dispositivo, permitindo que os usuários identifiquem e gerenciem dispositivos USB de forma eficiente.

## Usage
A sintaxe básica do comando `lsusb` é a seguinte:

```bash
lsusb [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `lsusb`:

- `-v`: Exibe informações detalhadas sobre os dispositivos USB.
- `-t`: Mostra a árvore de dispositivos USB, permitindo visualizar a hierarquia dos dispositivos conectados.
- `-s [bus]:[device]`: Filtra a saída para mostrar apenas o dispositivo especificado pelo número do barramento e do dispositivo.
- `-d [idVendor]:[idProduct]`: Filtra a saída para mostrar apenas os dispositivos que correspondem ao ID do fabricante e do produto.

## Common Examples

1. **Listar todos os dispositivos USB conectados:**
   ```bash
   lsusb
   ```

2. **Exibir informações detalhadas sobre todos os dispositivos USB:**
   ```bash
   lsusb -v
   ```

3. **Mostrar a árvore de dispositivos USB:**
   ```bash
   lsusb -t
   ```

4. **Filtrar para mostrar um dispositivo específico:**
   ```bash
   lsusb -s 001:002
   ```

5. **Filtrar por ID do fabricante e do produto:**
   ```bash
   lsusb -d 1234:5678
   ```

## Tips
- Utilize a opção `-v` com cautela, pois a saída pode ser extensa e difícil de interpretar. Considere redirecionar a saída para um arquivo para análise posterior.
- Combine `lsusb` com outros comandos, como `grep`, para filtrar informações específicas. Por exemplo:
  ```bash
  lsusb | grep "Logitech"
  ```
- Familiarize-se com os IDs dos dispositivos USB, pois eles podem ser úteis para resolver problemas de compatibilidade ou para identificar dispositivos desconhecidos.
# [Linux] Bash free uso: Exibir informações sobre a memória

## Overview
O comando `free` é utilizado para exibir informações sobre a memória do sistema, incluindo a memória total, usada, livre e buffers/cache. É uma ferramenta útil para monitorar o uso da memória em sistemas Linux.

## Usage
A sintaxe básica do comando `free` é a seguinte:

```bash
free [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `free`:

- `-h` : Exibe os valores em um formato legível por humanos (com unidades como KB, MB ou GB).
- `-m` : Exibe a memória em megabytes.
- `-g` : Exibe a memória em gigabytes.
- `-s [segundos]` : Atualiza a saída a cada número especificado de segundos.
- `-t` : Mostra a linha total de memória.

## Common Examples

### Exibir informações básicas sobre a memória
```bash
free
```

### Exibir informações em um formato legível por humanos
```bash
free -h
```

### Exibir informações em megabytes
```bash
free -m
```

### Exibir informações em gigabytes
```bash
free -g
```

### Atualizar a saída a cada 5 segundos
```bash
free -s 5
```

### Exibir a linha total de memória
```bash
free -t
```

## Tips
- Use a opção `-h` para facilitar a leitura dos dados, especialmente em sistemas com grandes quantidades de memória.
- Combine o comando `free` com outros comandos como `watch` para monitorar o uso da memória em tempo real:
  ```bash
  watch free -h
  ```
- Lembre-se de que o valor de "memória livre" pode não refletir a memória realmente disponível para novos processos, devido ao uso de buffers e cache pelo sistema.
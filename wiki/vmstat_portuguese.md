# [Linux] Bash vmstat Uso: Monitora o desempenho do sistema

## Overview
O comando `vmstat` (Virtual Memory Statistics) é utilizado para monitorar o desempenho do sistema em tempo real. Ele fornece informações sobre processos, memória, troca, I/O e CPU, permitindo que os administradores de sistema identifiquem gargalos e analisem o comportamento do sistema.

## Usage
A sintaxe básica do comando `vmstat` é a seguinte:

```bash
vmstat [opções] [intervalo] [contagem]
```

## Common Options
Aqui estão algumas opções comuns do `vmstat`:

- `-a`: Exibe informações sobre memória ativa e inativa.
- `-m`: Mostra estatísticas de memória de páginas.
- `-s`: Exibe um resumo das estatísticas de memória.
- `-d`: Mostra estatísticas de dispositivos de bloco.
- `intervalo`: Define o intervalo em segundos entre as atualizações.
- `contagem`: Especifica quantas vezes o comando deve ser executado.

## Common Examples

1. **Exibir estatísticas padrão:**
   ```bash
   vmstat
   ```

2. **Monitorar o sistema a cada 2 segundos por 5 vezes:**
   ```bash
   vmstat 2 5
   ```

3. **Mostrar estatísticas de memória ativa e inativa:**
   ```bash
   vmstat -a
   ```

4. **Exibir um resumo das estatísticas de memória:**
   ```bash
   vmstat -s
   ```

5. **Mostrar estatísticas de dispositivos de bloco:**
   ```bash
   vmstat -d
   ```

## Tips
- Utilize `vmstat` em conjunto com outros comandos, como `top` e `iostat`, para uma análise mais abrangente do desempenho do sistema.
- Experimente diferentes intervalos e contagens para observar como o sistema se comporta sob diferentes cargas.
- Salve a saída do `vmstat` em um arquivo para análise posterior usando a redireção, por exemplo:
  ```bash
  vmstat 2 5 > vmstat_output.txt
  ```
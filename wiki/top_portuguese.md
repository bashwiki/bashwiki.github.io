# [Linux] Bash top uso: Monitore o desempenho do sistema

## Overview
O comando `top` é uma ferramenta de monitoramento em tempo real que exibe informações sobre os processos em execução no sistema. Ele fornece uma visão geral do uso de CPU, memória e outros recursos, permitindo que os usuários identifiquem quais processos estão consumindo mais recursos.

## Usage
A sintaxe básica do comando `top` é a seguinte:

```bash
top [opções]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `top`:

- `-d <tempo>`: Define o intervalo de atualização em segundos.
- `-n <número>`: Especifica o número de iterações a serem exibidas antes de sair.
- `-u <usuário>`: Filtra os processos para mostrar apenas os pertencentes ao usuário especificado.
- `-p <PID>`: Monitora apenas o processo com o ID especificado.

## Common Examples

1. **Executar o top com atualização a cada 2 segundos:**
   ```bash
   top -d 2
   ```

2. **Mostrar apenas os processos de um usuário específico:**
   ```bash
   top -u nome_do_usuario
   ```

3. **Monitorar um processo específico pelo seu PID:**
   ```bash
   top -p 1234
   ```

4. **Executar o top por um número específico de iterações:**
   ```bash
   top -n 5
   ```

## Tips
- Use a tecla `h` enquanto o `top` está em execução para acessar a ajuda e ver os comandos de atalho disponíveis.
- Para sair do `top`, pressione `q`.
- Você pode ordenar os processos por diferentes critérios, como uso de CPU ou memória, pressionando as teclas correspondentes enquanto o `top` está em execução (por exemplo, `P` para CPU e `M` para memória).
- Considere usar o comando `htop` como uma alternativa mais visual e interativa ao `top`, se estiver disponível no seu sistema.
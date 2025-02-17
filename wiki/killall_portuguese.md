# [Linux] Bash killall Uso: Finaliza processos pelo nome

## Overview
O comando `killall` é utilizado para finalizar processos em execução com base no nome do processo. Isso permite que os usuários encerrem facilmente múltiplos processos que compartilham o mesmo nome, sem a necessidade de identificar cada ID de processo individualmente.

## Usage
A sintaxe básica do comando `killall` é a seguinte:

```bash
killall [opções] [nome_do_processo]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `killall`:

- `-u [usuário]`: Finaliza apenas os processos pertencentes ao usuário especificado.
- `-i`: Solicita confirmação antes de finalizar cada processo.
- `-q`: Não exibe mensagens de erro se não houver processos correspondentes.
- `-s [sinal]`: Especifica o sinal a ser enviado ao processo (por exemplo, `-s SIGKILL`).

## Common Examples
Aqui estão alguns exemplos práticos do uso do `killall`:

1. Finalizar todos os processos do Firefox:
   ```bash
   killall firefox
   ```

2. Finalizar todos os processos do usuário "joao":
   ```bash
   killall -u joao
   ```

3. Enviar um sinal específico (SIGTERM) para todos os processos do nome "myapp":
   ```bash
   killall -s SIGTERM myapp
   ```

4. Usar a opção interativa para confirmar antes de finalizar cada processo:
   ```bash
   killall -i firefox
   ```

5. Finalizar todos os processos do nome "myservice" sem mensagens de erro:
   ```bash
   killall -q myservice
   ```

## Tips
- Sempre verifique quais processos estão em execução antes de usar `killall`, para evitar encerrar processos importantes acidentalmente.
- Utilize a opção `-i` para ter um controle adicional ao finalizar processos, especialmente em ambientes de produção.
- Combine `killall` com outros comandos, como `ps`, para listar processos antes de decidir qual finalizar.
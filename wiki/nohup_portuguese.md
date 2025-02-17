# [Linux] Bash nohup uso: Executar comandos sem interrupção

## Overview
O comando `nohup` (no hang up) é utilizado para executar processos em segundo plano, permitindo que eles continuem rodando mesmo após o usuário sair da sessão ou fechar o terminal. Isso é especialmente útil para longas tarefas que não devem ser interrompidas.

## Usage
A sintaxe básica do comando `nohup` é a seguinte:

```bash
nohup [opções] [comando] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `nohup`:

- `&`: Coloca o comando em segundo plano.
- `-h`: Exibe a ajuda do comando.
- `-v`: Exibe a versão do comando.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `nohup`:

1. Executar um script em segundo plano:
   ```bash
   nohup ./meu_script.sh &
   ```

2. Rodar um comando de backup sem interrupções:
   ```bash
   nohup tar -czf backup.tar.gz /pasta/importante &
   ```

3. Executar um servidor web em segundo plano:
   ```bash
   nohup python -m http.server 8000 &
   ```

4. Redirecionar a saída para um arquivo:
   ```bash
   nohup ./meu_programa > saida.log 2>&1 &
   ```

## Tips
- Sempre redirecione a saída para um arquivo para evitar que a saída padrão seja enviada para `/dev/null`.
- Use `jobs` para verificar os processos em segundo plano.
- Combine `nohup` com `disown` para garantir que o processo não seja encerrado ao sair do terminal.
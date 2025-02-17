# [Linux] Bash command uso: [executar comandos em segundo plano]

## Overview
O comando `nohup` é utilizado para executar processos em segundo plano, permitindo que eles continuem rodando mesmo após o usuário sair da sessão. Isso é especialmente útil para longas tarefas que não precisam de interação contínua.

## Usage
A sintaxe básica do comando `nohup` é a seguinte:

```bash
nohup comando [opções] [argumentos] &
```

## Common Options
- `&`: Coloca o comando em segundo plano.
- `-p`: Permite que você especifique um PID (Process ID) para o comando.
- `-n`: Ignora a saída padrão, redirecionando-a para `/dev/null`.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `nohup`:

1. Executar um script em segundo plano:
   ```bash
   nohup ./meu_script.sh &
   ```

2. Rodar um comando de backup sem se preocupar com a sessão:
   ```bash
   nohup tar -czf backup.tar.gz /pasta/para/backup &
   ```

3. Executar um servidor web em segundo plano:
   ```bash
   nohup python -m http.server 8000 &
   ```

4. Executar um comando e redirecionar a saída para um arquivo:
   ```bash
   nohup long_running_command > output.log &
   ```

## Tips
- Sempre use `&` ao final do comando para garantir que ele seja executado em segundo plano.
- Verifique o arquivo `nohup.out` para mensagens de saída e erros, caso não tenha redirecionado a saída.
- Utilize `jobs` para listar os processos em segundo plano e `fg` para trazê-los de volta para o primeiro plano, se necessário.
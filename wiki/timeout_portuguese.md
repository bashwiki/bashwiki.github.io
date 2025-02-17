# [Linux] Bash timeout uso: Limitar a duração de um comando

## Overview
O comando `timeout` é utilizado para executar um comando e limitar o tempo que ele pode ser executado. Se o comando não terminar dentro do período especificado, o `timeout` o encerra automaticamente.

## Usage
A sintaxe básica do comando é a seguinte:

```bash
timeout [opções] DURAÇÃO COMANDO [argumentos]
```

## Common Options
- `-s, --signal SIGNAL`: Especifica o sinal a ser enviado ao comando quando o tempo expira. O padrão é `SIGTERM`.
- `-k, --kill-after DURAÇÃO`: Após o tempo limite, espera a duração especificada antes de enviar um sinal de término forçado.
- `--preserve-status`: Mantém o código de saída do comando original em vez de retornar o código de saída do `timeout`.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `timeout`:

1. **Executar um comando com limite de tempo de 5 segundos:**
   ```bash
   timeout 5s sleep 10
   ```
   Neste exemplo, o comando `sleep 10` será interrompido após 5 segundos.

2. **Usar um sinal específico ao expirar o tempo:**
   ```bash
   timeout -s SIGKILL 3s sleep 10
   ```
   Aqui, o comando `sleep 10` será forçado a terminar com o sinal `SIGKILL` após 3 segundos.

3. **Manter o código de saída do comando original:**
   ```bash
   timeout --preserve-status 2s ls /nonexistent
   ```
   Neste caso, o comando `ls` será executado, mas como não existe o diretório, o código de saída será mantido mesmo que o `timeout` expire.

4. **Usar o `kill-after` para dar um tempo extra antes de forçar a finalização:**
   ```bash
   timeout -k 2s 5s sleep 10
   ```
   O comando `sleep 10` será interrompido após 5 segundos, mas o `timeout` aguardará mais 2 segundos antes de enviar um sinal de término forçado.

## Tips
- Sempre teste seus comandos com `timeout` em um ambiente seguro para evitar a perda de dados.
- Use a opção `--preserve-status` se precisar capturar o resultado do comando original.
- Combine `timeout` com outros comandos em scripts para garantir que processos longos não travem o sistema.
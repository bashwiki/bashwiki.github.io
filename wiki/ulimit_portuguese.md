# [Linux] Bash ulimit Uso: Limitar recursos do sistema

## Overview
O comando `ulimit` é utilizado em sistemas Unix e Linux para definir ou exibir limites de recursos disponíveis para o shell e os processos que ele cria. Esses limites ajudam a evitar que um único usuário ou processo consuma todos os recursos do sistema, garantindo uma melhor estabilidade e desempenho.

## Usage
A sintaxe básica do comando `ulimit` é a seguinte:

```bash
ulimit [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `ulimit`:

- `-a`: Exibe todos os limites atuais.
- `-c`: Define o tamanho máximo do arquivo de core (em bytes).
- `-d`: Define o tamanho máximo da memória de dados (em kilobytes).
- `-f`: Define o tamanho máximo dos arquivos que podem ser criados (em blocks).
- `-l`: Define o tamanho máximo da memória bloqueada (em bytes).
- `-m`: Define o tamanho máximo da memória residente (em kilobytes).
- `-n`: Define o número máximo de descritores de arquivo que podem ser abertos.
- `-s`: Define o tamanho máximo da pilha (em kilobytes).
- `-t`: Define o tempo máximo de CPU que um processo pode usar (em segundos).
- `-u`: Define o número máximo de processos que um usuário pode criar.

## Common Examples

Aqui estão alguns exemplos práticos do uso do comando `ulimit`:

1. **Exibir todos os limites atuais:**
   ```bash
   ulimit -a
   ```

2. **Definir o número máximo de descritores de arquivo:**
   ```bash
   ulimit -n 1024
   ```

3. **Definir o tamanho máximo de arquivos que podem ser criados:**
   ```bash
   ulimit -f 2048
   ```

4. **Definir o tamanho máximo da pilha:**
   ```bash
   ulimit -s 8192
   ```

5. **Definir o tempo máximo de CPU para um processo:**
   ```bash
   ulimit -t 60
   ```

## Tips
- Sempre verifique os limites atuais com `ulimit -a` antes de fazer alterações.
- Use `ulimit` com cautela, pois definir limites muito baixos pode impedir que aplicações funcionem corretamente.
- Para aplicar limites de forma permanente, edite o arquivo de configuração do shell, como `~/.bashrc` ou `/etc/security/limits.conf`.
- Lembre-se de que algumas opções podem exigir privilégios de superusuário para serem alteradas.
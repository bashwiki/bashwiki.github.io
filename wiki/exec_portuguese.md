# [Linux] Bash exec uso equivalente: Executar comandos em um novo processo

## Overview
O comando `exec` no Bash é utilizado para substituir o shell atual por um novo comando, permitindo que você execute um programa sem criar um novo processo. Isso é útil para economizar recursos e para situações em que você deseja que o novo comando assuma o controle total do terminal.

## Usage
A sintaxe básica do comando `exec` é a seguinte:

```bash
exec [opções] [comando] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `exec`:

- `-a nome`: Permite especificar um nome diferente para o comando que será executado.
- `-l`: Faz com que o comando seja executado como um login shell.
- `-p`: Preserva o ambiente do shell atual.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `exec`:

1. **Substituir o shell atual por um novo comando:**
   ```bash
   exec ls -l
   ```
   Neste exemplo, o shell atual será substituído pelo comando `ls -l`, listando os arquivos no diretório atual.

2. **Executar um script em vez do shell atual:**
   ```bash
   exec ./meu_script.sh
   ```
   Aqui, o shell atual é substituído pelo script `meu_script.sh`, e após a execução, não retornará ao shell original.

3. **Executar um comando com um nome diferente:**
   ```bash
   exec -a novo_nome /bin/bash
   ```
   Este comando executa o Bash, mas o nome do processo será exibido como `novo_nome`.

4. **Executar um comando como um login shell:**
   ```bash
   exec -l /bin/bash
   ```
   Isso inicia um novo shell Bash como um login shell, que pode ser útil para redefinir variáveis de ambiente.

## Tips
- Use `exec` quando você não precisa retornar ao shell original, pois ele substitui o processo atual.
- Tenha cuidado ao usar `exec` em scripts, pois uma vez que o comando é executado, o script não continuará após essa linha.
- Para depuração, considere usar `set -x` antes de um comando `exec` para visualizar os comandos que estão sendo executados.
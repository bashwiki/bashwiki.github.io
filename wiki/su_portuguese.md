# [Linux] Bash su Uso: Mudar de usuário no terminal

## Overview
O comando `su` (substitute user) é utilizado no Linux para mudar de usuário no terminal. Ele permite que um usuário comum assuma a identidade de outro usuário, geralmente o usuário root, para executar comandos com privilégios elevados.

## Usage
A sintaxe básica do comando `su` é a seguinte:

```bash
su [opções] [usuário]
```

Se o usuário não for especificado, o `su` tentará mudar para o usuário root por padrão.

## Common Options
- `-l` ou `--login`: Inicia uma sessão de login como o usuário especificado.
- `-c`: Permite executar um comando específico como o usuário indicado.
- `-s`: Especifica um shell diferente para a nova sessão.
- `-m` ou `--preserve-environment`: Preserva o ambiente do usuário atual.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `su`:

1. Mudar para o usuário root:
   ```bash
   su
   ```

2. Mudar para um usuário específico (por exemplo, `usuario1`):
   ```bash
   su usuario1
   ```

3. Executar um comando como root (por exemplo, atualizar o sistema):
   ```bash
   su -c "apt update && apt upgrade"
   ```

4. Iniciar uma sessão de login como um usuário específico:
   ```bash
   su - usuario1
   ```

5. Mudar para um shell diferente (por exemplo, `/bin/bash`):
   ```bash
   su -s /bin/bash usuario1
   ```

## Tips
- Sempre use `su` com cautela, especialmente ao mudar para o usuário root, pois você pode fazer alterações críticas no sistema.
- Considere usar `sudo` em vez de `su` para executar comandos específicos com privilégios elevados, pois isso pode ser mais seguro e conveniente.
- Lembre-se de que, ao usar `su`, você precisará fornecer a senha do usuário para o qual está mudando.
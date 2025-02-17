# [Linux] Bash last uso: Exibir logins de usuários

## Overview
O comando `last` é utilizado para exibir uma lista dos últimos logins de usuários no sistema. Ele lê o arquivo de log `/var/log/wtmp`, que registra todas as entradas e saídas dos usuários, permitindo que você veja quem acessou o sistema e quando.

## Usage
A sintaxe básica do comando `last` é a seguinte:

```bash
last [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o comando `last`:

- `-a`: Mostra o nome do host da máquina remota.
- `-n <número>`: Limita a saída aos últimos `número` de logins.
- `-x`: Exibe também as sessões de encerramento e reinicializações do sistema.
- `-R`: Não exibe o nome do host.

## Common Examples

Aqui estão alguns exemplos práticos do uso do comando `last`:

1. **Exibir todos os logins**:
   ```bash
   last
   ```

2. **Limitar a saída aos últimos 5 logins**:
   ```bash
   last -n 5
   ```

3. **Mostrar logins com o nome do host**:
   ```bash
   last -a
   ```

4. **Incluir sessões de encerramento e reinicializações**:
   ```bash
   last -x
   ```

5. **Exibir logins sem o nome do host**:
   ```bash
   last -R
   ```

## Tips
- Utilize `last` em combinação com outros comandos, como `grep`, para filtrar resultados específicos. Por exemplo, para encontrar logins de um usuário específico:
  ```bash
  last | grep nome_do_usuario
  ```
- Verifique regularmente os logs de login para monitorar atividades suspeitas no sistema.
- Lembre-se de que o arquivo `/var/log/wtmp` pode ser rotacionado, então os dados mais antigos podem não estar disponíveis.
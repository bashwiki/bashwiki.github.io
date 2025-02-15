# [리눅스] Bash last 사용법

## Overview
O comando `last` é uma ferramenta do Bash utilizada para exibir uma lista dos usuários que se conectaram e desconectaram do sistema. Ele lê o arquivo de log `/var/log/wtmp`, que registra todas as sessões de login e logout, permitindo que os administradores e desenvolvedores monitorem a atividade dos usuários no sistema.

## Usage
A sintaxe básica do comando `last` é a seguinte:

```bash
last [opções] [usuário]
```

### Opções Comuns:
- `-a`: Mostra o nome do host remoto na saída.
- `-n [número]`: Limita o número de entradas exibidas a `[número]`.
- `-x`: Exibe também as entradas de shutdown e reboot.
- `-R`: Não mostra o nome do host remoto.

## Examples
### Exemplo 1: Listar todas as sessões de login
Para visualizar todas as sessões de login registradas, você pode simplesmente executar:

```bash
last
```

Este comando retornará uma lista de usuários que se conectaram ao sistema, incluindo informações como o terminal utilizado, o endereço IP (se aplicável), e as datas e horários de login e logout.

### Exemplo 2: Limitar a saída a 5 entradas
Se você quiser ver apenas as últimas 5 sessões de login, utilize a opção `-n`:

```bash
last -n 5
```

Isso mostrará as cinco entradas mais recentes do log de sessões.

## Tips
- Utilize a opção `-a` para facilitar a identificação de onde os usuários estão se conectando, especialmente útil em ambientes com múltiplos servidores.
- Combine o comando `last` com `grep` para filtrar resultados específicos. Por exemplo, para encontrar todas as sessões de um usuário específico, você pode usar:

```bash
last | grep nome_do_usuario
```

- Lembre-se de que o arquivo de log `/var/log/wtmp` pode ser rotacionado, o que significa que entradas mais antigas podem não estar disponíveis se o log foi arquivado.
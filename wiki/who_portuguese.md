# [리눅스] Bash who 사용법

## Overview
O comando `who` é uma ferramenta do Bash que exibe informações sobre os usuários que estão atualmente logados no sistema. Ele fornece detalhes como o nome de usuário, terminal, data e hora do login, e, em alguns casos, o endereço IP ou hostname do usuário. O principal propósito do comando `who` é permitir que administradores e usuários vejam quem está ativo no sistema em um dado momento.

## Usage
A sintaxe básica do comando `who` é a seguinte:

```bash
who [opções]
```

### Opções Comuns:
- `-a`: Exibe todas as informações disponíveis, incluindo detalhes adicionais sobre os usuários logados.
- `-b`: Mostra a hora da última inicialização do sistema.
- `-q`: Exibe apenas os nomes dos usuários logados e a contagem total de usuários.
- `--help`: Mostra uma mensagem de ajuda com informações sobre o uso do comando.

## Examples
Aqui estão alguns exemplos práticos de como usar o comando `who`:

1. **Exibir usuários logados**:
   Para ver todos os usuários que estão atualmente logados no sistema, você pode simplesmente executar:

   ```bash
   who
   ```

   A saída mostrará uma lista de usuários, incluindo o nome do usuário, terminal, data e hora do login.

2. **Exibir informações detalhadas**:
   Para obter informações mais detalhadas sobre os usuários logados, você pode usar a opção `-a`:

   ```bash
   who -a
   ```

   Isso fornecerá uma visão mais completa, incluindo informações adicionais como o tempo de inatividade e o estado do terminal.

## Tips
- Utilize o comando `who` em conjunto com outros comandos, como `grep`, para filtrar resultados específicos. Por exemplo, para encontrar um usuário específico:

  ```bash
  who | grep nome_do_usuario
  ```

- Para monitorar a atividade dos usuários em tempo real, você pode usar o comando `watch` em conjunto com `who`:

  ```bash
  watch who
  ```

  Isso atualizará a lista de usuários logados a cada 2 segundos, permitindo que você veja as mudanças em tempo real.

- Lembre-se de que o comando `who` pode não mostrar usuários que estão logados via SSH se a sessão estiver em modo "quiet" ou se o usuário tiver configurado seu ambiente para não ser exibido.
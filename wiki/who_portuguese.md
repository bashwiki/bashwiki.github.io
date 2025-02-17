# [Linux] Bash who uso equivalente: Exibir usuários conectados

## Overview
O comando `who` é utilizado no Bash para exibir uma lista de usuários que estão atualmente conectados ao sistema. Ele fornece informações sobre os usuários, como nome de usuário, terminal, data e hora do login.

## Usage
A sintaxe básica do comando `who` é a seguinte:

```bash
who [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `who`:

- `-a`: Exibe todas as informações disponíveis, incluindo usuários conectados e detalhes adicionais.
- `-b`: Mostra a última vez que o sistema foi inicializado.
- `-q`: Exibe apenas os nomes de usuários conectados e a contagem total de usuários.
- `--help`: Mostra uma mensagem de ajuda com informações sobre o uso do comando.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `who`:

1. **Exibir todos os usuários conectados:**
   ```bash
   who
   ```

2. **Mostrar informações detalhadas sobre os usuários conectados:**
   ```bash
   who -a
   ```

3. **Ver a última inicialização do sistema:**
   ```bash
   who -b
   ```

4. **Listar apenas os nomes de usuários conectados:**
   ```bash
   who -q
   ```

## Tips
- Utilize `who` em combinação com outros comandos, como `grep`, para filtrar resultados específicos.
- Para obter informações em tempo real sobre os usuários conectados, você pode usar o comando `watch` junto com `who`:
  ```bash
  watch who
  ```
- Lembre-se de que o comando `who` pode não mostrar usuários que estão conectados via SSH se eles não tiverem um terminal associado.
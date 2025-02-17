# [Linux] Usuários Bash: Exibir informações sobre usuários do sistema

## Overview
O comando `users` é utilizado para exibir os nomes dos usuários que estão atualmente logados no sistema. Ele fornece uma visão rápida de quem está acessando a máquina no momento, sendo útil para administradores e usuários que desejam monitorar a atividade.

## Usage
A sintaxe básica do comando `users` é a seguinte:

```
users [opções]
```

## Common Options
- `-n`: Exibe apenas o número de usuários logados, sem listar os nomes.
- `-r`: Exibe apenas os usuários que estão logados em sessões remotas.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `users`:

1. **Listar usuários logados:**
   ```bash
   users
   ```

2. **Contar o número de usuários logados:**
   ```bash
   users -n
   ```

3. **Listar usuários logados remotamente:**
   ```bash
   users -r
   ```

## Tips
- Utilize o comando `who` em conjunto com `users` para obter informações mais detalhadas sobre os usuários logados, como o terminal e o horário de login.
- Para um monitoramento mais abrangente, considere usar o comando `w`, que fornece informações sobre o que os usuários estão fazendo no momento.
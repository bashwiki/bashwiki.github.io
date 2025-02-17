# [Linux] Bash id uso: exibir informações do usuário

## Overview
O comando `id` é utilizado para exibir informações sobre o usuário atual ou sobre um usuário específico. Ele fornece detalhes como o UID (User ID), GID (Group ID) e os grupos aos quais o usuário pertence.

## Usage
A sintaxe básica do comando `id` é a seguinte:

```bash
id [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `id`:

- `-u`: Exibe apenas o UID do usuário.
- `-g`: Exibe apenas o GID do grupo principal do usuário.
- `-G`: Exibe todos os GIDs dos grupos aos quais o usuário pertence.
- `-n`: Exibe os nomes em vez dos IDs numéricos.
- `-r`: Exibe o GID real em vez do GID efetivo.

## Common Examples

### Exibir informações do usuário atual
```bash
id
```

### Exibir UID do usuário atual
```bash
id -u
```

### Exibir GID do grupo principal do usuário atual
```bash
id -g
```

### Exibir todos os GIDs do usuário atual
```bash
id -G
```

### Exibir informações de um usuário específico
```bash
id nome_do_usuario
```

### Exibir nomes em vez de IDs
```bash
id -n
```

## Tips
- Utilize `id -u nome_do_usuario` para verificar rapidamente o UID de um usuário específico.
- Combine opções, como `id -Gn nome_do_usuario`, para obter uma lista dos grupos de um usuário em formato de nome.
- O comando `id` é útil para scripts que precisam verificar permissões de usuários e grupos.
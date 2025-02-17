# [Linux] Bash useradd uso: Criação de novos usuários no sistema

## Overview
O comando `useradd` é utilizado para criar novos usuários em sistemas Linux. Ele permite que administradores do sistema adicionem contas de usuário, definindo várias opções, como diretórios home e grupos.

## Usage
A sintaxe básica do comando `useradd` é a seguinte:

```bash
useradd [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `useradd`:

- `-m`: Cria um diretório home para o usuário.
- `-s`: Especifica o shell padrão do usuário.
- `-G`: Adiciona o usuário a grupos adicionais.
- `-c`: Adiciona um comentário, geralmente usado para o nome completo do usuário.
- `-r`: Cria um usuário do sistema.

## Common Examples

### Criar um usuário simples
Para criar um usuário chamado `joao`:

```bash
useradd joao
```

### Criar um usuário com diretório home
Para criar um usuário chamado `maria` com um diretório home:

```bash
useradd -m maria
```

### Criar um usuário com shell específico
Para criar um usuário chamado `pedro` com o shell `/bin/bash`:

```bash
useradd -s /bin/bash pedro
```

### Criar um usuário e adicionar a grupos
Para criar um usuário chamado `ana` e adicioná-la ao grupo `admin`:

```bash
useradd -G admin ana
```

### Criar um usuário com comentário
Para criar um usuário chamado `carlos` e adicionar um comentário:

```bash
useradd -c "Carlos Silva" carlos
```

## Tips
- Sempre verifique se o nome de usuário que você deseja criar já não existe no sistema.
- Use a opção `-m` para garantir que o usuário tenha um diretório home, o que é útil para armazenar arquivos pessoais.
- Após criar um usuário, não se esqueça de definir uma senha usando o comando `passwd [nome_do_usuario]`.
- Considere usar a opção `-r` para criar usuários do sistema que não precisam de um diretório home ou shell interativo.
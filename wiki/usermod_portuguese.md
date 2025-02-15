# [리눅스] Bash usermod 사용법

## Overview
O comando `usermod` é uma ferramenta utilizada em sistemas operacionais baseados em Unix e Linux para modificar as propriedades de uma conta de usuário existente. Seu principal objetivo é permitir que administradores do sistema alterem informações como nome do usuário, grupo principal, diretórios de login, e permissões de acesso, entre outras configurações.

## Usage
A sintaxe básica do comando `usermod` é a seguinte:

```bash
usermod [opções] nome_do_usuario
```

### Opções Comuns:
- `-aG grupo`: Adiciona o usuário a um ou mais grupos suplementares. O `-a` é necessário para evitar que o usuário seja removido de outros grupos.
- `-d diretório`: Altera o diretório home do usuário.
- `-l novo_nome`: Muda o nome de login do usuário.
- `-g grupo`: Define o grupo principal do usuário.
- `-s shell`: Altera o shell padrão do usuário.
- `-u UID`: Modifica o ID do usuário.

## Examples
### Exemplo 1: Adicionar um usuário a um grupo
Para adicionar o usuário `joao` ao grupo `desenvolvedores`, você pode usar o seguinte comando:

```bash
sudo usermod -aG desenvolvedores joao
```

### Exemplo 2: Alterar o diretório home de um usuário
Se você deseja mudar o diretório home do usuário `maria` para `/home/maria_nova`, utilize o comando:

```bash
sudo usermod -d /home/maria_nova maria
```

## Tips
- Sempre faça um backup das configurações do sistema antes de realizar alterações significativas nas contas de usuário.
- Utilize o comando `id nome_do_usuario` para verificar as informações do usuário antes e depois de fazer alterações.
- Lembre-se de que algumas alterações, como mudar o grupo principal, podem exigir que o usuário faça logout e login novamente para que as mudanças tenham efeito.
- Use o comando `usermod` com cautela, especialmente em sistemas de produção, para evitar a perda de acesso a contas importantes.
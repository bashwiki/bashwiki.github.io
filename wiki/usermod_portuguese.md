# [Linux] Bash usermod Uso: Modificar contas de usuário

O comando `usermod` é utilizado para modificar contas de usuário no sistema Linux.

## Overview
O comando `usermod` permite que administradores do sistema alterem informações sobre contas de usuário, como nome, grupo, diretório home e permissões. É uma ferramenta essencial para gerenciar usuários em um ambiente Linux.

## Usage
A sintaxe básica do comando `usermod` é a seguinte:

```bash
usermod [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `usermod`:

- `-aG [grupo]`: Adiciona o usuário a um grupo sem removê-lo de outros grupos.
- `-d [diretório]`: Muda o diretório home do usuário.
- `-l [novo_nome]`: Altera o nome de login do usuário.
- `-g [grupo]`: Define o grupo primário do usuário.
- `-s [shell]`: Altera o shell padrão do usuário.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `usermod`:

1. **Adicionar um usuário a um grupo**:
   ```bash
   usermod -aG sudo nome_do_usuario
   ```

2. **Mudar o diretório home de um usuário**:
   ```bash
   usermod -d /novo/diretorio nome_do_usuario
   ```

3. **Alterar o nome de login de um usuário**:
   ```bash
   usermod -l novo_nome nome_atual
   ```

4. **Definir um novo grupo primário para um usuário**:
   ```bash
   usermod -g novo_grupo nome_do_usuario
   ```

5. **Alterar o shell padrão de um usuário**:
   ```bash
   usermod -s /bin/zsh nome_do_usuario
   ```

## Tips
- Sempre faça um backup das informações do usuário antes de realizar alterações significativas.
- Use a opção `-aG` ao adicionar um usuário a grupos para evitar a remoção de outros grupos existentes.
- Verifique as alterações feitas utilizando o comando `id nome_do_usuario` para confirmar as modificações.
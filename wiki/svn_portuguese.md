# [Linux] Bash svn Uso: Gerenciar repositórios Subversion

## Overview
O comando `svn` é utilizado para interagir com repositórios Subversion (SVN), permitindo que os usuários realizem operações como checkout, commit, update e muito mais. É uma ferramenta essencial para o controle de versão em projetos de desenvolvimento de software.

## Usage
A sintaxe básica do comando `svn` é a seguinte:

```bash
svn [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `svn`:

- `checkout`: Faz o download de um repositório ou parte dele para o diretório local.
- `commit`: Envia as alterações feitas no diretório de trabalho para o repositório.
- `update`: Atualiza o diretório de trabalho com as últimas alterações do repositório.
- `add`: Adiciona novos arquivos ou diretórios ao repositório.
- `delete`: Remove arquivos ou diretórios do repositório.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `svn`:

### 1. Fazer checkout de um repositório
```bash
svn checkout https://exemplo.com/repositorio
```

### 2. Enviar alterações para o repositório
```bash
svn commit -m "Mensagem de commit"
```

### 3. Atualizar o diretório de trabalho
```bash
svn update
```

### 4. Adicionar um novo arquivo ao repositório
```bash
svn add novo_arquivo.txt
```

### 5. Remover um arquivo do repositório
```bash
svn delete arquivo_antigo.txt
```

## Tips
- Sempre faça um `svn update` antes de começar a trabalhar para garantir que você tenha a versão mais recente do código.
- Use mensagens de commit claras e descritivas para facilitar o entendimento das alterações feitas.
- Considere usar branches para desenvolver novas funcionalidades sem afetar a versão principal do projeto.
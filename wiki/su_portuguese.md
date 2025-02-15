# [리눅스] Bash su 사용법

## Overview
O comando `su` (substitute user) é utilizado no sistema operacional Linux para mudar o usuário atual para outro usuário. O principal propósito do `su` é permitir que um usuário execute comandos com as permissões de outro usuário, geralmente o usuário root, que possui privilégios administrativos. Isso é especialmente útil para tarefas que requerem acesso elevado ao sistema.

## Usage
A sintaxe básica do comando `su` é a seguinte:

```bash
su [opções] [usuário]
```

### Opções Comuns:
- `-` ou `--login`: Inicia uma sessão de login como o usuário especificado, carregando o ambiente do usuário.
- `-c`: Permite que você execute um comando específico como o usuário alvo.
- `-m` ou `--preserve-environment`: Preserva o ambiente do usuário atual ao mudar para o usuário especificado.

Se o usuário não for especificado, o comando `su` assume que você deseja mudar para o usuário root.

## Examples
### Exemplo 1: Mudar para o usuário root
Para mudar para o usuário root e iniciar uma sessão de login, você pode usar o seguinte comando:

```bash
su -
```
Após executar este comando, será solicitado que você insira a senha do usuário root.

### Exemplo 2: Executar um comando como outro usuário
Se você deseja executar um comando específico como um usuário diferente, use a opção `-c`. Por exemplo, para listar os arquivos no diretório home do usuário "usuario":

```bash
su -c 'ls ~usuario' usuario
```
Neste caso, você será solicitado a inserir a senha do "usuario".

## Tips
- Sempre tenha cuidado ao usar o `su`, especialmente ao mudar para o usuário root, pois você pode inadvertidamente modificar ou excluir arquivos críticos do sistema.
- Considere usar `sudo` em vez de `su` para executar comandos com privilégios elevados, pois `sudo` oferece um controle mais granular sobre quais comandos podem ser executados e permite auditoria de comandos executados.
- Mantenha suas senhas seguras e não compartilhe credenciais de acesso com outros usuários para evitar comprometer a segurança do sistema.
# [리눅스] Bash svn 사용법

## Overview
O comando `svn` é uma ferramenta de controle de versão que faz parte do Apache Subversion. Ele permite que desenvolvedores e engenheiros gerenciem mudanças em arquivos e diretórios ao longo do tempo, possibilitando a colaboração em projetos de software. O `svn` é amplamente utilizado para rastrear alterações, reverter para versões anteriores e manter um histórico de modificações, facilitando o trabalho em equipe e a manutenção de código.

## Usage
A sintaxe básica do comando `svn` é a seguinte:

```
svn [opções] [subcomando] [argumentos]
```

### Comandos Comuns
- `checkout`: Baixa uma cópia de trabalho do repositório.
- `commit`: Envia alterações locais para o repositório.
- `update`: Atualiza a cópia de trabalho com as últimas alterações do repositório.
- `add`: Adiciona novos arquivos ou diretórios ao controle de versão.
- `delete`: Remove arquivos ou diretórios do controle de versão.
- `status`: Mostra o status dos arquivos na cópia de trabalho.

### Opções Comuns
- `-m "mensagem"`: Adiciona uma mensagem de log ao comando `commit`.
- `-q`: Executa o comando em modo silencioso, sem exibir mensagens.
- `--force`: Força a execução de um comando, mesmo que haja conflitos.

## Examples
### Exemplo 1: Baixando um repositório
Para baixar uma cópia de trabalho de um repositório, você pode usar o comando `checkout`:

```bash
svn checkout https://exemplo.com/repositorio/trunk
```

### Exemplo 2: Enviando alterações
Após fazer alterações em sua cópia de trabalho, você pode enviar essas alterações para o repositório usando o comando `commit`:

```bash
svn commit -m "Corrigido bug na função de login"
```

## Tips
- Sempre faça um `svn update` antes de iniciar novas alterações para garantir que sua cópia de trabalho esteja atualizada.
- Utilize mensagens de commit descritivas para facilitar o entendimento das mudanças feitas.
- Revise o status dos arquivos com `svn status` para ver quais arquivos foram modificados, adicionados ou removidos antes de realizar um commit.
- Considere usar branches para desenvolver novas funcionalidades sem afetar a versão principal do projeto.
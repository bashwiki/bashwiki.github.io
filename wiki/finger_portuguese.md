# [Linux] Bash finger uso: Exibir informações sobre usuários do sistema

## Overview
O comando `finger` é utilizado para exibir informações sobre usuários no sistema, como nome, terminal, data de login e tempo de atividade. Ele é útil para obter uma visão rápida sobre quem está logado e algumas informações adicionais sobre cada usuário.

## Usage
A sintaxe básica do comando `finger` é a seguinte:

```bash
finger [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `finger`:

- `-l`: Exibe informações detalhadas sobre os usuários, incluindo o diretório inicial e a shell.
- `-m`: Ignora a distinção entre maiúsculas e minúsculas ao procurar usuários.
- `-s`: Exibe uma lista resumida dos usuários logados, mostrando apenas os nomes e os terminais.

## Common Examples

### Exibir informações sobre todos os usuários logados
```bash
finger
```

### Exibir informações detalhadas sobre um usuário específico
```bash
finger nome_do_usuario
```

### Exibir informações resumidas sobre os usuários logados
```bash
finger -s
```

### Ignorar a distinção entre maiúsculas e minúsculas ao procurar um usuário
```bash
finger -m Nome_Do_Usuario
```

### Exibir informações detalhadas sobre todos os usuários
```bash
finger -l
```

## Tips
- Utilize `finger` em scripts para monitorar usuários logados e suas atividades.
- Combine `finger` com outros comandos, como `grep`, para filtrar informações específicas.
- Lembre-se de que o `finger` pode não estar instalado por padrão em todas as distribuições Linux; você pode precisar instalá-lo usando o gerenciador de pacotes da sua distribuição.
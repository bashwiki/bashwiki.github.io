# [Linux] Bash shopt Uso: Configura opções de shell

## Overview
O comando `shopt` é utilizado no Bash para modificar opções de comportamento do shell. Ele permite que os usuários ativem ou desativem funcionalidades específicas, ajustando a maneira como o shell opera.

## Usage
A sintaxe básica do comando `shopt` é a seguinte:

```bash
shopt [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `shopt`:

- `-s`: Ativa a opção especificada.
- `-u`: Desativa a opção especificada.
- `-p`: Exibe as opções atuais e seus estados (ativado ou desativado).

## Common Examples

### Ativar a opção `cdspell`
Para ativar a correção automática de erros de digitação no comando `cd`, use:

```bash
shopt -s cdspell
```

### Desativar a opção `cdspell`
Para desativar a correção automática de erros de digitação no comando `cd`, use:

```bash
shopt -u cdspell
```

### Listar todas as opções
Para ver todas as opções disponíveis e seus estados, execute:

```bash
shopt -p
```

### Ativar a opção `nullglob`
Para que padrões glob (como `*.txt`) retornem vazio se não houver correspondência, ative a opção `nullglob`:

```bash
shopt -s nullglob
```

### Desativar a opção `nullglob`
Para reverter o comportamento padrão, desative a opção `nullglob`:

```bash
shopt -u nullglob
```

## Tips
- Sempre verifique as opções disponíveis com `shopt -p` antes de fazer alterações, para evitar comportamentos inesperados.
- Use `shopt` em scripts para garantir que o ambiente do shell esteja configurado conforme necessário.
- Lembre-se de que as alterações feitas com `shopt` são específicas para a sessão do shell atual. Se você quiser que sejam permanentes, adicione os comandos ao seu arquivo de inicialização do shell, como `~/.bashrc`.
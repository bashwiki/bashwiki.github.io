# [Linux] Bash mkdir Uso: Criação de diretórios

## Overview
O comando `mkdir` é utilizado para criar novos diretórios no sistema de arquivos. É uma ferramenta essencial para organizar arquivos e pastas de maneira eficiente.

## Usage
A sintaxe básica do comando `mkdir` é a seguinte:

```bash
mkdir [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `mkdir`:

- `-p`: Cria diretórios pai conforme necessário. Se os diretórios intermediários não existirem, eles serão criados.
- `-v`: Exibe uma mensagem para cada diretório que é criado, útil para verificar a execução do comando.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `mkdir`:

1. **Criar um único diretório:**
   ```bash
   mkdir meu_diretorio
   ```

2. **Criar múltiplos diretórios ao mesmo tempo:**
   ```bash
   mkdir dir1 dir2 dir3
   ```

3. **Criar um diretório com subdiretórios:**
   ```bash
   mkdir -p pai/filho/neto
   ```

4. **Criar um diretório e exibir uma mensagem:**
   ```bash
   mkdir -v novo_diretorio
   ```

## Tips
- Sempre use a opção `-p` ao criar uma estrutura de diretórios complexa para evitar erros se os diretórios pai não existirem.
- Utilize a opção `-v` para confirmar que os diretórios foram criados corretamente, especialmente ao criar múltiplos diretórios.
- Verifique as permissões do diretório onde você está tentando criar novos diretórios para evitar erros de permissão.
# [Linux] Bash set uso: Configurar opções do shell

## Overview
O comando `set` no Bash é utilizado para definir ou exibir variáveis de ambiente e opções do shell. Ele permite que os usuários configurem o comportamento do shell de acordo com suas necessidades, tornando-o uma ferramenta poderosa para personalização.

## Usage
A sintaxe básica do comando `set` é a seguinte:

```bash
set [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `set`:

- `-e`: Faz com que o shell saia imediatamente se um comando retornar um status de saída diferente de zero.
- `-u`: Trata variáveis não definidas como um erro e sai imediatamente.
- `-x`: Exibe os comandos e seus argumentos à medida que são executados, útil para depuração.
- `-o`: Permite definir opções do shell, como `-o noclobber` para evitar que arquivos sejam sobrescritos.

## Common Examples

1. **Ativar a saída de depuração:**
   ```bash
   set -x
   ```

2. **Sair ao encontrar um erro:**
   ```bash
   set -e
   ```

3. **Tratar variáveis não definidas como erro:**
   ```bash
   set -u
   ```

4. **Combinar opções:**
   ```bash
   set -eux
   ```

5. **Exibir todas as variáveis de ambiente e opções atuais:**
   ```bash
   set
   ```

## Tips
- Use `set -e` em scripts para evitar que erros não tratados causem comportamentos inesperados.
- Combine `set -u` com `set -e` para garantir que seu script falhe rapidamente em caso de variáveis não definidas.
- Utilize `set -x` durante a depuração para entender melhor o fluxo de execução do seu script.
# [Linux] Bash whoami Uso: Identifica o usuário atual

## Overview
O comando `whoami` é utilizado no Bash para exibir o nome do usuário que está atualmente logado no sistema. É uma maneira simples e rápida de verificar qual conta de usuário está ativa no terminal.

## Usage
A sintaxe básica do comando é a seguinte:

```bash
whoami [opções]
```

## Common Options
O comando `whoami` não possui muitas opções, mas aqui estão algumas que podem ser úteis:

- `--help`: Exibe uma mensagem de ajuda com informações sobre o comando.
- `--version`: Mostra a versão do comando `whoami`.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `whoami`:

1. **Exibir o nome do usuário atual:**
   ```bash
   whoami
   ```

2. **Exibir a ajuda do comando:**
   ```bash
   whoami --help
   ```

3. **Verificar a versão do comando:**
   ```bash
   whoami --version
   ```

## Tips
- Utilize o comando `whoami` em scripts para verificar qual usuário está executando o script, garantindo que as permissões estejam corretas.
- Combine `whoami` com outros comandos, como `sudo`, para verificar se você está executando como superusuário.
- Lembre-se de que o `whoami` é sensível ao contexto do terminal em que está sendo executado, portanto, pode retornar resultados diferentes se você estiver usando `su` ou `sudo` para mudar de usuário.
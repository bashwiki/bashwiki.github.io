# [Linux] Bash getenforce Uso: Verifica o status do SELinux

## Overview
O comando `getenforce` é utilizado para verificar o status do SELinux (Security-Enhanced Linux) em um sistema. Ele informa se o SELinux está em modo "Enforcing", "Permissive" ou "Disabled", ajudando na administração de políticas de segurança.

## Usage
A sintaxe básica do comando `getenforce` é a seguinte:

```bash
getenforce [opções]
```

## Common Options
O comando `getenforce` não possui muitas opções, mas aqui estão algumas relevantes:

- `-h`, `--help`: Exibe a ajuda do comando.
- `-V`, `--version`: Mostra a versão do comando.

## Common Examples

1. **Verificar o status do SELinux:**
   Para verificar rapidamente o status do SELinux, você pode usar:
   ```bash
   getenforce
   ```

2. **Exibir ajuda do comando:**
   Para ver as opções disponíveis e obter mais informações sobre o comando:
   ```bash
   getenforce --help
   ```

3. **Verificar a versão do comando:**
   Para saber qual versão do `getenforce` você está utilizando:
   ```bash
   getenforce --version
   ```

## Tips
- Utilize o comando `getenforce` frequentemente para monitorar o status do SELinux, especialmente ao realizar alterações nas políticas de segurança.
- Combine o `getenforce` com outros comandos, como `setenforce`, para gerenciar o SELinux de forma eficaz.
- Lembre-se de que, se o SELinux estiver desativado, algumas políticas de segurança não serão aplicadas, o que pode afetar a segurança do sistema.
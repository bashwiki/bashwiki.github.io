# [Linux] Bash cd Uso: Navegar entre diretórios

## Overview
O comando `cd` (change directory) é utilizado para mudar o diretório atual no terminal. Ele permite que você navegue entre diferentes pastas do sistema de arquivos, facilitando o acesso a arquivos e programas.

## Usage
A sintaxe básica do comando `cd` é a seguinte:

```bash
cd [opções] [argumentos]
```

## Common Options
Embora o comando `cd` não tenha muitas opções, algumas das mais comuns incluem:

- `-`: Retorna ao diretório anterior.
- `..`: Muda para o diretório pai do diretório atual.
- `~`: Muda para o diretório home do usuário.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `cd`:

1. **Mudar para um diretório específico:**
   ```bash
   cd /caminho/para/o/diretorio
   ```

2. **Voltar ao diretório anterior:**
   ```bash
   cd -
   ```

3. **Subir um nível no diretório:**
   ```bash
   cd ..
   ```

4. **Ir para o diretório home do usuário:**
   ```bash
   cd ~
   ```

5. **Navegar para um diretório relativo:**
   ```bash
   cd pasta/subpasta
   ```

## Tips
- Utilize `cd -` para alternar rapidamente entre dois diretórios.
- Use `cd ..` repetidamente para subir vários níveis na hierarquia de diretórios.
- Você pode usar a tecla `Tab` para autocompletar nomes de diretórios, economizando tempo e evitando erros de digitação.
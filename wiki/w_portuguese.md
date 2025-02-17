# [Linux] Bash w: Exibir informações sobre usuários logados

## Overview
O comando `w` é utilizado para mostrar quem está logado no sistema e o que estão fazendo. Ele fornece informações detalhadas sobre os usuários, como o tempo de atividade, o terminal em que estão logados e a carga do sistema.

## Usage
A sintaxe básica do comando `w` é a seguinte:

```bash
w [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `w`:

- `-h`: Remove o cabeçalho da saída.
- `-s`: Exibe a saída em um formato mais curto, omitindo informações como o tempo de inatividade.
- `-u`: Mostra o tempo de inatividade dos usuários.
- `-f`: Exibe informações sobre o terminal de cada usuário.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `w`:

1. **Exibir informações padrão sobre usuários logados:**
   ```bash
   w
   ```

2. **Exibir informações sem o cabeçalho:**
   ```bash
   w -h
   ```

3. **Exibir informações em formato curto:**
   ```bash
   w -s
   ```

4. **Exibir informações com tempo de inatividade:**
   ```bash
   w -u
   ```

5. **Exibir informações detalhadas sobre o terminal:**
   ```bash
   w -f
   ```

## Tips
- Utilize `w` regularmente para monitorar a atividade dos usuários em sistemas multiusuário.
- Combine `w` com outros comandos, como `grep`, para filtrar informações específicas sobre usuários.
- Lembre-se de que a saída do `w` pode ser útil para identificar usuários inativos ou para auditorias de segurança.
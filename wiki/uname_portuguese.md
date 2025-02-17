# [Linux] Bash uname Uso: Exibe informações do sistema

## Overview
O comando `uname` é utilizado para exibir informações sobre o sistema operacional em que você está trabalhando. Ele fornece detalhes como o nome do kernel, a versão e outros dados relevantes que podem ser úteis para administradores de sistema e desenvolvedores.

## Usage
A sintaxe básica do comando `uname` é a seguinte:

```bash
uname [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o comando `uname`:

- `-a`: Exibe todas as informações disponíveis sobre o sistema.
- `-s`: Mostra o nome do kernel.
- `-n`: Exibe o nome do host da máquina.
- `-r`: Mostra a versão do kernel.
- `-v`: Exibe a data e hora da versão do kernel.
- `-m`: Mostra a arquitetura da máquina (por exemplo, x86_64).
- `-p`: Exibe o tipo de processador, se disponível.
- `-i`: Mostra a plataforma do hardware, se disponível.
- `-o`: Exibe o nome do sistema operacional.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `uname`:

1. **Exibir todas as informações do sistema:**

   ```bash
   uname -a
   ```

2. **Mostrar apenas o nome do kernel:**

   ```bash
   uname -s
   ```

3. **Exibir a versão do kernel:**

   ```bash
   uname -r
   ```

4. **Mostrar a arquitetura da máquina:**

   ```bash
   uname -m
   ```

5. **Exibir o nome do host:**

   ```bash
   uname -n
   ```

## Tips
- Utilize `uname -a` para obter uma visão geral completa do sistema em um único comando.
- Combine `uname` com outros comandos, como `grep`, para filtrar informações específicas.
- Lembre-se de que as opções podem variar entre diferentes distribuições do Linux, então consulte a página de manual (`man uname`) para detalhes adicionais.
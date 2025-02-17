# [Linux] Bash gcc Uso: Compilador de código-fonte C e C++

## Overview
O comando `gcc` (GNU Compiler Collection) é um compilador que transforma código-fonte escrito em linguagens como C e C++ em executáveis. Ele é amplamente utilizado em sistemas Linux e Unix para compilar programas e bibliotecas.

## Usage
A sintaxe básica do comando `gcc` é a seguinte:

```bash
gcc [opções] [arquivos]
```

## Common Options
Aqui estão algumas opções comuns do `gcc`:

- `-o <arquivo>`: Especifica o nome do arquivo de saída.
- `-Wall`: Ativa todos os avisos recomendados.
- `-g`: Inclui informações de depuração no executável.
- `-O2`: Ativa otimizações de nível 2 para melhorar o desempenho do código.
- `-I<diretório>`: Adiciona um diretório à lista de diretórios de inclusão para arquivos de cabeçalho.
- `-L<diretório>`: Adiciona um diretório à lista de diretórios de busca para bibliotecas.

## Common Examples
Aqui estão alguns exemplos práticos de uso do `gcc`:

1. Compilar um único arquivo C:
   ```bash
   gcc -o meu_programa meu_programa.c
   ```

2. Compilar com avisos ativados:
   ```bash
   gcc -Wall -o meu_programa meu_programa.c
   ```

3. Compilar um arquivo C com informações de depuração:
   ```bash
   gcc -g -o meu_programa meu_programa.c
   ```

4. Compilar múltiplos arquivos C:
   ```bash
   gcc -o meu_programa arquivo1.c arquivo2.c
   ```

5. Usar otimizações durante a compilação:
   ```bash
   gcc -O2 -o meu_programa meu_programa.c
   ```

## Tips
- Sempre use a opção `-Wall` para capturar possíveis problemas no seu código.
- Mantenha seu código organizado em múltiplos arquivos para facilitar a manutenção e a compilação.
- Utilize a opção `-g` durante o desenvolvimento para facilitar a depuração com ferramentas como `gdb`.
- Considere usar um Makefile para gerenciar projetos maiores, facilitando a compilação de múltiplos arquivos.
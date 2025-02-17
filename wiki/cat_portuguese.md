# [Linux] Bash cat uso: Exibir o conteúdo de arquivos

## Overview
O comando `cat` é utilizado para concatenar e exibir o conteúdo de arquivos no terminal. Ele é uma ferramenta simples, mas poderosa, que permite visualizar rapidamente o conteúdo de um ou mais arquivos de texto.

## Usage
A sintaxe básica do comando `cat` é a seguinte:

```bash
cat [opções] [arquivos]
```

## Common Options
Aqui estão algumas opções comuns do comando `cat`:

- `-n`: Numera todas as linhas da saída.
- `-b`: Numera apenas as linhas não vazias.
- `-E`: Exibe um símbolo `$` no final de cada linha.
- `-s`: Suprime linhas em branco consecutivas.
- `-A`: Exibe caracteres não imprimíveis de forma visível.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `cat`:

1. **Exibir o conteúdo de um arquivo:**
   ```bash
   cat arquivo.txt
   ```

2. **Concatenar dois arquivos e exibir o resultado:**
   ```bash
   cat arquivo1.txt arquivo2.txt
   ```

3. **Criar um novo arquivo a partir da entrada do terminal:**
   ```bash
   cat > novo_arquivo.txt
   ```
   (Pressione `CTRL+D` para salvar e sair.)

4. **Exibir o conteúdo de um arquivo com numeração de linhas:**
   ```bash
   cat -n arquivo.txt
   ```

5. **Suprimir linhas em branco consecutivas:**
   ```bash
   cat -s arquivo.txt
   ```

## Tips
- Utilize `cat` em combinação com outros comandos, como `grep`, para filtrar resultados.
- Para visualizar arquivos longos, considere usar `less` ou `more` em vez de `cat`, pois eles permitem rolar pelo conteúdo.
- Ao criar arquivos com `cat`, lembre-se de que o conteúdo anterior será sobrescrito se você não usar `>>` para anexar.
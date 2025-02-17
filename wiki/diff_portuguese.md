# [Linux] Bash diff uso equivalente: Compara arquivos e exibe diferenças

## Overview
O comando `diff` é uma ferramenta poderosa no Bash que permite comparar o conteúdo de dois arquivos ou diretórios, exibindo as diferenças entre eles. Ele é amplamente utilizado para identificar alterações em arquivos de texto, como códigos-fonte ou documentos.

## Usage
A sintaxe básica do comando `diff` é a seguinte:

```bash
diff [opções] [arquivo1] [arquivo2]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `diff`:

- `-u`: Exibe as diferenças em formato unificado, que é mais fácil de ler.
- `-c`: Mostra as diferenças em formato de contexto, fornecendo mais informações sobre as linhas alteradas.
- `-i`: Ignora diferenças de maiúsculas e minúsculas.
- `-w`: Ignora espaços em branco ao comparar as linhas.
- `-r`: Compara diretórios recursivamente.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `diff`:

1. Comparar dois arquivos de texto:
   ```bash
   diff arquivo1.txt arquivo2.txt
   ```

2. Comparar arquivos com saída em formato unificado:
   ```bash
   diff -u arquivo1.txt arquivo2.txt
   ```

3. Comparar diretórios recursivamente:
   ```bash
   diff -r diretorio1/ diretorio2/
   ```

4. Ignorar diferenças de maiúsculas e minúsculas:
   ```bash
   diff -i arquivo1.txt arquivo2.txt
   ```

5. Comparar arquivos e ignorar espaços em branco:
   ```bash
   diff -w arquivo1.txt arquivo2.txt
   ```

## Tips
- Sempre utilize a opção `-u` para uma saída mais legível, especialmente ao revisar alterações em códigos.
- Quando comparar diretórios, a opção `-r` é útil para garantir que todas as subpastas e arquivos sejam incluídos na comparação.
- Combine opções para personalizar a comparação conforme necessário, como `diff -u -w arquivo1.txt arquivo2.txt` para ignorar espaços em branco e usar o formato unificado.
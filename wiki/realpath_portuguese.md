# [Linux] Bash realpath Uso: Resolve caminhos absolutos de arquivos

## Overview
O comando `realpath` é utilizado para resolver e exibir o caminho absoluto de arquivos e diretórios. Ele transforma caminhos relativos em caminhos absolutos, facilitando a localização de arquivos no sistema de arquivos.

## Usage
A sintaxe básica do comando `realpath` é a seguinte:

```bash
realpath [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `realpath`:

- `-m`, `--canonicalize-missing`: Resolve o caminho, mas não gera um erro se o arquivo não existir.
- `-q`, `--quiet`: Não exibe mensagens de erro.
- `-s`, `--strip`: Remove o prefixo do caminho, se especificado.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `realpath`:

1. **Resolver um caminho absoluto:**
   ```bash
   realpath ./documento.txt
   ```

2. **Resolver um caminho de diretório:**
   ```bash
   realpath /home/usuario/pasta/
   ```

3. **Usar a opção `-m` para caminhos que podem não existir:**
   ```bash
   realpath -m ./arquivo_inexistente.txt
   ```

4. **Combinar com `-q` para suprimir mensagens de erro:**
   ```bash
   realpath -q ./arquivo_inexistente.txt
   ```

5. **Resolver um caminho com a opção `-s`:**
   ```bash
   realpath -s /home/usuario/pasta/../documento.txt
   ```

## Tips
- Utilize `realpath` em scripts para garantir que os caminhos utilizados sejam absolutos, evitando confusões com caminhos relativos.
- Combine `realpath` com outros comandos, como `cd`, para navegar diretamente para o diretório absoluto de um arquivo.
- Sempre verifique se o caminho que você está tentando resolver é acessível, especialmente ao usar a opção `-m`.
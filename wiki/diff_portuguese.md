# [리눅스] Bash diff 사용법

## Overview
O comando `diff` é uma ferramenta poderosa utilizada em sistemas Unix e Linux para comparar arquivos de texto. Seu principal objetivo é identificar as diferenças entre dois arquivos, mostrando quais linhas foram adicionadas, removidas ou modificadas. Isso é especialmente útil para desenvolvedores e engenheiros que precisam revisar alterações em código-fonte ou documentos.

## Usage
A sintaxe básica do comando `diff` é a seguinte:

```
diff [opções] arquivo1 arquivo2
```

### Opções Comuns:
- `-u`: Exibe as diferenças em um formato unificado, que é mais fácil de ler.
- `-c`: Mostra as diferenças em um formato de contexto, que inclui algumas linhas de contexto ao redor das mudanças.
- `-i`: Ignora diferenças entre maiúsculas e minúsculas.
- `-w`: Ignora espaços em branco ao comparar linhas.
- `-r`: Compara diretórios recursivamente.

## Examples
### Exemplo 1: Comparando dois arquivos de texto
Suponha que você tenha dois arquivos, `versao1.txt` e `versao2.txt`, e deseja ver as diferenças entre eles. Você pode usar o seguinte comando:

```bash
diff versao1.txt versao2.txt
```

### Exemplo 2: Usando o formato unificado
Para uma visualização mais clara das diferenças, você pode usar a opção `-u`:

```bash
diff -u versao1.txt versao2.txt
```

Isso mostrará as diferenças em um formato que destaca as linhas adicionadas e removidas, facilitando a revisão das alterações.

## Tips
- Sempre utilize a opção `-u` ao compartilhar as saídas do `diff` com outros, pois o formato unificado é mais legível e amplamente aceito.
- Ao comparar diretórios, a opção `-r` pode ser muito útil para verificar alterações em múltiplos arquivos de uma só vez.
- Combine o `diff` com outras ferramentas, como `patch`, para aplicar as diferenças encontradas em um arquivo original, facilitando a atualização de versões de arquivos.
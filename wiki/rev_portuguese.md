# [Linux] Bash rev: Inverte linhas de texto

## Overview
O comando `rev` é utilizado para inverter as linhas de um arquivo ou a entrada padrão. Ele lê cada linha de texto e a reverte, apresentando o resultado na saída padrão. É uma ferramenta simples, mas útil em várias situações, como manipulação de strings e formatação de dados.

## Usage
A sintaxe básica do comando `rev` é a seguinte:

```bash
rev [opções] [argumentos]
```

## Common Options
- `-o, --output=ARQUIVO`: Especifica um arquivo de saída para armazenar o resultado.
- `-h, --help`: Exibe uma mensagem de ajuda com informações sobre o uso do comando.
- `-V, --version`: Mostra a versão do comando `rev`.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `rev`:

1. **Inverter uma linha de texto diretamente no terminal:**

```bash
echo "Olá Mundo" | rev
```
Saída:
```
odnu olA
```

2. **Inverter o conteúdo de um arquivo:**

```bash
rev arquivo.txt
```
Este comando lê o arquivo `arquivo.txt` e inverte cada linha.

3. **Salvar a saída invertida em um novo arquivo:**

```bash
rev arquivo.txt -o arquivo_invertido.txt
```
Aqui, o conteúdo de `arquivo.txt` é invertido e salvo em `arquivo_invertido.txt`.

4. **Inverter várias linhas de texto:**

```bash
cat <<EOF | rev
Linha 1
Linha 2
Linha 3
EOF
```
Saída:
```
1 anil
2 anil
3 anil
```

## Tips
- Utilize `rev` em combinação com outros comandos, como `grep` ou `sort`, para manipulações mais complexas de texto.
- Lembre-se de que `rev` inverte apenas as linhas, e não o conteúdo de palavras individuais. Se você precisar inverter palavras, considere usar outras ferramentas como `awk` ou `sed`.
- Teste o comando com arquivos pequenos antes de aplicá-lo em arquivos maiores para garantir que o resultado atenda às suas expectativas.
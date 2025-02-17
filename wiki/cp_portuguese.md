# [Linux] Bash cp Uso: Copiar arquivos e diretórios

## Overview
O comando `cp` é utilizado no Bash para copiar arquivos e diretórios de um local para outro. Ele permite que você crie cópias de arquivos existentes, facilitando o gerenciamento e a organização de dados no sistema.

## Usage
A sintaxe básica do comando `cp` é a seguinte:

```bash
cp [opções] [origem] [destino]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `cp`:

- `-r`: Copia diretórios recursivamente.
- `-i`: Pergunta antes de sobrescrever arquivos existentes.
- `-u`: Copia apenas arquivos que são novos ou que foram modificados.
- `-v`: Exibe os arquivos que estão sendo copiados.
- `-a`: Copia arquivos e diretórios de forma recursiva, preservando atributos.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `cp`:

1. **Copiar um arquivo para outro local:**
   ```bash
   cp arquivo.txt /caminho/para/destino/
   ```

2. **Copiar um diretório e seu conteúdo:**
   ```bash
   cp -r /caminho/para/diretorio /caminho/para/destino/
   ```

3. **Copiar um arquivo e perguntar antes de sobrescrever:**
   ```bash
   cp -i arquivo.txt /caminho/para/destino/
   ```

4. **Copiar apenas arquivos que foram modificados:**
   ```bash
   cp -u arquivo.txt /caminho/para/destino/
   ```

5. **Copiar um arquivo e exibir o progresso:**
   ```bash
   cp -v arquivo.txt /caminho/para/destino/
   ```

## Tips
- Sempre verifique o caminho de destino antes de executar o comando `cp` para evitar sobrescrever arquivos importantes.
- Utilize a opção `-i` para evitar a perda acidental de dados ao sobrescrever arquivos.
- Para cópias de segurança, considere usar a opção `-a` para preservar as permissões e atributos dos arquivos.